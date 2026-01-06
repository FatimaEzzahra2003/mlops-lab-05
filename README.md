# MLOps Lab – Docker et conteneurs

Ce lab explique comment **utiliser Docker** pour lancer des conteneurs, comprendre la structure d’une commande `docker run`, et conteneuriser l’API churn du projet `mlops-lab-01`.

## Étape 1 : Vérifier l’installation de Docker

<img width="753" height="127" alt="image" src="https://github.com/user-attachments/assets/c8146cc2-6fcb-4545-95cd-b0b74dd609dd" />


<img width="941" height="100" alt="image" src="https://github.com/user-attachments/assets/e5f9dbc3-1ea8-4fb3-9fff-5ce706302a8b" />


## Étape 2 : Lancer un serveur Nginx dans un conteneur


<img width="941" height="148" alt="image" src="https://github.com/user-attachments/assets/3bb2e606-0778-4af1-b11f-2a453860f388" />


<img width="941" height="288" alt="image" src="https://github.com/user-attachments/assets/9d184f17-e8b6-4877-afce-15b76a3b73db" />


* Arrêter et supprimer le conteneur :

<img width="683" height="236" alt="image" src="https://github.com/user-attachments/assets/9afb924d-350b-4e45-9aff-438e118b81b9" />


## Étape 3 : Ouvrir un shell Linux isolé dans un conteneur

<img width="941" height="500" alt="image" src="https://github.com/user-attachments/assets/f11f26c2-f0ad-4493-84e1-14fd06fe90a3" />


Dans le conteneur :


<img width="941" height="442" alt="image" src="https://github.com/user-attachments/assets/3d9f4e3a-be5f-4916-8a66-8bff62a1ea5c" />


<img width="941" height="566" alt="image" src="https://github.com/user-attachments/assets/b2918a0b-b6d9-4b9b-a0cd-7a0d5ac546f4" />



Vérifier conteneur arrêté :


<img width="941" height="103" alt="image" src="https://github.com/user-attachments/assets/e4de98a3-2024-44a0-8d77-5a4e6183a12d" />


<img width="669" height="136" alt="image" src="https://github.com/user-attachments/assets/ca802ef1-d2ce-487a-aff2-81b7604b276a" />


## Étape 4 : Comprendre la structure d’une commande `docker run`


<img width="941" height="124" alt="image" src="https://github.com/user-attachments/assets/30811654-3439-4192-b170-eaa06f18e87b" />


Arrêter et supprimer :

<img width="675" height="136" alt="image" src="https://github.com/user-attachments/assets/7fe50a4c-e13c-418c-9dc6-e18cd05514b8" />


## Étape 5 : Conteneuriser l’API churn du projet mlops-lab-01


<img width="763" height="741" alt="image" src="https://github.com/user-attachments/assets/ca0a924d-39ca-483c-afc6-bf122bf2a591" />


* Vérifier l’API en local :

<img width="941" height="226" alt="image" src="https://github.com/user-attachments/assets/61660ec1-a803-4b94-9d70-f61a8ae1769b" />



## Étape 6 : Créer `requirements.txt`


<img width="941" height="304" alt="image" src="https://github.com/user-attachments/assets/af7da181-931d-4dfa-8585-63a3851b4a47" />



## Étape 7 : Créer le Dockerfile


<img width="560" height="454" alt="image" src="https://github.com/user-attachments/assets/c84c5e92-9c5d-4622-9f1b-58e0e3e1d468" />



## Étape 8 : Préparer un modèle actif

* Vérifier qu’un modèle existe dans `models/` :
  
<img width="941" height="394" alt="image" src="https://github.com/user-attachments/assets/46847029-ea6f-4a14-be4d-3d63aea118a0" />


# Note importante – Problème de stockage

## À partir de cette étape, un **problème majeur de stockage disque** est survenu sur ma machine locale (espace insuffisant pour construire les images Docker).Pour continuer et finaliser le lab, les étapes suivantes ont été **réalisées sur la machine d’une collègue**, dans les mêmes conditions .

## Étape 9 : Construire l’image Docker


<img width="932" height="289" alt="image" src="https://github.com/user-attachments/assets/8b9b552a-ad46-49e5-80bd-894130409154" />


![imgdocker](https://github.com/user-attachments/assets/a52ca618-dde8-4681-9ee8-3130b1ee0a70)


## Étape 10 : Lancer l’API churn dans un conteneur


<img width="945" height="83" alt="image" src="https://github.com/user-attachments/assets/5e69934b-b365-4c2c-ac44-6979cd04b261" />


<img width="945" height="162" alt="image" src="https://github.com/user-attachments/assets/275c98f5-917e-4126-9c5f-26264caf9ecf" />


<img width="945" height="162" alt="image" src="https://github.com/user-attachments/assets/775a41d4-6fe9-444e-a89d-bb55745a6766" />


## Étape 11 : Vérifier les logs

<img width="945" height="55" alt="image" src="https://github.com/user-attachments/assets/ab4017e7-3bb9-4034-b876-91a0f6e66392" />


<img width="945" height="78" alt="image" src="https://github.com/user-attachments/assets/b7c8e887-f352-47a8-84ab-ed5e3bf1d0fa" />


<img width="945" height="79" alt="image" src="https://github.com/user-attachments/assets/b5b01326-911b-4a53-9a7b-9c579aeeb3da" />


<img width="945" height="161" alt="image" src="https://github.com/user-attachments/assets/8203e13f-6ba3-4505-b429-4a20ac0cc326" />


## Étape 12 : Orchestration locale avec Docker Compose


<img width="650" height="284" alt="image" src="https://github.com/user-attachments/assets/d9c136e0-4f7b-4237-ab99-ab7ae89412b8" />


## Étape 13 : Démarrer l’API avec Docker Compose


<img width="945" height="311" alt="image" src="https://github.com/user-attachments/assets/d991e325-6408-4a82-aec5-beab09d295eb" />


## Étape 14 : Lancer en arrière-plan et observer les logs

<img width="945" height="97" alt="image" src="https://github.com/user-attachments/assets/070ea1cb-2563-4459-97f7-46f4a22279f4" />


<img width="945" height="100" alt="image" src="https://github.com/user-attachments/assets/ddc27dbe-8f4f-430f-9719-16e9aace7514" />


<img width="945" height="423" alt="image" src="https://github.com/user-attachments/assets/324b5e79-dbf8-4eaa-92f3-5cb1134aea8d" />


<img width="945" height="394" alt="image" src="https://github.com/user-attachments/assets/65fcdc42-4ec7-4ede-82d1-3ab4d1ccef69" />



<img width="945" height="448" alt="image" src="https://github.com/user-attachments/assets/43685067-6d29-4883-83af-2bb84bd700c1" />


<img width="945" height="139" alt="image" src="https://github.com/user-attachments/assets/ed3250f4-13e1-41d8-a646-af1e1add782d" />




---

Si tu veux, je peux te préparer **une version avec toutes les images simulées / captures d’écran pour GitHub**, prête à publier directement.

Veux-tu que je fasse ça ?
