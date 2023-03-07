# TD7A4

Etapes pour lancer l'application:

1) Créer l'image avec le Dockerfile
  
  Pour cela lancer le terminal dans le dossier où se trouve le Dockerfile et lancer la commande:
  "docker build -t image-td6 ."
  
2) Lancer le docker-compose

  Le docker-compose créera les conteneurs des images "image-td6" (image de notre application python) et "mongo", créera le network pour relier les deux conteneurs, créera bind mount pour que notre conteneur de l'application python puisse récupérer les données de notre fichier "file.txt" en local (ne pas oublier de changer le chemin du fichier en local car il sera forcément différent du mien) et enfin créera un volume pour rendre les données de notre database persistants.
  Pour cela lancer la commande:
  "docker-compose up"
  
3) Lancer l'application

  Utiliser les commandes suivantes pour démarrer vos conteneurs:
  "docker start mongo-td6"
  "docker start container-td6"
  
  Puis pour lancer l'application:
  "docker exec -it container-td6"
  
 Voici le résultat que vous devriez avoir:
 ![image](https://user-images.githubusercontent.com/79918333/222913848-452d19de-2e19-45d8-9baa-d1dd10bb057e.png)

   
