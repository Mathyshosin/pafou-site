# Site PAFOU : état et plan de mise en ligne

Fait le 19/11/2026. **Rien n'est en ligne, rien n'est acheté, rien n'est publié.**

## Ce qui est prêt (dans `~/Projets/pafou-site`)

- **Accueil**, **9 pages de jeux** (`jeux/`), **7 guides comparatifs** (`guides/`), **FAQ** (20 questions), **À propos**, **404**.
- **Blog** : 30 articles écrits d'avance (`_outils/articles/`), 3 publiés le premier jour puis 1 par jour.
- Pour Google et les IA : données structurées (application, FAQ, articles, fil d'Ariane, listes), `sitemap.xml`, `robots.txt` (robots des IA autorisés), `llms.txt`, `llms-full.txt`, flux RSS, images de partage, bandeau « ouvrir dans l'App Store » sur iPhone.
- Robot de publication : `.github/workflows/publier-blog.yml` (gratuit, comme BONGO).
- Kit hors site : `_lancement/HORS-SITE.md`.

Voir le site sur le Mac : aperçu `pafou-site` (http://localhost:8097). L'aperçu montre les 30 articles ; en ligne, il n'y en aura que 3 le premier jour.

## Les commandes

| Pour | Commande (depuis `~/Projets/pafou-site`) |
|---|---|
| Refaire le site | `python3 _outils/generer.py` |
| Contrôler les articles | `python3 _outils/verifier_blog.py` |
| Voir le blog à une date future | `PAFOU_DATE=2026-12-31 python3 _outils/generer.py` |
| Changer un texte de jeu, de guide ou de FAQ | modifier `_outils/contenu.py`, puis refaire le site |
| Écrire de nouveaux articles | suivre `_outils/BRIEF-ARTICLES.md`, ajouter les slugs à la fin de `_outils/blog_calendrier.py` |

## Ce qui attend ton accord

1. **Le nom de domaine.** `pafou.fr` est déjà pris. `pafouapp.fr` est libre (vérifié le 19/11), sur le modèle de `bongoapp.fr` : environ 7 à 10 € par an chez OVH, où tu as déjà tes autres domaines. Autres noms libres : `pafou-app.fr`, `pafoujeu.fr`. Sans domaine, le site peut vivre gratuitement à l'adresse `mathyshosin.github.io/pafou-site`, mais une adresse à soi inspire plus confiance à Google.
2. **L'hébergement.** GitHub Pages, gratuit, comme BONGO : un dépôt public `Mathyshosin/pafou-site`.
3. **La mise en ligne** elle-même.
4. **Le lien du site sur la fiche App Store** (« URL marketing »), à poser avec une prochaine version.
5. **Les liens depuis laplateformestudio.fr et bongoapp.fr.**
6. **Tout le kit hors site** : c'est toi qui postes.

## Le jour J, dans l'ordre (20 minutes)

1. Tu achètes `pafouapp.fr` chez OVH.
2. Je règle le début du blog : `DEBUT` dans `_outils/blog_calendrier.py` = la date du jour. Si le domaine n'est pas `pafouapp.fr`, je change `BASE` dans `_outils/generer.py` et `HOTE` dans `_outils/indexnow.py`.
3. Je refais le site à la vraie date (3 articles), je crée le fichier `CNAME`, le dépôt GitHub, et j'active GitHub Pages.
4. Chez OVH, tu ajoutes les 4 adresses de GitHub (les mêmes que pour bongoapp.fr), ou je te guide.
5. On vérifie que `https://pafouapp.fr` s'ouvre avec le cadenas.
6. Tu déclares le site à Google Search Console et à Bing (section 1 du kit hors site).
7. Le lendemain matin, on vérifie que le robot a bien publié le 4e article.

## À relire avant la mise en ligne

- **Les 7 guides comparatifs** citent d'autres apps (Picolo, TOZ, JUDUKU, Undercover, Insight, Vakarm, Chouic, DartCounter, Cray Cray…). Les notes viennent de l'App Store français au 19/11/2026, et chaque app est décrite d'après sa propre fiche. À refaire tous les 3 mois (`APPS` et `RELEVE` dans `contenu.py`).
- **L'article `jeux-a-boire-sans-materiel`** vise la recherche « jeu à boire sans matériel », mais donne chaque jeu en version points ou gages, avec un paragraphe sur la modération. Si tu préfères ne pas viser ce mot du tout, on retire l'article du calendrier.
- **La Tournée** est décrite honnêtement : le perdant prend une gorgée de ce qu'il veut, avec ou sans alcool.
- **Les prix** : aucun prix n'est écrit sur le site, seulement ce qui est gratuit et ce qui s'essaie une fois.
- **« Fait par trois amis », « testé en vraie soirée »** : à confirmer que ça te va.
- Le site dit **« pas encore de note sur l'App Store »**. À retirer dès que les premières notes arrivent.

## Suites possibles

- La page d'invitation du serveur (`/j/CODE`) parle encore de « bêta sur TestFlight » : à corriger au prochain déploiement du serveur.
- Les pages `/confidentialite` et `/support` restent sur le serveur Cloudflare ; le site y renvoie.
- Version anglaise du site : seulement si l'app sort en anglais.
- Après 3 à 4 semaines : regarder Search Console et réécrire les titres qui s'affichent mais ne sont pas cliqués.
