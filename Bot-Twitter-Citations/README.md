# Bot Twitter de Citations

Un bot qui génère des citations inspirantes en fonction d'un fichier et qui les présente sur des images de fond :

<img src="https://image.noelshack.com/fichiers/2018/19/3/1525833428-capture-1.png" />

Le bot est aussi capable de répondre à un tweet avec une citation quand on lui demande : 

<img src="https://image.noelshack.com/fichiers/2018/19/3/1525833429-capture-2.png" />

# Installation 

1. Télécharger le répertoire Github, puis dans la console : 

```
cd repertoire_des_fichiers
pip install -r requirements.txt
mkdir output
```

2. Editer le fichier secret.py 

```
consumer_key = 'CONSUMER_KEY'
consumer_secret = 'CONSUMER_SECRET'
access_token = 'ACCESS_TOKEN'
access_secret = 'ACCESS_SECRET'
```

Pour trouver ces valeurs, il faut déclarer une nouvelle application sur https://apps.twitter.com/. Après avoir créé une nouvelle application, les informations sont dans l'onglet "Key & Access Tokens"

3. Renseigner le nom du compte qui postera les tweets dans le fichier conf.py 

```
bot_name = "@Compte_Twitter"
fichier_citations = "citations.txt"
tweet_with_picture = True # Remplacer pour une citation textuelle sans image
time_between_tweets = 21600 # Le temps entre deux tweets, ici 6 heures
reply_with_picture = True 
regex_reply = "[cC]itation" # Chaîne qui déclenche une réponse 
text_reply = "Voici ta citation :" # Texte qui accompagne la réponse
```

4. dans la console : 
```
python run_post.py &
python run_reply.py &
```

le caractère optionnel "&" à la fin signifie "éxecuter en tâche de fond".

5. Infos : 

les fonds sont à placer dans le dossier /input, les polices de caractères dans le dossier /fonts, les images générées seront placées dans le dossier /output

# Remerciements et documentation : 

la library pour générer des citations vient de : https://github.com/owocki/quotify 
documentation de tweepy : http://docs.tweepy.org/en/v3.5.0/

C'est la première fois que je partage quelque chose sur Github, soyez indulgents :-) ! 
