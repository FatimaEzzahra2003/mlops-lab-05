from __future__ import annotations
"""
API FastAPI de prédiction de churn pour le lab MLOps.

Ce service :
- charge dynamiquement le modèle courant indiqué dans `registry/current_model.txt`;
- expose un endpoint `/health` pour vérifier l'état de l'API et du modèle;
- expose un endpoint `/predict` pour faire une prédiction de churn;
- journalise chaque requête dans `logs/predictions.log`.

Cette version :
- sécurise l'appel à `predict_proba`;
- recharge le modèle automatiquement si `current_model.txt` change.
"""

import json
import time
from pathlib import Path
from typing import Any, Optional

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# ---------------------------------------------------------------------------
# Constantes de chemin
# ---------------------------------------------------------------------------

ROOT: Path = Path(__file__).resolve().parents[1]
MODELS_DIR: Path = ROOT / "models"
REGISTRY_DIR: Path = ROOT / "registry"
CURRENT_MODEL_PATH: Path = REGISTRY_DIR / "current_model.txt"
LOG_PATH: Path = ROOT / "logs" / "predictions.log"

# ---------------------------------------------------------------------------
# Application FastAPI
# ---------------------------------------------------------------------------

app = FastAPI(title="MLOps Lab 01 - Churn API")

# ---------------------------------------------------------------------------
# Schéma d'entrée
# ---------------------------------------------------------------------------

class PredictRequest(BaseModel):
    tenure_months: int = Field(..., ge=0, le=200)
    num_complaints: int = Field(..., ge=0, le=50)
    avg_session_minutes: float = Field(..., ge=0.0, le=500.0)
    plan_type: str
    region: str
    request_id: Optional[str] = 1

# ---------------------------------------------------------------------------
# Cache de modèle en mémoire
# ---------------------------------------------------------------------------

_model_cache: dict[str, Any] = {"name": None, "model": None, "mtime": None}

# ---------------------------------------------------------------------------
# Fonctions utilitaires
# ---------------------------------------------------------------------------

def get_current_model_name() -> str:
    if not CURRENT_MODEL_PATH.exists():
        raise FileNotFoundError("Aucun modèle courant. Lancer train.py d'abord.")
    name = CURRENT_MODEL_PATH.read_text(encoding="utf-8").strip()
    if not name:
        raise FileNotFoundError("Fichier current_model.txt vide.")
    return name

def load_model_if_needed() -> tuple[str, Any]:
    """
    Recharge le modèle si le fichier a changé ou si le cache est vide.
    """
    name = get_current_model_name()
    current_mtime = CURRENT_MODEL_PATH.stat().st_mtime

    if (_model_cache["name"] == name and
        _model_cache["model"] is not None and
        _model_cache["mtime"] == current_mtime):
        return name, _model_cache["model"]

    path = MODELS_DIR / name
    if not path.exists():
        raise FileNotFoundError(f"Modèle introuvable : {path}")

    model = joblib.load(path)
    _model_cache["name"] = name
    _model_cache["model"] = model
    _model_cache["mtime"] = current_mtime

    print(f"[INFO] Modèle chargé : {name}")
    return name, model

def log_prediction(payload: dict[str, Any]) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as log_file:
        log_file.write(json.dumps(payload, ensure_ascii=False) + "\n")

# ---------------------------------------------------------------------------
# Endpoints FastAPI
# ---------------------------------------------------------------------------

@app.get("/health")
def health() -> dict[str, Any]:
    try:
        model_name = get_current_model_name()
        return {"status": "ok", "current_model": model_name}
    except Exception as exc:
        return {"status": "error", "detail": str(exc)}

@app.post("/predict")
def predict(req: PredictRequest) -> dict[str, Any]:
    try:
        model_name, model = load_model_if_needed()
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    # Normalisation minimale
    features = {
        "tenure_months": req.tenure_months,
        "num_complaints": req.num_complaints,
        "avg_session_minutes": req.avg_session_minutes,
        "plan_type": req.plan_type.strip().lower(),
        "region": req.region.strip().upper(),
    }
    X_df = pd.DataFrame([features])

    start = time.perf_counter()
    try:
        if not hasattr(model, "predict_proba"):
            raise HTTPException(
                status_code=500,
                detail=(
                    f"Modèle incompatible : 'predict_proba' absent. "
                    f"Réentraîner avec scikit-learn ≥1.0."
                ),
            )
        proba = float(model.predict_proba(X_df)[0][1])
        pred = int(proba >= 0.5)
    except HTTPException as exc:
        raise exc
    except Exception as exc:
        raise HTTPException(status_code=400, detail=f"Erreur de prédiction : {exc}") from exc

    latency_ms = (time.perf_counter() - start) * 1000.0

    out: dict[str, Any] = {
        "request_id": req.request_id,
        "model_version": model_name,
        "prediction": pred,
        "probability": round(proba, 6),
        "latency_ms": round(latency_ms, 3),
        "features": features,
        "ts": int(time.time()),
    }

    log_prediction(out)
    return out
