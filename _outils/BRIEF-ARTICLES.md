# Écrire un article du blog PAFOU

Chaque article est un fichier `_outils/articles/<slug>.py` qui définit un dictionnaire `ARTICLE`.
Le contrôle `python3 _outils/verifier_blog.py` doit passer sans erreur.

## Les faits sur PAFOU (ne rien inventer d'autre)

- PAFOU est un jeu de soirée sur iPhone (iOS 16.4 ou plus récent), en français, classé 17+ sur l'App Store. Pas de version Android.
- Téléchargement gratuit, avec achats intégrés. Toujours gratuits : La Pyramide, les fléchettes, et le niveau Tranquille des Dossiers et de Cap d'assumer ?. Les autres modes et niveaux s'essaient une fois, puis demandent un achat (les prix sont affichés dans l'app). Ne JAMAIS écrire de prix, ni « gratuit » sans cette nuance.
- Zéro matériel : chacun son téléphone (on crée un salon, les autres rejoignent avec un code ou un QR code), ou un seul téléphone sur la table selon le jeu.
- Tout se joue à voix haute. L'app n'enregistre jamais les réponses. Pas de publicité dans l'app.
- Les modes :
  - **La Pyramide** (2 à 8 joueurs, environ 20 min) : bluff et mémoire. Chacun mémorise 4 cartes, puis elles sont retournées. 15 cartes sont révélées une à une ; à chaque carte, tu peux affirmer à un pote que tu as la même valeur, vrai ou pas. S'il te croit, tu marques. S'il crie « Menteur », tu dois retourner la bonne carte de mémoire. Podium avec des titres (Roi ou Reine du bluff, Pigeon de la soirée). Jouable aussi sur un seul téléphone.
  - **Les Dossiers** (2 à 8 joueurs, environ 15 min, 3 niveaux : Tranquille, Piquant, Spicy) : tu tires une question que toi seul vois, le hasard désigne à qui tu la poses. Les cartes citent les prénoms des joueurs. Les autres parient si la carte sera jouée ou esquivée.
  - **Cap d'assumer ?** (2 à 8 joueurs, 3 niveaux) : action ou vérité version soirée. Tu désignes quelqu'un, il choisit Action ou Vérité, la carte s'affiche chez tout le monde. On peut toujours passer.
  - **La Tournée** (3 à 8 joueurs, chacun son téléphone, environ 15 min) : douze manches de mini-jeux (sondage, vote, minorité, intrus, réflexe, chrono, bombe). Le perdant d'une manche prend une gorgée de ce qu'il veut, avec ou sans alcool. À citer peu, et jamais en mettant l'alcool en avant.
  - **Le Mode bar** (3 joueurs et plus, un seul téléphone posé sur la table, niveaux Tranquille et Piquant) : 13 cartes qui mélangent Qui de nous, Le Procès, Le Débat débile, Le Mot interdit, Autour du bar, La Mission secrète. Pas de points : le téléphone arbitre, on parle entre nous.
  - **Les fléchettes** (2 à 8 joueurs) : compteur de score 301, 501 et Cricket, option « finir sur un double », on touche la cible à l'écran, annulation d'une fléchette, partie sauvegardée. Sans réseau.
  - **Tête-à-tête** (2 joueurs, un seul téléphone) : pour un premier date. Trois niveaux (Léger, Vrai, Ça chauffe), un vote secret pour passer au niveau suivant, un bilan à la fin, et le perdant paie l'addition. Rien de sexuel.
  - **On se découvre** (3 à 12 joueurs, un seul téléphone) : pour un groupe qui ne se connaît pas. Première impression, Face à face, Deux vérités un mensonge, Le Fait mystère, puis deux équipes : Mime, Même réponse, Mot interdit, Ligne muette. Sans alcool.
  - **Les bandes de potes** : un groupe permanent qu'on rejoint par un lien, classement du mois (3 points par victoire, 1 par partie, remis à zéro chaque mois), titres. Demande un compte « Se connecter avec Apple », sinon le compte est facultatif.
- Plus de 400 cartes. Fait en France, par le collectif La Plateforme.

## Règles d'écriture

- **Tutoiement** partout. Jamais « vous », « votre », « vos ».
- **Aucun emoji**, aucun symbole décoratif.
- **Alcool** : ne jamais encourager à boire, ne jamais parler de « shot », « cul sec », « finir son verre », d'ivresse. Quand un jeu classique fait boire, donne toujours la version « gage » ou « point » et écris que ça se joue sans alcool. PAFOU se présente comme un jeu de soirée, pas comme un jeu à boire.
- **Pas de contenu sexuel ni adulte** : les listes de questions et de gages restent au niveau « tout le monde peut les lire à voix haute devant ses collègues ».
- **Rien d'inventé** : pas de faux avis, pas de chiffres de téléchargements, pas de « n° 1 », pas de « la meilleure app ». Pas d'étude citée. Aucune promesse sur le prix.
- **Concurrents** : tu peux citer seulement Picolo, TOZ, JUDUKU, Undercover, Insight, Vakarm, « Action ou Vérité » de Chouic, DartCounter, et seulement pour dire ce qu'ils sont en une phrase neutre. Jamais de critique.
- **Utile d'abord** : l'article doit servir même à quelqu'un qui n'installe pas PAFOU (vraies règles, vraies listes écrites par toi, étapes concrètes). PAFOU arrive naturellement, une à trois fois, là où il rend le service.
- Phrases courtes, français parlé mais propre. Chaque `<h2>` est une question ou une promesse claire, et le premier paragraphe qui suit répond tout de suite.
- Les listes de questions, de gages ou de mots sont **originales** (ne recopie pas les cartes d'une app).
- Longueur du `corps` : 700 à 1 300 mots.

## Format

```python
ARTICLE = {
  "slug": "mon-article",                 # = nom du fichier
  "categorie": "idees",                  # idees | regles | questions | situations
  "mot_cle": "jeux de soirée sans matériel",   # la recherche visée, unique
  "titre": "…",                          # le H1, 45 à 95 caractères
  "titre_seo": "…",                      # balise title, 60 caractères au plus, contient le mot-clé
  "titre_court": "…",                    # 40 caractères au plus
  "description": "…",                    # 120 à 160 caractères
  "resume": "…",                         # une phrase, 110 caractères au plus
  "perso": "cafe",                       # biere cafe canette champagne cocktail coupe gobelet milk mojito spritz vin whisky
  "jeu": "la-pyramide",                  # la page de jeu la plus liée (voir liste), ou None
  "lire_aussi": ["slug-a", "slug-b"],    # 2 ou 3 autres articles
  "reponse": "…",                        # la réponse courte, 40 à 75 mots, lisible seule
  "en_bref": ["…", "…", "…"],            # 3 ou 4 points, <strong> autorisé
  "corps": """ … HTML … """,
  "faq": [("Question ?", "Réponse en 1 à 3 phrases."), …],   # 3 ou 4 questions
}
```

HTML autorisé dans `corps` : `<h2>`, `<h3>`, `<p>`, `<ul>`, `<ol>`, `<li>`, `<strong>`, `<table>` (avec `<thead>`/`<tbody>`), `<div class="astuce">`.
Au moins 4 `<h2>`. Pas de `<h1>`, pas d'image, pas de style.

Liens internes, jamais de `href` écrit en dur :
- vers un article : `[[slug|texte du lien]]`
- vers une page de jeu : `[[jeu:la-pyramide|texte]]` avec `la-pyramide`, `les-dossiers`, `cap-d-assumer`, `la-tournee`, `mode-bar`, `flechettes`, `tete-a-tete`, `on-se-decouvre`, `bandes-de-potes`
- vers un guide : `[[guide:slug|texte]]` avec `meilleure-app-jeu-de-soiree`, `application-action-ou-verite`, `jeu-de-bluff-entre-amis`, `application-compteur-flechettes`, `jeu-pour-premier-date`, `jeu-de-soiree-sans-materiel`, `alternatives-picolo`

Chaque article contient au moins 2 liens internes, dont au moins un vers une page de jeu ou un guide, et le mot « PAFOU » au moins une fois dans le corps.

## La liste des 30 articles (slugs)

Idées : jeux-de-soiree-entre-potes, jeux-a-deux-en-soiree, jeux-grande-tablee, jeux-de-soiree-sans-alcool, jeux-a-boire-sans-materiel, jeux-anniversaire-adulte, jeux-nouvel-an-entre-amis, jeux-de-bar-entre-amis, jeux-pour-briser-la-glace, jeux-de-noel-entre-amis.
Règles et questions : regles-jeu-de-la-pyramide, questions-action-ou-verite, phrases-je-n-ai-jamais, questions-qui-de-nous, questions-tu-preferes, deux-verites-un-mensonge, regles-flechettes-301-501, regles-cricket-flechettes, regles-jeu-du-menteur, idees-de-gages-soiree.
Situations : questions-premier-date, jeux-pour-un-premier-date, jeux-a-deux-en-couple, compter-les-points-aux-flechettes, relancer-une-soiree-qui-retombe, un-telephone-ou-chacun-le-sien, mots-a-mimer, jeu-de-l-intrus-regles, organiser-une-soiree-jeux, jeux-cremaillere.
