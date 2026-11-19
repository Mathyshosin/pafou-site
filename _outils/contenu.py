# Tout le texte des pages fixes du site PAFOU : les jeux, les guides (comparatifs), la FAQ.
# Liens internes : [[jeu:slug|texte]], [[guide:slug|texte]], [[slug-d-article|texte]].
# Tableaux comparatifs : {{tableau:cle1,cle2}} avec les clés de APPS.

RELEVE = "2026-11-19"  # date du relevé des fiches App Store des autres apps (notes, âge, éditeur)

# Relevé sur l'App Store français (API publique d'Apple) le 19/11/2026. « principe » résume la fiche de l'éditeur.
APPS = {
    "pafou": {"nom": "PAFOU", "editeur": "Mathys Hosin (La Plateforme)", "note": None, "avis": 0, "age": "17+", "url": "https://apps.apple.com/fr/app/id6822692855",
              "principe": "Plusieurs jeux dans une app : bluff, questions, action ou vérité, mini-jeux, mode bar, fléchettes, jeu pour un premier date. Chacun son téléphone ou un seul sur la table."},
    "picolo": {"nom": "Picolo", "editeur": "Marmelapp", "note": 4.5, "avis": 46732, "age": "17+", "url": "https://apps.apple.com/fr/app/id1001473964",
               "principe": "On inscrit les prénoms, l'app enchaîne des questions et des consignes à lire à voix haute sur un seul téléphone."},
    "toz": {"nom": "TOZ", "editeur": "AFK Studio", "note": 4.6, "avis": 15046, "age": "17+", "url": "https://apps.apple.com/fr/app/id1476978964",
            "principe": "Une collection de classiques de soirée revisités : Je n'ai jamais, Action ou Vérité, Qui pourrait, Tu préfères."},
    "juduku": {"nom": "JUDUKU", "editeur": "ATM Gaming", "note": 4.9, "avis": 10072, "age": "17+", "url": "https://apps.apple.com/fr/app/id1423726773",
               "principe": "8 secondes pour citer 3 réponses à une question. L'app accompagne le jeu de cartes du même nom."},
    "chouic": {"nom": "Action ou Vérité (Chouic)", "editeur": "Chouic", "note": 4.8, "avis": 36659, "age": "17+", "url": "https://apps.apple.com/fr/app/id898735886",
               "principe": "Action ou vérité avec une roue, en couple ou en groupe, plusieurs niveaux dont certains payants."},
    "insight": {"nom": "Insight", "editeur": "MWM", "note": 4.6, "avis": 16003, "age": "17+", "url": "https://apps.apple.com/fr/app/id6471489809",
                "principe": "Plusieurs jeux de soirée dans une app, dont un jeu de l'imposteur et des questions pour briser la glace."},
    "undercover": {"nom": "Undercover", "editeur": "Nahnu", "note": 4.7, "avis": 96160, "age": "12+", "url": "https://apps.apple.com/fr/app/id946882449",
                   "principe": "Jeu de mots à rôles cachés : tout le monde reçoit le même mot secret, sauf certains joueurs qu'il faut démasquer."},
    "vakarm": {"nom": "Vakarm", "editeur": "VYS Games", "note": 4.5, "avis": 49325, "age": "17+", "url": "https://apps.apple.com/fr/app/id1504657826",
               "principe": "Le « jeu des problèmes » : votes, duels et défis entre potes, sur un seul téléphone ou chacun le sien."},
    "cap": {"nom": "CAP", "editeur": "Supercap", "note": 4.4, "avis": 1232, "age": "17+", "url": "https://apps.apple.com/fr/app/id1526004658",
            "principe": "Des défis « cap ou pas cap » à partir des prénoms des joueurs."},
    "guessup": {"nom": "Guess Up", "editeur": "Cosmicode", "note": 4.6, "avis": 9770, "age": "9+", "url": "https://apps.apple.com/fr/app/id1160484607",
                "principe": "Le téléphone sur le front : on devine le mot grâce aux mimes et aux indices des autres."},
    "flechettes-compteur": {"nom": "Fléchettes Compteur de Scores", "editeur": "Yosyp Hameliak", "note": 4.8, "avis": 8006, "age": "4+", "url": "https://apps.apple.com/fr/app/id1511427031",
                            "principe": "Un compteur de points pour plusieurs modes de jeu, avec un comptage par la caméra annoncé sur sa fiche."},
    "dartcounter": {"nom": "DartCounter", "editeur": "DartCounter", "note": 4.8, "avis": 951, "age": "4+", "url": "https://apps.apple.com/fr/app/id999533915",
                    "principe": "Un compteur très complet pour joueurs réguliers : x01, cricket, jeux d'entraînement, parties en ligne, statistiques."},
    "craycray": {"nom": "Cray Cray", "editeur": "CRAYCRAY", "note": 4.6, "avis": 1529, "age": "12+", "url": "https://apps.apple.com/fr/app/id6475202904",
                 "principe": "Une app pour les couples déjà formés : un défi par jour et des questions où chacun répond de son côté."},
}

ACCES_GRATUIT = "Toujours gratuit"
ACCES_TRANQUILLE = "Niveau Tranquille gratuit. Les autres niveaux s'essaient une fois, puis demandent un achat."
ACCES_ESSAI = "Une partie d'essai offerte, puis un achat dans l'app."

JEUX = [
    {
        "slug": "la-pyramide", "nom": "La Pyramide", "etiquette": "Bluff et mémoire", "couleur": "bleu", "logo": "pyramide", "ecran": "pyramide", "perso": "vin",
        "titre": "La Pyramide : le jeu de bluff et de mémoire entre amis",
        "titre_seo": "La Pyramide : jeu de bluff entre amis sur iPhone | PAFOU",
        "description": "La Pyramide est le jeu de bluff et de mémoire de PAFOU : 4 cartes à retenir, 15 cartes révélées, et tes potes qui crient « Menteur ». De 2 à 8 joueurs, gratuit.",
        "accroche": "Tu bluffes. Il te grille.",
        "fiche": [("Joueurs", "2 à 8"), ("Durée", "environ 20 minutes"), ("Téléphones", "chacun le sien, ou un seul qui passe de main en main"), ("Accès", ACCES_GRATUIT)],
        "reponse": "La Pyramide est un jeu de bluff et de mémoire pour 2 à 8 joueurs, inclus gratuitement dans l'app iPhone PAFOU. Chacun mémorise 4 cartes, puis 15 cartes sont révélées une à une. À chaque carte, tu peux affirmer à un ami que tu as la même valeur, que ce soit vrai ou non. S'il crie « Menteur », tu dois le prouver de mémoire.",
        "en_bref": ["Un jeu de <strong>bluff</strong> : tu peux mentir sur tes cartes, il faut juste ne pas te faire prendre.", "Un jeu de <strong>mémoire</strong> : tes 4 cartes sont retournées, tu ne les revois plus.", "<strong>2 à 8 joueurs</strong>, une vingtaine de minutes, sans matériel.", "<strong>Toujours gratuit</strong> dans PAFOU, sur plusieurs téléphones ou un seul."],
        "corps": """
<h2>Comment se joue La Pyramide ?</h2>
<p>La Pyramide se joue en cinq temps. Tout le monde suit la même carte en même temps, chacun sur son téléphone.</p>
<ol>
<li><strong>Tu mémorises 4 cartes.</strong> Chaque joueur reçoit 4 cartes, les range comme il veut et les retient. Quand tout le monde est prêt, elles sont retournées. Plus personne ne les revoit.</li>
<li><strong>15 cartes sont révélées une à une.</strong> Elles forment une pyramide de cinq étages. Plus on monte, plus l'étage vaut cher.</li>
<li><strong>Tu affirmes, vrai ou pas.</strong> À chaque carte révélée, tu peux dire à un pote que tu as la même valeur dans ta main. Tu peux dire la vérité. Tu peux aussi bluffer.</li>
<li><strong>Il te croit, ou il crie « Menteur ».</strong> S'il te croit, tu gagnes 1 point et il perd les points de l'étage. S'il crie « Menteur », tu dois retourner la bonne carte parmi tes 4, de mémoire.</li>
<li><strong>La preuve tranche.</strong> Bonne carte : 2 points pour toi, et il perd l'étage. Mauvaise carte : 2 points pour lui, et c'est toi qui perds l'étage.</li>
</ol>
<p>Après la quinzième carte, le podium tombe, avec des titres comme « Roi ou Reine du bluff » et « Pigeon de la soirée ».</p>

<h2>Pourquoi c'est un bon jeu de bluff entre amis ?</h2>
<p>Parce que le mensonge et la mémoire se mélangent. Même quand tu dis la vérité, tu dois te souvenir de la place de ta carte. Un joueur honnête qui a mal retenu sa main perd autant qu'un menteur démasqué. Résultat : tout le monde doute de tout le monde, y compris de soi.</p>
<p>Chaque tour ne concerne que deux joueurs, mais toute la table regarde. C'est ce qui fait monter le bruit : on prend parti, on se souvient du bluff d'avant, on règle ses comptes au tour suivant.</p>

<h2>Peut-on jouer avec un seul téléphone ?</h2>
<p>Oui. En créant la partie, choisis « Un seul tél ». Le téléphone passe de main en main : chacun regarde ses cartes à son tour, à l'abri des regards. C'est pratique quand tes potes n'ont pas tous l'app, ou pas tous un iPhone.</p>
<p>À plusieurs téléphones, tu crées un salon et tu partages le code ou le QR code. La partie avance en même temps chez tout le monde.</p>

<h2>D'où vient le jeu de la pyramide ?</h2>
<p>La pyramide est un jeu de cartes de soirée très connu en France, qui se joue d'habitude avec un vrai paquet de 52 cartes. La version de PAFOU garde le cœur du jeu, le bluff et la preuve par la mémoire, et s'occupe du reste : distribution, comptage des points, tour de parole. Si tu cherches les règles avec un vrai paquet, on les détaille dans [[regles-jeu-de-la-pyramide|les règles du jeu de la pyramide]].</p>
<div class="astuce">Astuce de menteur : bluffe tôt, sur les étages qui valent peu. Tu perds peu si on te prend, et tu te construis une réputation de joueur honnête pour le sommet.</div>

<h2>Et après la Pyramide ?</h2>
<p>Les points s'additionnent sur toute la soirée quand tu changes de jeu. Tu peux enchaîner avec [[jeu:les-dossiers|Les Dossiers]] pour faire parler la table, ou comparer avec d'autres [[guide:jeu-de-bluff-entre-amis|jeux de bluff entre amis]].</p>
""",
        "faq": [
            ("La Pyramide est-elle gratuite ?", "Oui. La Pyramide fait partie des jeux toujours gratuits de PAFOU, avec les fléchettes. L'app se télécharge gratuitement sur l'App Store."),
            ("À combien peut-on jouer à La Pyramide ?", "De 2 à 8 joueurs. Le jeu est plus drôle à partir de 4, quand on peut choisir sa cible."),
            ("Faut-il un jeu de cartes ?", "Non. Les cartes sont dans l'app : la distribution, la pyramide et les points sont gérés par le téléphone."),
            ("Est-ce un jeu à boire ?", "Non. La Pyramide de PAFOU se joue aux points. Une option « verre », facultative et réglée par chaque joueur, existe avec ou sans alcool, mais le jeu fonctionne entièrement sans."),
        ],
    },
    {
        "slug": "les-dossiers", "nom": "Les Dossiers", "etiquette": "Questions entre potes", "couleur": "jaune", "logo": "dossiers", "ecran": "dossiers", "perso": "mojito",
        "titre": "Les Dossiers : le jeu de questions qui cite tes potes par leur prénom",
        "titre_seo": "Les Dossiers : jeu de questions entre potes | PAFOU",
        "description": "Les Dossiers, c'est le jeu de questions de PAFOU : tu tires une carte, le hasard désigne à qui tu la poses, et la table parie. 2 à 8 joueurs, trois niveaux.",
        "accroche": "Ça reste entre nous.",
        "fiche": [("Joueurs", "2 à 8"), ("Durée", "environ 15 minutes"), ("Téléphones", "chacun le sien"), ("Niveaux", "Tranquille, Piquant, Spicy"), ("Accès", ACCES_TRANQUILLE)],
        "reponse": "Les Dossiers est le jeu de questions entre potes de l'app iPhone PAFOU, pour 2 à 8 joueurs. À ton tour, tu tires une question que toi seul vois, et le hasard désigne à qui tu la poses. Les cartes citent les joueurs par leur prénom. Pendant ce temps, les autres parient : la carte sera-t-elle jouée ou esquivée ?",
        "en_bref": ["Des questions qui <strong>citent les prénoms</strong> des gens à table.", "Le hasard choisit la cible : <strong>personne n'est épargné</strong>, personne n'est acharné.", "Les spectateurs <strong>parient</strong> sur chaque carte, donc tout le monde joue tout le temps.", "<strong>Trois niveaux</strong> à choisir selon l'ambiance ; le niveau Tranquille est gratuit."],
        "corps": """
<h2>Comment se joue Les Dossiers ?</h2>
<p>À ton tour, tu tires une carte. Tu es le seul à la voir. Le hasard désigne ensuite à qui tu la poses, et la question s'affiche en grand sur tous les téléphones.</p>
<p>La personne visée répond ou réalise la carte à voix haute. C'est toi, le juge de la carte, qui tranches sur ton téléphone : « Carré » si elle a joué le jeu, « PAFOU » si elle a esquivé. Elle peut toujours passer, sans se justifier.</p>
<p>Les cartes ont plusieurs formats, écrits pour être compris en une lecture :</p>
<ul>
<li><strong>Balance</strong> : « Qui ici écrirait à son ex ce soir ? »</li>
<li><strong>Aveu</strong> : « Sur quel truc t'as menti à ce groupe sans jamais te faire griller ? »</li>
<li><strong>Pièce à conviction</strong> : « Montre ton dernier screen. Explique pourquoi tu l'as gardé. »</li>
<li><strong>Classement</strong> : « Qui ici ferait le pire coloc, du pire au meilleur ? »</li>
<li><strong>Jury</strong> : « Ta plus grosse flemme de l'année. La table décide si c'est pardonnable. »</li>
</ul>

<h2>Que font les autres pendant qu'une carte se joue ?</h2>
<p>Ils parient. Chaque spectateur choisit « Carré » (la carte sera jouée) ou « PAFOU » (elle sera esquivée). Un bon pronostic rapporte 1 point. Une carte jouée rapporte 2 points à celui qui l'assume.</p>
<p>À la fin, tout le monde vote pour la meilleure réponse de la partie : c'est la palme d'or, qui vaut 3 points.</p>

<h2>Quels sont les trois niveaux ?</h2>
<p>Tu choisis l'intensité avant de commencer, et chacun la valide.</p>
<table>
<thead><tr><th>Niveau</th><th>Pour qui</th><th>Accès</th></tr></thead>
<tbody>
<tr><td>Tranquille</td><td>Briser la glace, jouer avec des gens qu'on connaît peu</td><td>Gratuit</td></tr>
<tr><td>Piquant</td><td>Les anecdotes gênantes entre vrais potes</td><td>Un essai, puis achat</td></tr>
<tr><td>Spicy</td><td>Réservé aux adultes qui se connaissent bien</td><td>Un essai, puis achat</td></tr>
</tbody>
</table>

<h2>Est-ce que l'app garde nos réponses ?</h2>
<p>Non. Tout se dit à voix haute, autour de la table. PAFOU n'enregistre jamais les réponses, ne demande aucune photo et aucun contact. Ce qui se dit pendant Les Dossiers reste entre les gens présents.</p>

<h2>Avec quoi enchaîner ?</h2>
<p>Si la table veut plus d'action, passe à [[jeu:cap-d-assumer|Cap d'assumer ?]], la version action ou vérité. Si vous êtes au bar avec un seul téléphone, le [[jeu:mode-bar|Mode bar]] reprend le même esprit. Et pour t'échauffer, tu trouveras des idées dans nos [[questions-qui-de-nous|questions « Qui de nous »]].</p>
""",
        "faq": [
            ("Les Dossiers, c'est gratuit ?", "Le niveau Tranquille est toujours gratuit. Les niveaux Piquant et Spicy s'essaient une fois, puis demandent un achat dans l'app."),
            ("Peut-on refuser de répondre ?", "Oui, toujours. Chaque joueur peut passer une carte sans donner de raison. Il ne marque simplement pas les points de la carte."),
            ("Les questions sont-elles toujours les mêmes ?", "Non. Une carte déjà sortie pendant la soirée ne revient pas, et l'app compte plus de 400 cartes tous jeux confondus."),
        ],
    },
    {
        "slug": "cap-d-assumer", "nom": "Cap d'assumer ?", "etiquette": "Action ou vérité", "couleur": "corail", "logo": "cap", "ecran": "action", "perso": "canette",
        "titre": "Cap d'assumer ? L'action ou vérité version soirée",
        "titre_seo": "Cap d'assumer ? L'app action ou vérité entre amis | PAFOU",
        "description": "Cap d'assumer ? est le jeu action ou vérité de PAFOU : tu désignes quelqu'un, il choisit, la carte s'affiche chez tout le monde. 2 à 8 joueurs, trois niveaux.",
        "accroche": "Tu racontes. Ou tu oses.",
        "fiche": [("Joueurs", "2 à 8"), ("Durée", "environ 15 minutes"), ("Téléphones", "chacun le sien"), ("Niveaux", "Tranquille, Piquant, Spicy"), ("Accès", ACCES_TRANQUILLE)],
        "reponse": "Cap d'assumer ? est le jeu action ou vérité de l'app iPhone PAFOU, pour 2 à 8 joueurs. À ton tour, tu désignes quelqu'un. Cette personne choisit Action ou Vérité, la carte apparaît sur tous les téléphones et elle joue à voix haute. Les autres parient sur le résultat, et le niveau Tranquille est gratuit.",
        "en_bref": ["Le classique <strong>action ou vérité</strong>, avec des cartes écrites pour une soirée entre adultes.", "La carte s'affiche <strong>chez tout le monde</strong> : pas besoin de lire par-dessus une épaule.", "Les autres <strong>parient</strong> : jouée ou esquivée ?", "On peut <strong>toujours passer</strong>, sans se justifier."],
        "corps": """
<h2>Comment se joue Cap d'assumer ?</h2>
<p>À ton tour, tu désignes un joueur. Il choisit entre deux boutons : Vérité (« Tu racontes ») ou Action (« Tu oses »). La carte tirée s'affiche sur tous les téléphones, et il la joue à voix haute.</p>
<p>Celui qui a désigné devient le juge de la carte. Il valide sur son téléphone : « Carré » si c'est assumé, « PAFOU » si c'est esquivé. Une carte assumée rapporte 2 points.</p>
<p>Quelques vérités du jeu, pour le ton :</p>
<ul>
<li>« Quelle excuse bidon as-tu déjà servie à quelqu'un de cette table ? »</li>
<li>« Qui ici tu adores, mais avec qui tu ne pourrais jamais vivre ? »</li>
<li>« Quelle anecdote racontes-tu en arrangeant beaucoup trop la vérité ? »</li>
</ul>

<h2>Qu'est-ce qui change par rapport à un action ou vérité classique ?</h2>
<p>Trois choses. D'abord, personne ne doit inventer les questions : les cartes sont écrites d'avance, et une carte sortie ne revient pas dans la soirée. Ensuite, toute la table joue en continu grâce aux paris. Enfin, certains défis durent plusieurs tours : ils restent affichés en haut de tous les écrans, et l'app prévient quand ils sont finis.</p>
<p>Si tu veux jouer sans app, avec tes propres idées, pioche dans notre liste de [[questions-action-ou-verite|questions action ou vérité]].</p>

<h2>Quel niveau choisir ?</h2>
<p>Tranquille pour démarrer ou pour un groupe mélangé : c'est le niveau gratuit. Piquant pour les anecdotes gênantes entre vrais potes. Spicy est réservé aux adultes qui se connaissent bien. Chacun valide le niveau avant le départ, donc personne ne se retrouve embarqué sans l'avoir choisi.</p>
<div class="astuce">Commence toujours un cran en dessous de ce que la table réclame. Monter de niveau en cours de soirée fait plaisir à tout le monde. Redescendre, beaucoup moins.</div>

<h2>Peut-on y jouer à deux ?</h2>
<p>Oui, le jeu fonctionne dès 2 joueurs. Pour un premier rendez-vous, [[jeu:tete-a-tete|Tête-à-tête]] est plus adapté : il est pensé pour deux personnes qui se connaissent à peine.</p>

<h2>Quelle app action ou vérité choisir ?</h2>
<p>Ça dépend de ce que tu cherches : un seul téléphone ou plusieurs, en couple ou en groupe. On compare les options dans notre guide des [[guide:application-action-ou-verite|applications action ou vérité]].</p>
""",
        "faq": [
            ("Cap d'assumer ? est-il gratuit ?", "Le niveau Tranquille est toujours gratuit. Les niveaux Piquant et Spicy s'essaient une fois, puis demandent un achat dans l'app."),
            ("Combien de joueurs faut-il ?", "De 2 à 8 joueurs, chacun sur son iPhone. Le jeu est le plus vivant entre 4 et 6."),
            ("Les actions demandent-elles du matériel ?", "Non. Les actions se font avec ce qu'il y a autour de la table et un téléphone. Aucun contact physique n'est imposé."),
        ],
    },
    {
        "slug": "la-tournee", "nom": "La Tournée", "etiquette": "Mini-jeux", "couleur": "menthe", "logo": None, "ecran": "tournee", "perso": "gobelet",
        "titre": "La Tournée : dix mini-jeux de soirée, chacun sur son téléphone",
        "titre_seo": "La Tournée : mini-jeux de soirée entre amis | PAFOU",
        "description": "La Tournée enchaîne douze manches de mini-jeux : sondages, votes secrets, intrus, réflexes, chrono. De 3 à 8 joueurs, chacun sur son iPhone, en 15 minutes.",
        "accroche": "Votes, réflexes, bluff : qui tient le mieux ?",
        "fiche": [("Joueurs", "3 à 8"), ("Durée", "environ 15 minutes"), ("Téléphones", "chacun le sien"), ("Accès", ACCES_ESSAI)],
        "reponse": "La Tournée est le mode mini-jeux de l'app iPhone PAFOU, pour 3 à 8 joueurs qui ont chacun leur téléphone. Une partie enchaîne douze manches rapides tirées parmi dix mini-jeux : sondage, vote secret, minorité, intrus, réflexe, chrono, bombe. Chaque manche désigne un perdant, qui prend un gage. Comptez une quinzaine de minutes.",
        "en_bref": ["<strong>Douze manches</strong> rapides, dix mini-jeux différents.", "Tout se joue <strong>en secret</strong>, puis l'écran révèle le résultat à tout le monde.", "<strong>3 à 8 joueurs</strong>, chacun sur son téléphone.", "Le perdant prend un gage simple, <strong>avec ou sans alcool</strong>."],
        "corps": """
<h2>Quels sont les mini-jeux de La Tournée ?</h2>
<p>Il y en a dix, mélangés à chaque partie. Aucun ne dure plus d'une minute ou deux.</p>
<table>
<thead><tr><th>Mini-jeu</th><th>Le principe</th></tr></thead>
<tbody>
<tr><td>Sondage</td><td>Une question bête sur un joueur. Tout le monde vote, et il doit deviner la réponse préférée de la table.</td></tr>
<tr><td>Dossier</td><td>Un joueur joue une carte à voix haute. Les autres votent « Assumé » ou « Esquivé ».</td></tr>
<tr><td>Vote</td><td>« Qui ici… ? » Le plus désigné perd la manche.</td></tr>
<tr><td>Minorité</td><td>Deux choix. Ceux qui sont les moins nombreux perdent.</td></tr>
<tr><td>Doublon</td><td>Chacun choisit un numéro. Ceux qui ont pris le même perdent.</td></tr>
<tr><td>L'Intrus</td><td>Tout le monde a le même mot, sauf un joueur qui ne le sait pas. Un mot chacun, puis on vote.</td></tr>
<tr><td>La Bombe</td><td>Trois tapes pour s'en débarrasser avant qu'elle explose.</td></tr>
<tr><td>Le Bourrin</td><td>Le plus de tapes possible en 5 secondes.</td></tr>
<tr><td>Le Chrono</td><td>Arrêter son chrono le plus près possible de 5 secondes, sans le voir.</td></tr>
<tr><td>Le Réflexe</td><td>Les écrans passent au jaune en même temps. Le dernier à taper perd.</td></tr>
</tbody>
</table>

<h2>Comment gagne-t-on ?</h2>
<p>Il n'y a pas de points. Chaque manche désigne un ou plusieurs perdants, et le gagnant de la partie est celui qui a perdu le moins de manches. Après chaque manche, ton écran te dit clairement si tu as perdu ou pas.</p>
<p>Les temps des jeux de réflexe sont mesurés sur chaque téléphone. Un réseau lent ne pénalise personne.</p>

<h2>Quel est le gage du perdant ?</h2>
<p>Le perdant d'une manche prend une gorgée de ce qu'il veut : eau, soda, ce qu'il a devant lui. La Tournée se joue avec ou sans alcool, et rien n'oblige à boire de l'alcool pour y jouer. L'app compte les gorgées de chacun et rappelle de boire de l'eau. Ce mode est réservé aux adultes.</p>
<p>Si tu cherches des idées de gages qui ne passent pas par un verre, on en a rassemblé dans nos [[idees-de-gages-soiree|idées de gages de soirée]].</p>

<h2>Pourquoi chacun son téléphone ?</h2>
<p>Parce que tout repose sur le secret et la synchronisation. Tu votes sans que ton voisin voie ton écran, et les réflexes se jouent au même instant chez tout le monde. Si vous n'avez qu'un téléphone pour la table, regarde plutôt le [[jeu:mode-bar|Mode bar]].</p>

<h2>Pour quelle soirée ?</h2>
<p>La Tournée est le mode le plus rythmé de PAFOU : idéal quand la table commence à retomber, ou pour finir une soirée commencée avec [[jeu:la-pyramide|La Pyramide]]. Le jeu de l'intrus te plaît ? On explique ses règles complètes dans [[jeu-de-l-intrus-regles|le jeu de l'intrus]].</p>
""",
        "faq": [
            ("La Tournée est-elle un jeu à boire ?", "C'est un jeu de mini-jeux où le perdant d'une manche prend une gorgée de la boisson de son choix, avec ou sans alcool. On peut y jouer entièrement sans alcool."),
            ("La Tournée est-elle gratuite ?", "Tu peux l'essayer une fois gratuitement. Ensuite, elle demande un achat dans l'app. Dans un salon, il suffit qu'un joueur de la table l'ait débloquée."),
            ("Faut-il une connexion internet ?", "Oui. La Tournée synchronise les téléphones de la table, il faut donc du réseau ou du Wi-Fi."),
        ],
    },
    {
        "slug": "mode-bar", "nom": "Le Mode bar", "etiquette": "Un seul téléphone", "couleur": "corail", "logo": "bar", "ecran": "bar", "perso": "cocktail",
        "titre": "Le Mode bar : un seul téléphone sur la table, et tout le monde parle",
        "titre_seo": "Mode bar : jeu à faire au bar sur un seul téléphone | PAFOU",
        "description": "Le Mode bar de PAFOU se joue avec un seul téléphone posé sur la table : procès, débats débiles, mot interdit, mission secrète. À partir de 3 joueurs.",
        "accroche": "Vous parlez, vous riez.",
        "fiche": [("Joueurs", "3 et plus"), ("Durée", "13 cartes, environ 20 minutes"), ("Téléphones", "un seul, posé sur la table"), ("Niveaux", "Tranquille, Piquant"), ("Accès", ACCES_ESSAI)],
        "reponse": "Le Mode bar est un jeu de l'app iPhone PAFOU qui se joue avec un seul téléphone posé sur la table, à partir de 3 joueurs. Une partie mélange 13 cartes de six petits jeux : Qui de nous, Le Procès, Le Débat débile, Le Mot interdit, Autour du bar et La Mission secrète. Il n'y a pas de points : le téléphone arbitre, la table discute.",
        "en_bref": ["<strong>Un seul téléphone</strong> pour toute la table : personne n'a le nez sur son écran.", "<strong>Six petits jeux</strong> mélangés en 13 cartes.", "<strong>Pas de points</strong>, pas de perdant : le but est de faire parler.", "Fonctionne <strong>sans réseau</strong>, pratique en sous-sol."],
        "corps": """
<h2>Comment se joue le Mode bar ?</h2>
<p>Tu entres les prénoms, tu choisis un niveau et tu poses le téléphone au milieu de la table. Les cartes s'enchaînent, et chacune lance un petit jeu différent.</p>
<table>
<thead><tr><th>Petit jeu</th><th>Ce qui se passe</th></tr></thead>
<tbody>
<tr><td>Qui de nous</td><td>Une question sur le groupe. Au signal, tout le monde désigne quelqu'un.</td></tr>
<tr><td>Le Procès</td><td>Un joueur est accusé (« On accuse Jules de ne jamais payer sa part sans qu'on le demande »). Il se défend, un autre plaide, la table vote à main levée.</td></tr>
<tr><td>Le Débat débile</td><td>Deux camps, un sujet absurde, un chrono.</td></tr>
<tr><td>Le Mot interdit</td><td>Faire deviner un mot sans prononcer les mots interdits.</td></tr>
<tr><td>Autour du bar</td><td>Des petits paris sur ce qui se passe dans la salle.</td></tr>
<tr><td>La Mission secrète</td><td>Distribuée au début, à accomplir sans se faire remarquer, révélée à la fin.</td></tr>
</tbody>
</table>

<h2>Pourquoi un seul téléphone ?</h2>
<p>Parce qu'au bar, une table où chacun regarde son écran, c'est raté. Le Mode bar a été pensé à l'envers des autres jeux de PAFOU : le téléphone ne fait qu'annoncer la carte et tenir le chrono. Tout le reste se passe entre les gens.</p>
<p>Autre avantage : un seul iPhone suffit. Tes amis n'ont rien à installer.</p>

<h2>Est-ce que ça marche ailleurs qu'au bar ?</h2>
<p>Oui. Au restaurant, en terrasse, dans un train, chez toi autour d'une table basse. Le jeu ne demande ni réseau ni matériel. Le nom vient simplement de l'endroit où l'idée est née.</p>

<h2>Quel niveau choisir ?</h2>
<p>Tranquille tourne autour des petites hontes du quotidien, pour tout le monde. Piquant va chercher les crushs, les ex et les petits secrets. Aucun des deux niveaux ne parle d'alcool, et aucun ne demande de boire.</p>
<div class="astuce">La Mission secrète est la meilleure carte du jeu si tout le monde joue le jeu jusqu'au bout. Ne révèle rien avant la fin, même si on te soupçonne.</div>

<h2>Et s'il y a une cible de fléchettes ?</h2>
<p>PAFOU compte aussi les points : regarde le [[jeu:flechettes|compteur de fléchettes]]. Pour d'autres idées quand vous êtes de sortie, on a une liste de [[jeux-de-bar-entre-amis|jeux à faire au bar entre amis]].</p>
""",
        "faq": [
            ("Combien faut-il de téléphones pour le Mode bar ?", "Un seul. Il reste posé sur la table et sert d'arbitre. Les autres joueurs n'ont rien à installer."),
            ("Le Mode bar est-il gratuit ?", "Tu peux faire une partie d'essai gratuite. Ensuite, le mode demande un achat dans l'app."),
            ("Faut-il du réseau ?", "Non. Le Mode bar fonctionne sans connexion, ce qui est pratique dans une salle en sous-sol."),
        ],
    },
    {
        "slug": "flechettes", "nom": "Les fléchettes", "etiquette": "Compteur de score", "couleur": "nuit", "logo": "fleches", "ecran": "fleches", "perso": "biere",
        "titre": "Compteur de fléchettes : 301, 501 et Cricket sur iPhone",
        "titre_seo": "Compteur de fléchettes gratuit : 301, 501, Cricket | PAFOU",
        "description": "Le compteur de fléchettes de PAFOU compte les points en 301, 501 et Cricket, de 2 à 8 joueurs. Tu touches la cible à l'écran, l'app calcule. Gratuit, sans réseau.",
        "accroche": "La machine ne compte pas ? L'app compte.",
        "fiche": [("Joueurs", "2 à 8"), ("Jeux", "301, 501, Cricket"), ("Téléphones", "un seul"), ("Réseau", "aucun besoin"), ("Accès", ACCES_GRATUIT)],
        "reponse": "PAFOU contient un compteur de fléchettes gratuit sur iPhone, pour 2 à 8 joueurs. Il gère le 301, le 501 et le Cricket, avec l'option « finir sur un double ». Tu touches sur l'écran la zone de la cible atteinte par chaque fléchette, et l'app fait le calcul. Il fonctionne sans réseau et sauvegarde la partie à chaque lancer.",
        "en_bref": ["Trois jeux : <strong>301, 501 et Cricket</strong>.", "Tu touches <strong>la cible à l'écran</strong>, avec doubles et triples : pas de calcul de tête.", "<strong>Annulation</strong> d'une fléchette en cas d'erreur, partie <strong>sauvegardée</strong> à chaque lancer.", "<strong>Toujours gratuit</strong>, sans compte et sans réseau."],
        "corps": """
<h2>À quoi sert un compteur de fléchettes ?</h2>
<p>À jouer quand personne ne veut compter. C'est le cas sur une cible classique, en liège ou en sisal, qui ne compte rien du tout. C'est aussi le cas au bar quand la cible électronique est en panne ou réclame des pièces que personne n'a.</p>
<p>Avec le compteur de PAFOU, un joueur tient le téléphone. Après chaque fléchette, il touche la zone atteinte sur la cible dessinée à l'écran. Le score restant s'affiche pour tout le monde.</p>

<h2>Quels jeux de fléchettes sont inclus ?</h2>
<table>
<thead><tr><th>Jeu</th><th>Le but</th><th>Pour qui</th></tr></thead>
<tbody>
<tr><td>301</td><td>Partir de 301 et arriver exactement à zéro</td><td>Une partie courte, parfaite pour débuter</td></tr>
<tr><td>501</td><td>Partir de 501 et arriver exactement à zéro</td><td>Le format classique, plus long</td></tr>
<tr><td>Cricket</td><td>Fermer les numéros 15 à 20 et le centre, et marquer sur ceux que les autres n'ont pas fermés</td><td>Ceux qui veulent de la tactique</td></tr>
</tbody>
</table>
<p>L'option « finir sur un double » s'active d'un bouton pour le 301 et le 501. Si tu découvres ces jeux, on détaille [[regles-flechettes-301-501|les règles du 301 et du 501]] et [[regles-cricket-flechettes|les règles du Cricket]].</p>

<h2>Comment entre-t-on les points ?</h2>
<p>Tu touches la cible à l'écran, là où la fléchette s'est plantée. Les zones des doubles et des triples sont élargies pour être faciles à viser avec le doigt. Un bouton « À côté » sert pour les fléchettes ratées.</p>
<p>Une erreur ? Tu annules la dernière fléchette. Le téléphone s'éteint ou tu changes d'app ? La partie est sauvegardée à chaque lancer et tu la reprends où tu l'as laissée.</p>

<h2>Pourquoi un compteur dans un jeu de soirée ?</h2>
<p>Parce que les fléchettes font partie des soirées au bar, et qu'une app de plus à installer pour ça, c'est une de trop. Le compteur de PAFOU reste volontairement simple : pas de compte, pas de publicité, pas de statistiques de carrière.</p>
<p>Si tu joues en club ou que tu veux suivre ta moyenne sur des mois, une app spécialisée te servira mieux. On les compare honnêtement dans notre guide des [[guide:application-compteur-flechettes|applications de compteur de fléchettes]].</p>

<h2>Et entre deux parties ?</h2>
<p>Pose le téléphone sur la table et lance le [[jeu:mode-bar|Mode bar]] : il se joue aussi avec un seul iPhone.</p>
""",
        "faq": [
            ("Le compteur de fléchettes est-il gratuit ?", "Oui. Les fléchettes font partie des jeux toujours gratuits de PAFOU, sans compte et sans publicité."),
            ("Combien de joueurs peut-on inscrire ?", "De 2 à 8 joueurs sur le même téléphone."),
            ("Le compteur fonctionne-t-il sans internet ?", "Oui. Il n'a besoin d'aucune connexion, et la partie est sauvegardée sur le téléphone à chaque lancer."),
            ("Peut-on finir sur un double ?", "Oui. L'option « finir sur un double » se coche avant de lancer une partie de 301 ou de 501."),
        ],
    },
    {
        "slug": "tete-a-tete", "nom": "Tête-à-tête", "etiquette": "Premier date", "couleur": "menthe", "logo": "decouvre", "ecran": "tete", "perso": "whisky",
        "titre": "Tête-à-tête : le jeu à deux pour un premier date",
        "titre_seo": "Tête-à-tête : jeu à deux pour un premier date | PAFOU",
        "description": "Tête-à-tête est le jeu de PAFOU pour un premier date : un seul téléphone, trois niveaux, un vote secret pour passer au suivant. Et le perdant paie l'addition.",
        "accroche": "Le perdant paie l'addition.",
        "fiche": [("Joueurs", "2"), ("Téléphones", "un seul"), ("Niveaux", "Léger, Vrai, Ça chauffe"), ("Accès", ACCES_ESSAI)],
        "reponse": "Tête-à-tête est un jeu à deux de l'app iPhone PAFOU, conçu pour un premier date. Il se joue sur un seul téléphone posé entre vous. Les questions montent en trois niveaux, Léger, Vrai puis Ça chauffe, et on ne passe au suivant que si les deux le veulent, par un vote secret. À la fin, le perdant paie l'addition.",
        "en_bref": ["Pour <strong>deux personnes qui se connaissent à peine</strong>.", "<strong>Un seul téléphone</strong>, posé sur la table.", "Un <strong>vote secret</strong> pour monter d'un niveau : personne n'est mis mal à l'aise.", "Rien de sexuel, <strong>rien sur les ex</strong>."],
        "corps": """
<h2>Comment se joue Tête-à-tête ?</h2>
<p>Vous entrez vos deux prénoms et vous posez le téléphone entre vous. Le jeu alterne plusieurs types de cartes : des questions auxquelles chacun répond à son tour, et des cartes « Devine-moi » où l'un lit une question sur lui-même, l'autre devine, puis le premier révèle la vraie réponse.</p>
<p>Exemples de cartes « Devine-moi » du premier niveau : « Je suis en retard de combien, en général ? », « Je mets combien de réveils le matin ? », « Dans un groupe de potes, je suis lequel ? ».</p>
<p>Celui qui devine juste marque. À la fin, l'app affiche un bilan, et le perdant paie l'addition. Ou le prochain café, à vous de voir.</p>

<h2>Quels sont les trois niveaux ?</h2>
<table>
<thead><tr><th>Niveau</th><th>L'ambiance</th></tr></thead>
<tbody>
<tr><td>Léger</td><td>On se jauge, on rigole.</td></tr>
<tr><td>Vrai</td><td>On se livre un peu.</td></tr>
<tr><td>Ça chauffe</td><td>On flirte, sans forcer.</td></tr>
</tbody>
</table>
<p>Même au troisième niveau, les questions restent du flirt : « Je fais le premier pas, ou j'attends ? ». Le jeu ne contient rien de sexuel et ne pose aucune question sur le nombre d'ex.</p>

<h2>Comment fonctionne le vote secret ?</h2>
<p>À la fin d'un niveau, chacun répond à son tour, en cachant l'écran : « On passe au niveau suivant ? ». Le jeu ne monte que si les deux disent oui.</p>
<p>Et pour qu'un refus ne se devine pas, l'app garde parfois le niveau même quand les deux ont dit oui. Si le jeu ne monte pas, tu ne peux donc pas savoir si c'est l'autre qui a refusé ou si c'est le hasard. Personne ne perd la face.</p>

<h2>Pourquoi jouer à un jeu pendant un premier date ?</h2>
<p>Parce que le plus dur dans un premier rendez-vous, c'est de sortir des questions d'entretien : « Tu fais quoi dans la vie ? », « Tu viens d'où ? ». Un jeu donne une excuse pour poser des questions qu'on n'oserait pas poser, et pour y répondre sans que ça ressemble à une confession.</p>
<p>Un téléphone posé sur la table, écran visible par les deux, n'a pas le même effet qu'un téléphone dans la main. C'est le jeu qui parle, pas tes notifications.</p>
<div class="astuce">Propose-le au bon moment : une fois les verres ou les plats commandés, quand la première gêne est passée. Pas en t'asseyant.</div>

<h2>Et sans app ?</h2>
<p>Tu peux très bien jouer de tête. On a rassemblé des [[questions-premier-date|questions pour un premier rendez-vous]] et des [[jeux-pour-un-premier-date|petits jeux à faire à deux]]. Notre guide [[guide:jeu-pour-premier-date|quel jeu pour un premier date]] compare les options.</p>
""",
        "faq": [
            ("Tête-à-tête est-il fait pour les couples installés ?", "Il est pensé pour deux personnes qui se découvrent. Un couple peut y jouer, mais beaucoup de questions supposent qu'on ne connaît pas encore la réponse."),
            ("Tête-à-tête est-il gratuit ?", "Tu peux faire une partie d'essai gratuite. Ensuite, le mode demande un achat dans l'app."),
            ("Les questions sont-elles gênantes ?", "Non. Le jeu ne contient rien de sexuel et rien sur les ex, et chaque niveau ne s'ouvre que si les deux votent pour, en secret."),
        ],
    },
    {
        "slug": "on-se-decouvre", "nom": "On se découvre", "etiquette": "Faire connaissance", "couleur": "menthe", "logo": "decouvre", "ecran": "decouverte", "perso": "cafe",
        "titre": "On se découvre : le jeu pour briser la glace dans un groupe",
        "titre_seo": "On se découvre : jeu pour briser la glace en groupe | PAFOU",
        "description": "On se découvre est le jeu de PAFOU pour un groupe qui ne se connaît pas : première impression, face à face, puis défis en équipes. 3 à 12 joueurs, un seul téléphone.",
        "accroche": "Faites connaissance, puis défiez-vous en équipe.",
        "fiche": [("Joueurs", "3 à 12"), ("Téléphones", "un seul"), ("Niveaux", "Pour briser la glace, Pour vraiment se connaître"), ("Accès", ACCES_ESSAI)],
        "reponse": "On se découvre est un jeu de l'app iPhone PAFOU pour briser la glace dans un groupe de 3 à 12 personnes qui ne se connaissent pas ou peu. Il se joue sur un seul téléphone. La partie commence par des questions pour faire connaissance, puis, dès 4 joueurs, forme deux équipes mélangées pour des défis : mime, mot interdit, même réponse.",
        "en_bref": ["Pour une table où <strong>tout le monde ne se connaît pas</strong> : crémaillère, collègues, amis d'amis.", "<strong>Un seul téléphone</strong> : personne n'a rien à installer.", "D'abord <strong>on se présente</strong>, ensuite <strong>on joue en équipes</strong>.", "<strong>Sans alcool</strong> et sans question gênante."],
        "corps": """
<h2>Comment se déroule une partie ?</h2>
<p>En deux temps. Le premier sert à se connaître, le second à jouer ensemble.</p>
<p><strong>Premier temps : faire connaissance.</strong></p>
<ul>
<li><strong>Première impression</strong> : « Quel métier ferait Hugo dans un film ? » Tout le monde donne son avis à voix haute, puis Hugo dit la vérité.</li>
<li><strong>Face à face</strong> : deux joueurs répondent à la même question, chacun leur tour.</li>
<li><strong>Deux vérités, un mensonge</strong> : un joueur affirme trois choses sur lui, la table cherche l'intrus.</li>
<li><strong>Le Fait mystère</strong> : un fait sur quelqu'un de la table. À qui appartient-il ?</li>
</ul>
<p><strong>Second temps : les équipes.</strong> À partir de 4 joueurs, l'app forme deux équipes en mélangeant les gens. Elles s'affrontent sur quatre épreuves : Mime, Même réponse (répondre la même chose sans se concerter), Mot interdit et Ligne muette (se ranger dans un ordre donné sans parler). Un score départage les équipes.</p>

<h2>Pour quelles occasions ?</h2>
<p>Toutes celles où la moitié de la table se dit « je ne connais personne » : une crémaillère, un anniversaire qui mélange les groupes d'amis, une soirée entre collègues, un week-end d'intégration, un repas avec la belle-famille.</p>
<p>Le jeu repart de zéro à chaque partie. Il ne suppose pas que les joueurs ont une histoire commune, contrairement aux [[jeu:les-dossiers|Dossiers]], qui s'adressent à des potes.</p>

<h2>Pourquoi un jeu aide-t-il à briser la glace ?</h2>
<p>Parce qu'il donne à chacun un tour de parole et un sujet. Dans une soirée où les gens ne se connaissent pas, les plus à l'aise parlent et les autres écoutent. Ici, c'est le téléphone qui désigne, donc tout le monde a sa minute.</p>
<p>Le passage en équipes fait le reste : rien ne rapproche plus vite deux inconnus que de devoir gagner ensemble un mime raté.</p>

<h2>Quel niveau choisir ?</h2>
<p>« Pour briser la glace » est léger et drôle, parfait pour commencer. « Pour vraiment se connaître » va un peu plus loin dans le personnel, sans jamais devenir gênant. Dans le doute, prends le premier.</p>

<h2>D'autres idées pour faire connaissance ?</h2>
<p>On a rassemblé des [[jeux-pour-briser-la-glace|jeux pour briser la glace entre adultes]] qui se jouent sans rien, et les règles complètes de [[deux-verites-un-mensonge|Deux vérités, un mensonge]]. Si vous n'êtes que deux, regarde [[jeu:tete-a-tete|Tête-à-tête]].</p>
""",
        "faq": [
            ("Peut-on jouer à On se découvre entre collègues ?", "Oui. Le jeu ne contient ni alcool ni question intime, et il a été pensé pour des gens qui se connaissent peu."),
            ("Combien de joueurs faut-il ?", "De 3 à 12 joueurs sur un seul téléphone. Les épreuves en équipes commencent à partir de 4 joueurs."),
            ("On se découvre est-il gratuit ?", "Tu peux faire une partie d'essai gratuite. Ensuite, le mode demande un achat dans l'app."),
        ],
    },
    {
        "slug": "bandes-de-potes", "nom": "Les bandes de potes", "etiquette": "Classement du mois", "couleur": "bleu", "logo": None, "ecran": "bande", "perso": "champagne",
        "titre": "Les bandes de potes : le classement du mois entre amis",
        "titre_seo": "Bandes de potes : classement entre amis | PAFOU",
        "description": "Crée ta bande dans PAFOU, invite tes potes avec un lien et suivez le classement du mois : 3 points par victoire, 1 par partie, des titres et des stats.",
        "accroche": "Qui est le patron ce mois-ci ?",
        "fiche": [("Pour qui", "un groupe d'amis qui joue régulièrement"), ("Invitation", "par lien ou par code"), ("Classement", "remis à zéro chaque mois"), ("Compte", "Se connecter avec Apple")],
        "reponse": "Les bandes de potes sont des groupes permanents dans l'app iPhone PAFOU. Tu crées ta bande, tu invites tes amis avec un lien, et chaque partie jouée ensemble compte pour le classement du mois : 3 points par victoire, 1 point par partie. Le classement repart de zéro chaque mois, avec des titres et des statistiques à partager.",
        "en_bref": ["Un <strong>classement du mois</strong> entre amis, remis à zéro le 1er.", "<strong>3 points</strong> par victoire, <strong>1 point</strong> par partie jouée.", "Invitation par <strong>lien</strong> ou par code.", "Des <strong>titres</strong> à partager en image dans le groupe."],
        "corps": """
<h2>Comment créer une bande ?</h2>
<p>Depuis ton profil dans PAFOU, tu crées une bande et tu lui donnes un nom. L'app te donne un code et un lien d'invitation à envoyer dans ton groupe de discussion. Tes amis touchent le lien et rejoignent la bande.</p>
<p>Les bandes demandent un compte, créé avec « Se connecter avec Apple ». C'est le seul endroit de l'app où le compte est nécessaire : pour jouer, il reste facultatif.</p>

<h2>Comment marche le classement ?</h2>
<p>Une partie compte pour la bande dès que deux membres connectés y jouent ensemble. Chaque partie jouée rapporte 1 point, chaque victoire 3 points. Le classement affiche le podium du mois et le détail de chacun.</p>
<p>Le premier jour du mois, tout le monde repart de zéro. Celui qui a raté trois soirées en novembre a donc toutes ses chances en décembre.</p>

<h2>À quoi servent les titres ?</h2>
<p>À chambrer. Au fil des parties, PAFOU attribue des titres selon ce qui s'est passé à table : le meilleur bluffeur, celui qui se fait le plus souvent piéger. Tu peux partager les titres du mois en image dans ta conversation de groupe.</p>

<h2>Et la modération ?</h2>
<p>Les noms de bandes sont écrits par les joueurs et passent par un filtre de mots. Chaque membre peut signaler une bande ou un membre, le masquer ou quitter la bande. Le créateur peut exclure un membre. Les signalements sont lus par l'équipe.</p>

<h2>Par quel jeu commencer avec sa bande ?</h2>
<p>[[jeu:la-pyramide|La Pyramide]] est le meilleur point de départ : elle est gratuite, se joue de 2 à 8 et désigne un vrai vainqueur. Pour organiser un rendez-vous régulier, lis nos conseils pour [[organiser-une-soiree-jeux|organiser une soirée jeux]].</p>
""",
        "faq": [
            ("Faut-il un compte pour jouer à PAFOU ?", "Non. Le compte est facultatif pour jouer. Il devient nécessaire seulement pour les bandes de potes, parce qu'il faut savoir qui a gagné quoi."),
            ("Combien de bandes peut-on rejoindre ?", "Tu peux faire partie de plusieurs bandes : une par groupe d'amis, par exemple."),
            ("Que deviennent les points à la fin du mois ?", "Le classement repart de zéro le premier jour de chaque mois. Les titres gagnés restent visibles dans la bande."),
        ],
    },
]

GUIDES = [
    {
        "slug": "meilleure-app-jeu-de-soiree", "perso": "cocktail",
        "titre": "Quelle est la meilleure app de jeu de soirée en 2026 ? Le comparatif honnête",
        "titre_seo": "Meilleure app de jeu de soirée en 2026 : le comparatif",
        "titre_court": "Meilleure app de jeu de soirée",
        "description": "Comparatif 2026 des applications de jeux de soirée sur iPhone : Picolo, TOZ, JUDUKU, Undercover, Insight, Vakarm et PAFOU. Laquelle choisir selon ta soirée.",
        "resume": "Sept apps comparées, et laquelle choisir selon ta soirée.",
        "reponse": "Il n'existe pas une meilleure app de jeu de soirée, mais une meilleure app par situation. Pour un jeu de mots à rôles cachés, Undercover est la référence. Pour des consignes à lire sur un seul téléphone, Picolo. Pour une question rapide et bruyante, JUDUKU. Pour plusieurs jeux différents dans la même app, dont un jeu de bluff, un mode bar et un jeu pour un premier date, PAFOU.",
        "en_bref": ["Choisis d'abord selon <strong>le nombre de téléphones</strong> : un seul sur la table, ou chacun le sien.", "Choisis ensuite selon <strong>le groupe</strong> : vieux potes, inconnus, deux personnes.", "Les notes ci-dessous ont été relevées sur <strong>l'App Store français le 19 novembre 2026</strong>.", "PAFOU est <strong>récent</strong> (sorti fin octobre 2026) et n'a pas encore de notes : on le dit clairement."],
        "corps": """
<h2>Quelles sont les principales apps de jeux de soirée ?</h2>
<p>Voici sept applications qu'on croise le plus souvent en cherchant « jeu de soirée » sur l'App Store français. Les notes et les classes d'âge viennent de leurs fiches publiques.</p>
{{tableau:picolo,toz,juduku,undercover,insight,vakarm,pafou}}
<p>Ce tableau dit ce que chaque app annonce sur sa fiche. On n'a pas testé chaque niveau payant de chaque app, donc on ne note pas leur contenu. La note de l'App Store reste le meilleur indicateur public : toutes ces apps sont bien notées, par beaucoup de monde.</p>

<h2>Comment choisir entre toutes ces apps ?</h2>
<p>Pose-toi trois questions, dans cet ordre.</p>
<ol>
<li><strong>Combien de téléphones ?</strong> Un seul téléphone qui tourne, c'est simple et personne n'a rien à installer. Chacun le sien permet les votes secrets et le bluff, mais tout le monde doit avoir l'app.</li>
<li><strong>Qui est autour de la table ?</strong> Des potes de dix ans supportent des questions qui piquent. Un groupe mélangé a besoin d'un jeu pour faire connaissance.</li>
<li><strong>Quel type de jeu ?</strong> Lire des cartes, voter, bluffer, deviner un mot, relever un défi : ce ne sont pas les mêmes soirées.</li>
</ol>

<h2>Quelle app pour quelle soirée ?</h2>
<table>
<thead><tr><th>Ta soirée</th><th>Ce qu'on regarderait en premier</th></tr></thead>
<tbody>
<tr><td>Un grand groupe, un seul téléphone, zéro explication</td><td>Picolo ou TOZ</td></tr>
<tr><td>Un jeu de mots avec un imposteur à démasquer</td><td>Undercover ou Insight</td></tr>
<tr><td>Une épreuve rapide entre deux plats</td><td>JUDUKU</td></tr>
<tr><td>Des votes et des dossiers entre potes</td><td>Vakarm ou PAFOU (Les Dossiers)</td></tr>
<tr><td>Un jeu de bluff avec des cartes</td><td>PAFOU (La Pyramide)</td></tr>
<tr><td>Au bar, sans réseau, avec une cible de fléchettes</td><td>PAFOU (Mode bar et compteur)</td></tr>
<tr><td>Un premier rendez-vous à deux</td><td>PAFOU (Tête-à-tête)</td></tr>
<tr><td>Une partie du groupe est sur Android</td><td>Une app disponible sur les deux systèmes : PAFOU n'existe que sur iPhone</td></tr>
</tbody>
</table>

<h2>Que propose PAFOU, et pour qui ce n'est pas fait ?</h2>
<p>PAFOU réunit plusieurs jeux dans une seule app : [[jeu:la-pyramide|La Pyramide]] (bluff et mémoire), [[jeu:les-dossiers|Les Dossiers]] (questions qui citent les prénoms), [[jeu:cap-d-assumer|Cap d'assumer ?]] (action ou vérité), [[jeu:la-tournee|La Tournée]] (mini-jeux), le [[jeu:mode-bar|Mode bar]], un [[jeu:flechettes|compteur de fléchettes]], [[jeu:tete-a-tete|Tête-à-tête]] pour un premier date et [[jeu:on-se-decouvre|On se découvre]] pour briser la glace.</p>
<p>Ses limites, pour être clair :</p>
<ul>
<li><strong>iPhone uniquement.</strong> Pour les jeux à plusieurs téléphones, tout le monde doit avoir un iPhone. Les jeux à un seul téléphone règlent le problème.</li>
<li><strong>En français uniquement.</strong></li>
<li><strong>Une app récente</strong>, sortie le 31 octobre 2026, qui n'a pas encore de notes sur l'App Store.</li>
<li><strong>Une partie du contenu est payante.</strong> La Pyramide, les fléchettes et le niveau Tranquille des Dossiers et de Cap d'assumer ? sont gratuits. Le reste s'essaie une fois.</li>
</ul>

<h2>Gratuit ou payant : à quoi s'attendre ?</h2>
<p>Toutes les apps de ce comparatif se téléchargent gratuitement, et la plupart vendent du contenu en plus, souvent par abonnement. Avant de payer, vérifie deux choses : ce qui reste jouable sans payer, et si un seul achat suffit pour toute la table.</p>
<p>Dans PAFOU, pour une partie à plusieurs téléphones, il suffit qu'un joueur de la table ait débloqué un mode pour que tout le salon y joue pendant cette partie.</p>

<h2>Et sans application ?</h2>
<p>Un jeu de soirée n'a pas besoin d'une app. On a listé des [[jeux-de-soiree-entre-potes|jeux de soirée entre potes]] à lancer sans rien, et un guide des [[guide:jeu-de-soiree-sans-materiel|jeux de soirée sans matériel]].</p>
""",
        "faq": [
            ("Quelle est l'application de jeu de soirée la mieux notée ?", "Au 19 novembre 2026 sur l'App Store français, parmi les apps de ce comparatif, JUDUKU affiche 4,9 sur 5 et Undercover 4,7 sur 5 avec plus de 96 000 notes."),
            ("Quelle app de jeu de soirée fonctionne avec un seul téléphone ?", "Picolo se joue sur un seul téléphone. Dans PAFOU, le Mode bar, On se découvre, Tête-à-tête, les fléchettes et La Pyramide en mode « Un seul tél » se jouent aussi avec un seul iPhone."),
            ("PAFOU est-il gratuit ?", "PAFOU se télécharge gratuitement. La Pyramide, les fléchettes et le niveau Tranquille des Dossiers et de Cap d'assumer ? restent gratuits. Les autres modes s'essaient une fois, puis demandent un achat."),
            ("Existe-t-il une app de jeu de soirée sans alcool ?", "Oui. Undercover et Guess Up ne reposent pas sur l'alcool. Dans PAFOU, tous les jeux se jouent sans alcool : ils fonctionnent aux points, aux votes ou aux gages."),
        ],
    },
    {
        "slug": "application-action-ou-verite", "perso": "canette",
        "titre": "Quelle application action ou vérité choisir ? Le guide pour ne pas se tromper",
        "titre_seo": "Application action ou vérité : laquelle choisir en 2026 ?",
        "titre_court": "Application action ou vérité",
        "description": "Comment choisir une application action ou vérité sur iPhone : en groupe ou en couple, un téléphone ou plusieurs, niveaux gratuits. Avec Chouic, TOZ, CAP et PAFOU.",
        "resume": "Les critères qui comptent, et quatre apps comparées.",
        "reponse": "Pour choisir une application action ou vérité, regarde trois choses : si elle se joue sur un téléphone ou plusieurs, si les niveaux sages sont gratuits, et si elle convient à ton groupe. « Action ou Vérité » de Chouic est la plus installée et propose un mode couple. PAFOU propose Cap d'assumer ?, où la carte s'affiche sur tous les téléphones et où la table parie.",
        "en_bref": ["Un action ou vérité réussi dépend surtout du <strong>niveau choisi</strong> pour le groupe.", "<strong>Un seul téléphone</strong> est plus simple ; <strong>plusieurs</strong> font participer toute la table.", "Vérifie quels <strong>niveaux sont gratuits</strong> avant de lancer la soirée.", "Notes relevées sur l'App Store français le <strong>19 novembre 2026</strong>."],
        "corps": """
<h2>Quelles applications action ou vérité existent ?</h2>
<p>Il y en a des dizaines sur l'App Store. En voici quatre, avec ce que chacune annonce sur sa fiche.</p>
{{tableau:chouic,toz,cap,pafou}}

<h2>Quels critères comptent vraiment ?</h2>
<ul>
<li><strong>Le ton des cartes.</strong> Une bonne vérité fait raconter une histoire. Une mauvaise appelle un oui ou un non.</li>
<li><strong>Les niveaux.</strong> Il te faut au moins un niveau jouable avec des gens que tu connaissais peu ce matin.</li>
<li><strong>Le droit de passer.</strong> Un jeu qui force la main finit mal. Vérifie qu'on peut refuser une carte sans drame.</li>
<li><strong>La répétition.</strong> Si les mêmes cartes reviennent dans la soirée, le jeu s'épuise en vingt minutes.</li>
<li><strong>Le prix.</strong> Regarde ce qui reste gratuit, et si un seul joueur doit payer ou chacun.</li>
</ul>

<h2>En couple ou en groupe : est-ce la même app ?</h2>
<p>Pas forcément. Les cartes pour un couple et celles pour une bande de potes ne se ressemblent pas. L'app de Chouic propose un mode « couple » séparé du mode « groupe ».</p>
<p>PAFOU, lui, sépare les situations par jeu : [[jeu:cap-d-assumer|Cap d'assumer ?]] pour un groupe, et [[jeu:tete-a-tete|Tête-à-tête]] pour deux personnes qui se découvrent. Pour un couple installé, une app dédiée aux couples sera plus adaptée.</p>

<h2>Comment fonctionne Cap d'assumer ? dans PAFOU ?</h2>
<p>Chacun rejoint le salon avec son iPhone. À ton tour, tu désignes quelqu'un, qui choisit Action ou Vérité. La carte s'affiche chez tout le monde. Pendant qu'elle se joue, les autres parient : assumée ou esquivée ? Celui qui a désigné tranche.</p>
<p>Le niveau Tranquille est gratuit. Les niveaux Piquant et Spicy s'essaient une fois, puis demandent un achat. Spicy est réservé aux adultes.</p>

<h2>A-t-on besoin d'une app pour jouer à action ou vérité ?</h2>
<p>Non. Il suffit d'une liste d'idées et d'un peu d'imagination. On t'a préparé des [[questions-action-ou-verite|questions action ou vérité]] et des [[idees-de-gages-soiree|idées de gages]] à garder sous la main. L'app devient utile quand personne ne veut inventer, ou quand les idées tournent en rond.</p>
""",
        "faq": [
            ("Quelle est l'application action ou vérité la plus populaire en France ?", "Sur l'App Store français, « Action ou Vérité - Jeu Soirée » de Chouic affichait plus de 36 000 notes et 4,8 sur 5 le 19 novembre 2026."),
            ("Existe-t-il une app action ou vérité gratuite ?", "La plupart proposent des niveaux gratuits et des niveaux payants. Dans PAFOU, le niveau Tranquille de Cap d'assumer ? est gratuit."),
            ("Peut-on jouer à action ou vérité à deux ?", "Oui. La plupart des apps acceptent deux joueurs, et certaines ont un mode couple. Dans PAFOU, Cap d'assumer ? se joue dès 2 joueurs."),
        ],
    },
    {
        "slug": "jeu-de-bluff-entre-amis", "perso": "vin",
        "titre": "Quel jeu de bluff entre amis choisir ? Cartes, mots cachés et applications",
        "titre_seo": "Jeu de bluff entre amis : lequel choisir ? Notre guide",
        "titre_court": "Jeu de bluff entre amis",
        "description": "Les meilleurs types de jeux de bluff entre amis : le menteur, la pyramide, les jeux de rôles cachés. Et les applications pour y jouer : Undercover, Insight, PAFOU.",
        "resume": "Trois familles de jeux de bluff, et comment choisir.",
        "reponse": "Il existe trois familles de jeux de bluff entre amis : les jeux de cartes où l'on ment sur sa main, comme le menteur ou la pyramide ; les jeux de rôles cachés, comme Undercover, où il faut démasquer un imposteur ; et les jeux d'affirmations, comme Deux vérités, un mensonge. Sur iPhone, Undercover couvre les rôles cachés et PAFOU le bluff aux cartes avec La Pyramide.",
        "en_bref": ["<strong>Mentir sur ses cartes</strong> : le menteur, la pyramide.", "<strong>Cacher son rôle</strong> : l'imposteur, l'intrus, Undercover.", "<strong>Mentir sur soi</strong> : Deux vérités, un mensonge.", "Le bon jeu dépend du <strong>nombre de joueurs</strong> et du temps disponible."],
        "corps": """
<h2>Quels sont les grands types de jeux de bluff ?</h2>
<table>
<thead><tr><th>Famille</th><th>Le principe</th><th>Joueurs</th><th>Matériel</th></tr></thead>
<tbody>
<tr><td>Bluff aux cartes</td><td>Tu annonces une carte que tu n'as peut-être pas. Les autres te croient ou t'accusent.</td><td>2 à 8</td><td>Un paquet de cartes ou une app</td></tr>
<tr><td>Rôles cachés</td><td>Un ou plusieurs joueurs n'ont pas le même mot ou le même rôle. Il faut les démasquer.</td><td>4 à 12 et plus</td><td>Des papiers ou une app</td></tr>
<tr><td>Affirmations</td><td>Tu racontes des choses sur toi, dont une fausse. La table cherche le mensonge.</td><td>3 et plus</td><td>Rien</td></tr>
</tbody>
</table>

<h2>Quel jeu de bluff aux cartes choisir ?</h2>
<p>Le <strong>menteur</strong> est le plus simple : on pose ses cartes face cachée en annonçant leur valeur, et n'importe qui peut crier « Menteur ! ». On détaille [[regles-jeu-du-menteur|les règles du jeu du menteur]].</p>
<p>La <strong>pyramide</strong> ajoute la mémoire : tu mémorises tes cartes, puis tu ne les revois plus. Quand on t'accuse, tu dois retrouver la bonne carte. C'est le principe de [[jeu:la-pyramide|La Pyramide]] dans PAFOU, gratuite et jouable de 2 à 8. Avec un vrai paquet, suis [[regles-jeu-de-la-pyramide|les règles du jeu de la pyramide]].</p>

<h2>Quel jeu de rôles cachés choisir ?</h2>
<p>Sur téléphone, la référence est Undercover : tout le monde reçoit le même mot secret, sauf certains joueurs. Chacun décrit son mot sans le dire, puis on vote.</p>
{{tableau:undercover,insight,pafou}}
<p>Dans PAFOU, ce principe existe sous la forme d'un mini-jeu, L'Intrus, dans [[jeu:la-tournee|La Tournée]]. Ce n'est qu'une manche parmi d'autres : si tu veux une soirée entière de rôles cachés, une app dédiée comme Undercover est un meilleur choix. Pour y jouer sans app, lis [[jeu-de-l-intrus-regles|les règles du jeu de l'intrus]].</p>

<h2>Et pour bluffer sans aucun matériel ?</h2>
<p>[[deux-verites-un-mensonge|Deux vérités, un mensonge]] se joue n'importe où, dès trois personnes. C'est aussi un excellent jeu pour faire connaissance, et il fait partie d'[[jeu:on-se-decouvre|On se découvre]] dans PAFOU.</p>

<h2>Comment bien bluffer ?</h2>
<ul>
<li><strong>Dis souvent la vérité.</strong> Un menteur permanent est aussi lisible qu'un honnête permanent.</li>
<li><strong>Garde le même rythme.</strong> On repère un bluff à l'hésitation, ou au contraire à la réponse trop rapide.</li>
<li><strong>Bluffe quand ça coûte peu.</strong> Les premiers tours servent à brouiller ton image.</li>
<li><strong>Regarde qui t'accuse.</strong> Certains joueurs crient « Menteur » à tout le monde : mens-leur moins, dis-leur la vérité plus souvent.</li>
</ul>
""",
        "faq": [
            ("Quel jeu de bluff pour 2 joueurs ?", "Le bluff aux cartes fonctionne à deux : le menteur, ou La Pyramide dans PAFOU, qui se joue dès 2 joueurs. Les jeux de rôles cachés demandent au moins 4 joueurs."),
            ("Quelle application pour un jeu de bluff entre amis ?", "Undercover pour les rôles cachés, avec plus de 96 000 notes sur l'App Store français au 19 novembre 2026. PAFOU pour le bluff aux cartes, avec La Pyramide, gratuite."),
            ("Existe-t-il un jeu de bluff gratuit sur iPhone ?", "Oui. La Pyramide est toujours gratuite dans PAFOU. Undercover se télécharge aussi gratuitement, avec des achats intégrés."),
        ],
    },
    {
        "slug": "application-compteur-flechettes", "perso": "biere",
        "titre": "Quelle application pour compter les points aux fléchettes ?",
        "titre_seo": "Application compteur de fléchettes : laquelle choisir ?",
        "titre_court": "Application compteur de fléchettes",
        "description": "Compteur de fléchettes sur iPhone : comment choisir entre une app pour joueurs réguliers (DartCounter) et un compteur simple pour le bar (PAFOU). 301, 501, Cricket.",
        "resume": "Joueur régulier ou partie au bar : pas la même app.",
        "reponse": "Pour compter les points aux fléchettes, choisis selon ton usage. Si tu joues souvent et que tu veux des statistiques, des jeux d'entraînement ou des parties en ligne, prends une app spécialisée comme DartCounter. Si tu veux juste compter un 301, un 501 ou un Cricket entre amis au bar, le compteur gratuit de PAFOU suffit, sans compte et sans réseau.",
        "en_bref": ["<strong>Joueur régulier</strong> : une app spécialisée avec statistiques.", "<strong>Partie entre amis</strong> : un compteur simple, sans compte.", "Vérifie les <strong>jeux gérés</strong> : 301, 501, Cricket, finir sur un double.", "Notes relevées sur l'App Store français le <strong>19 novembre 2026</strong>."],
        "corps": """
<h2>Quelles applications comptent les points aux fléchettes ?</h2>
{{tableau:dartcounter,flechettes-compteur,pafou}}
<p>Les deux premières sont des apps de sport dédiées aux fléchettes. PAFOU est un jeu de soirée qui contient un compteur. Ce n'est pas le même objet, et c'est pour ça qu'on les distingue.</p>

<h2>Que doit savoir faire un bon compteur ?</h2>
<ul>
<li><strong>Gérer les jeux que tu joues.</strong> Au minimum le 301 et le 501. Le Cricket si ta bande aime la tactique.</li>
<li><strong>Entrer une fléchette en un geste.</strong> Si la saisie prend dix secondes, plus personne ne voudra tenir le téléphone.</li>
<li><strong>Annuler une erreur.</strong> On se trompe de zone au moins une fois par partie.</li>
<li><strong>Refuser un dépassement.</strong> En 301 et 501, dépasser zéro annule le tour : l'app doit le gérer seule.</li>
<li><strong>Tenir sans réseau.</strong> Beaucoup de salles de fléchettes sont en sous-sol.</li>
</ul>

<h2>Quand prendre une app spécialisée ?</h2>
<p>Quand les fléchettes sont ton sport, pas ton occupation du jeudi soir. Une app comme DartCounter annonce sur sa fiche des jeux d'entraînement, des parties en ligne et la sauvegarde de toutes tes parties dans un compte. Si tu veux suivre ta moyenne sur des mois ou jouer contre quelqu'un à distance, c'est ce qu'il te faut. PAFOU ne fait rien de tout ça.</p>

<h2>Quand le compteur de PAFOU suffit-il ?</h2>
<p>Quand tu veux juste que quelqu'un compte à ta place. Le [[jeu:flechettes|compteur de fléchettes de PAFOU]] gère le 301, le 501 et le Cricket pour 2 à 8 joueurs, avec l'option « finir sur un double ». Tu touches la cible à l'écran, tu peux annuler une fléchette, et la partie est sauvegardée à chaque lancer.</p>
<p>Il est toujours gratuit, sans compte, sans publicité et sans réseau. Et entre deux parties, le même téléphone sert au [[jeu:mode-bar|Mode bar]].</p>

<h2>Et pour compter de tête ?</h2>
<p>C'est possible, avec un peu de méthode. On explique comment [[compter-les-points-aux-flechettes|compter les points aux fléchettes]], et on rappelle [[regles-flechettes-301-501|les règles du 301 et du 501]].</p>
""",
        "faq": [
            ("Existe-t-il un compteur de fléchettes gratuit sur iPhone ?", "Oui. Le compteur de PAFOU est toujours gratuit. Les apps spécialisées se téléchargent aussi gratuitement, avec des options payantes."),
            ("Quelle app pour le Cricket aux fléchettes ?", "DartCounter et PAFOU gèrent le Cricket. Dans PAFOU, il se joue de 2 à 8 joueurs sur un seul téléphone."),
            ("Une app peut-elle compter les fléchettes toute seule ?", "Certaines apps annoncent un comptage par la caméra. Dans PAFOU, la saisie est manuelle : tu touches la zone atteinte sur la cible à l'écran."),
        ],
    },
    {
        "slug": "jeu-pour-premier-date", "perso": "whisky",
        "titre": "Quel jeu pour un premier date ? Les options qui évitent les blancs",
        "titre_seo": "Jeu pour un premier date : quoi choisir pour éviter les blancs",
        "titre_court": "Jeu pour un premier date",
        "description": "Quel jeu choisir pour un premier date : questions à deux, petits défis, applications. Ce qui marche, ce qu'il faut éviter, et le mode Tête-à-tête de PAFOU.",
        "resume": "Ce qui marche à deux quand on se connaît à peine.",
        "reponse": "Pour un premier date, choisis un jeu qui se joue à deux, sur la table, et qui fait parler plutôt que gagner. Les jeux de questions à tour de rôle fonctionnent le mieux. Évite les jeux pensés pour les couples installés, souvent trop intimes. Sur iPhone, le mode Tête-à-tête de PAFOU est conçu pour cette situation, avec un vote secret avant chaque montée de niveau.",
        "en_bref": ["Un bon jeu de premier date <strong>fait parler</strong>, il ne fait pas concourir.", "Les apps « couple » visent des gens <strong>déjà ensemble</strong> : ce n'est pas le même besoin.", "Il faut pouvoir <strong>refuser une question</strong> sans gêne.", "<strong>Un téléphone posé sur la table</strong>, pas un écran chacun."],
        "corps": """
<h2>Qu'est-ce qui fait un bon jeu de premier date ?</h2>
<ul>
<li><strong>Il se joue à deux</strong>, sans avoir besoin d'un troisième pour arbitrer.</li>
<li><strong>Il tient dans une poche.</strong> Personne n'arrive à un premier rendez-vous avec une boîte de jeu.</li>
<li><strong>Il monte doucement.</strong> Les premières questions doivent être faciles et drôles.</li>
<li><strong>Il laisse une porte de sortie.</strong> On doit pouvoir passer une question, ou arrêter, sans que ça se remarque.</li>
<li><strong>Il se joue à voix haute.</strong> Si chacun tape sur son écran, ce n'est plus un rendez-vous.</li>
</ul>

<h2>Quelles sont les options ?</h2>
<table>
<thead><tr><th>Option</th><th>Avantage</th><th>Limite</th></tr></thead>
<tbody>
<tr><td>Une liste de questions</td><td>Gratuit, rien à installer</td><td>Sortir une liste peut sembler préparé</td></tr>
<tr><td>Un petit jeu sans matériel</td><td>Spontané, se lance en une phrase</td><td>Il faut connaître les règles</td></tr>
<tr><td>Une app pour couples</td><td>Beaucoup de contenu</td><td>Pensée pour des gens déjà ensemble</td></tr>
<tr><td>Un jeu conçu pour un premier date</td><td>Le niveau monte seulement si les deux le veulent</td><td>Il faut que l'autre ait envie de jouer</td></tr>
</tbody>
</table>
<p>Pour les deux premières lignes, on t'a préparé des [[questions-premier-date|questions pour un premier rendez-vous]] et des [[jeux-pour-un-premier-date|petits jeux à faire à deux]].</p>

<h2>Les apps pour couples conviennent-elles ?</h2>
<p>Pas vraiment, et ce n'est pas leur faute. Une app comme Cray Cray s'adresse, d'après sa fiche, aux couples qui veulent se rapprocher un peu plus chaque jour, y compris à distance. C'est un autre besoin : on y parle de la relation, pas de se découvrir.</p>
{{tableau:craycray,pafou}}

<h2>Comment fonctionne Tête-à-tête dans PAFOU ?</h2>
<p>[[jeu:tete-a-tete|Tête-à-tête]] se joue sur un seul iPhone posé entre vous. Les cartes alternent questions et « Devine-moi », où l'un devine la réponse de l'autre. Trois niveaux : Léger, Vrai, Ça chauffe.</p>
<p>À la fin de chaque niveau, chacun vote en secret pour continuer ou non. L'app garde parfois le niveau même si les deux disent oui, pour qu'un refus ne puisse pas se deviner. Le jeu ne contient rien de sexuel et rien sur les ex. À la fin, le perdant paie l'addition.</p>
<p>Une partie d'essai est offerte. Ensuite, le mode demande un achat dans l'app.</p>

<h2>Que faut-il éviter ?</h2>
<ul>
<li>Les jeux à gages physiques ou à contact.</li>
<li>Les questions sur les anciennes relations.</li>
<li>Les jeux où l'on boit quand on perd : un premier rendez-vous se passe mieux avec les idées claires.</li>
<li>Insister si l'autre n'a pas envie de jouer. Dans ce cas, range le téléphone.</li>
</ul>
""",
        "faq": [
            ("Est-ce bizarre de proposer un jeu à un premier date ?", "Non, si tu le proposes légèrement et au bon moment, une fois installés. Si l'autre n'accroche pas, n'insiste pas."),
            ("Quel jeu faire à deux dans un bar ?", "Un jeu de questions à tour de rôle, Deux vérités un mensonge, ou une partie de fléchettes s'il y a une cible. Sur iPhone, Tête-à-tête de PAFOU se joue sur un seul téléphone."),
            ("Tête-à-tête est-il gratuit ?", "Une partie d'essai est offerte. Ensuite, le mode demande un achat dans l'app PAFOU."),
        ],
    },
    {
        "slug": "jeu-de-soiree-sans-materiel", "perso": "coupe",
        "titre": "Jeux de soirée sans matériel : quoi lancer quand on n'a rien sous la main",
        "titre_seo": "Jeux de soirée sans matériel : quoi lancer sans rien",
        "titre_court": "Jeux de soirée sans matériel",
        "description": "Les jeux de soirée sans matériel qui marchent vraiment : jeux de parole, de bluff, de mime, et les apps qui remplacent cartes et papier. Classés par situation.",
        "resume": "Parole, bluff, mime, téléphone : classés par situation.",
        "reponse": "Les meilleurs jeux de soirée sans matériel sont ceux qui se jouent à la voix : Qui de nous, Je n'ai jamais, Deux vérités un mensonge, Tu préfères, le mime. Aucun ne demande de cartes ni de plateau. Si tu veux des cartes, un compteur ou des votes secrets sans rien acheter, un téléphone suffit : une app comme PAFOU remplace le paquet de cartes et le papier.",
        "en_bref": ["<strong>Rien du tout</strong> : les jeux de parole et de mime.", "<strong>Un téléphone</strong> : cartes, votes secrets et chrono sans rien transporter.", "Choisis selon <strong>le nombre de joueurs</strong> et si le groupe se connaît.", "Tous ces jeux se jouent <strong>sans alcool</strong>, aux points ou aux gages."],
        "corps": """
<h2>Quels jeux se jouent sans rien du tout ?</h2>
<table>
<thead><tr><th>Jeu</th><th>Joueurs</th><th>Le principe</th></tr></thead>
<tbody>
<tr><td>Qui de nous</td><td>4 et plus</td><td>Une question, tout le monde pointe quelqu'un au signal.</td></tr>
<tr><td>Je n'ai jamais</td><td>3 et plus</td><td>Tu dis une chose que tu n'as jamais faite. Ceux qui l'ont faite baissent un doigt.</td></tr>
<tr><td>Deux vérités, un mensonge</td><td>3 et plus</td><td>Trois affirmations sur toi, la table cherche la fausse.</td></tr>
<tr><td>Tu préfères</td><td>2 et plus</td><td>Deux options impossibles, chacun choisit et défend son choix.</td></tr>
<tr><td>Le mime</td><td>4 et plus</td><td>Faire deviner un mot sans parler, en équipes.</td></tr>
</tbody>
</table>
<p>On a des listes prêtes pour chacun : [[questions-qui-de-nous|questions « Qui de nous »]], [[phrases-je-n-ai-jamais|phrases « Je n'ai jamais »]], [[questions-tu-preferes|dilemmes « Tu préfères »]], [[mots-a-mimer|mots à mimer]] et les règles de [[deux-verites-un-mensonge|Deux vérités, un mensonge]].</p>

<h2>Que change un téléphone ?</h2>
<p>Un téléphone remplace trois objets : le paquet de cartes, le papier et le chronomètre. Il permet aussi ce qu'on ne peut pas faire à la voix : voter en secret, distribuer un rôle caché, tirer une question que personne n'a écrite.</p>
<p>Deux formules existent. Avec <strong>un seul téléphone</strong>, personne n'a rien à installer. Avec <strong>chacun le sien</strong>, on peut bluffer et voter sans être vu. On compare les deux dans [[un-telephone-ou-chacun-le-sien|un téléphone ou chacun le sien]].</p>

<h2>Quel jeu sans matériel selon la situation ?</h2>
<table>
<thead><tr><th>Situation</th><th>Sans rien</th><th>Avec PAFOU sur iPhone</th></tr></thead>
<tbody>
<tr><td>Des potes proches</td><td>Qui de nous, Je n'ai jamais</td><td>[[jeu:les-dossiers|Les Dossiers]], [[jeu:cap-d-assumer|Cap d'assumer ?]]</td></tr>
<tr><td>Envie de bluffer</td><td>Deux vérités, un mensonge</td><td>[[jeu:la-pyramide|La Pyramide]]</td></tr>
<tr><td>Un groupe qui ne se connaît pas</td><td>Deux vérités, un mensonge, le mime</td><td>[[jeu:on-se-decouvre|On se découvre]]</td></tr>
<tr><td>Au bar</td><td>Tu préfères</td><td>[[jeu:mode-bar|Mode bar]], [[jeu:flechettes|fléchettes]]</td></tr>
<tr><td>À deux</td><td>Tu préfères, des questions à tour de rôle</td><td>[[jeu:tete-a-tete|Tête-à-tête]]</td></tr>
</tbody>
</table>

<h2>Faut-il de l'alcool pour que ces jeux marchent ?</h2>
<p>Non. Beaucoup de ces jeux sont connus comme des jeux à boire, mais aucun n'en a besoin. Un doigt baissé, un point perdu ou un petit gage font exactement le même travail. On donne des versions complètes dans [[jeux-de-soiree-sans-alcool|jeux de soirée sans alcool]]. Et si certains boivent, la règle reste simple : personne n'est jamais forcé, et l'abus d'alcool est dangereux pour la santé.</p>

<h2>Quelle app choisir pour remplacer le matériel ?</h2>
<p>Ça dépend du jeu que tu veux. On compare les principales dans [[guide:meilleure-app-jeu-de-soiree|quelle est la meilleure app de jeu de soirée]].</p>
""",
        "faq": [
            ("Quel jeu de soirée faire sans rien ?", "Qui de nous, Je n'ai jamais, Deux vérités un mensonge, Tu préfères et le mime se jouent sans aucun matériel."),
            ("Quel jeu de soirée sans cartes ?", "Tous les jeux de parole fonctionnent sans cartes. Pour un jeu de cartes sans paquet, La Pyramide dans PAFOU distribue et compte à ta place."),
            ("Peut-on jouer à ces jeux sans alcool ?", "Oui. Tous se jouent aux points ou aux gages. L'alcool n'est nécessaire dans aucun d'eux."),
        ],
    },
    {
        "slug": "alternatives-picolo", "perso": "spritz",
        "titre": "Quelles alternatives à Picolo ? 6 jeux de soirée à essayer",
        "titre_seo": "Alternatives à Picolo : 6 jeux de soirée à essayer en 2026",
        "titre_court": "Alternatives à Picolo",
        "description": "Tu connais Picolo par cœur ? Six alternatives pour changer : TOZ, JUDUKU, Undercover, Insight, Vakarm et PAFOU, avec ce que chacune fait de différent.",
        "resume": "Six apps pour changer, et ce que chacune fait de différent.",
        "reponse": "Si tu cherches une alternative à Picolo, tout dépend de ce que tu veux changer. Pour rester sur un seul téléphone avec des classiques, regarde TOZ. Pour un jeu de mots avec un imposteur, Undercover ou Insight. Pour des votes entre potes, Vakarm. Pour un jeu de bluff, un mode bar et des jeux où chacun a son téléphone, PAFOU.",
        "en_bref": ["Picolo reste une <strong>valeur sûre</strong> : plus de 46 000 notes sur l'App Store français.", "Changer d'app sert surtout à <strong>changer de type de jeu</strong>.", "Regarde si tu veux rester sur <strong>un seul téléphone</strong>.", "Notes relevées le <strong>19 novembre 2026</strong>."],
        "corps": """
<h2>Pourquoi chercher une alternative à Picolo ?</h2>
<p>Rarement parce que l'app est mauvaise. Picolo est l'un des jeux de soirée les plus installés en France, et son principe est limpide : on inscrit les prénoms, on lit les consignes. On cherche autre chose quand on connaît les cartes, quand on veut un jeu avec de la stratégie, ou quand on veut que chacun joue sur son téléphone.</p>

<h2>Quelles sont les alternatives ?</h2>
{{tableau:picolo,toz,juduku,undercover,insight,vakarm,pafou}}

<h2>Laquelle choisir selon ce que tu veux changer ?</h2>
<table>
<thead><tr><th>Tu veux…</th><th>Regarde</th></tr></thead>
<tbody>
<tr><td>Le même confort, d'autres cartes</td><td>TOZ</td></tr>
<tr><td>Du rythme et du bruit</td><td>JUDUKU</td></tr>
<tr><td>Chercher un imposteur</td><td>Undercover, Insight</td></tr>
<tr><td>Voter les uns sur les autres</td><td>Vakarm, PAFOU</td></tr>
<tr><td>Bluffer avec des cartes</td><td>PAFOU</td></tr>
<tr><td>Un jeu pour le bar ou pour un rendez-vous à deux</td><td>PAFOU</td></tr>
</tbody>
</table>

<h2>Qu'est-ce que PAFOU fait de différent ?</h2>
<p>PAFOU n'est pas un jeu de consignes à lire, c'est une boîte de plusieurs jeux. [[jeu:la-pyramide|La Pyramide]] est un jeu de bluff et de mémoire. [[jeu:les-dossiers|Les Dossiers]] posent des questions qui citent les prénoms, pendant que les autres parient. Le [[jeu:mode-bar|Mode bar]] se joue sur un seul téléphone, comme Picolo, mais sans points et sans alcool.</p>
<p>Ce que PAFOU ne fait pas : il n'existe que sur iPhone, seulement en français, et il est trop récent pour avoir des notes. La Pyramide et les fléchettes sont gratuites ; plusieurs modes sont payants après un essai.</p>

<h2>Et si on arrêtait les apps ?</h2>
<p>C'est aussi une alternative. Une liste de [[jeux-de-soiree-entre-potes|jeux de soirée entre potes]] et quelques [[questions-qui-de-nous|questions « Qui de nous »]] suffisent pour une soirée entière.</p>
""",
        "faq": [
            ("Quel jeu ressemble à Picolo ?", "TOZ est le plus proche dans l'esprit : des classiques de soirée à lire sur un seul téléphone. Dans PAFOU, le Mode bar se joue aussi sur un seul téléphone."),
            ("Quelle alternative à Picolo sans alcool ?", "Undercover ne repose pas sur l'alcool. Dans PAFOU, le Mode bar, On se découvre et La Pyramide se jouent entièrement sans alcool."),
            ("Picolo ou PAFOU ?", "Picolo si tu veux un jeu de consignes à lire, connu de tous. PAFOU si tu veux plusieurs jeux différents, dont un jeu de bluff, et que ton groupe est sur iPhone."),
        ],
    },
]

FAQ = [
    ("L'app", [
        ("C'est quoi, PAFOU ?", "PAFOU est un jeu de soirée sur iPhone, en français. L'app réunit plusieurs jeux : La Pyramide (bluff et mémoire), Les Dossiers (questions entre potes), Cap d'assumer ? (action ou vérité), La Tournée (mini-jeux), le Mode bar, un compteur de fléchettes, Tête-à-tête pour un premier date et On se découvre pour briser la glace."),
        ("Sur quels téléphones PAFOU fonctionne-t-il ?", "Sur iPhone, avec iOS 16.4 ou plus récent. Il n'existe pas de version Android."),
        ("PAFOU est-il gratuit ?", "PAFOU se télécharge gratuitement. La Pyramide, les fléchettes et le niveau Tranquille des Dossiers et de Cap d'assumer ? sont toujours gratuits. Les autres modes et niveaux s'essaient une fois, puis demandent un achat dans l'app."),
        ("Y a-t-il de la publicité dans PAFOU ?", "Non. Il n'y a pas de publicité dans l'app."),
        ("À partir de quel âge peut-on jouer ?", "PAFOU est classé 17+ sur l'App Store. Certains niveaux sont réservés aux adultes."),
        ("En quelle langue est PAFOU ?", "En français uniquement, pour l'instant."),
    ]),
    ("Jouer", [
        ("Combien de joueurs faut-il ?", "De 2 à 12 selon le jeu. Tête-à-tête se joue à 2, La Pyramide, Les Dossiers et Cap d'assumer ? de 2 à 8, La Tournée de 3 à 8, et On se découvre jusqu'à 12."),
        ("Faut-il que tout le monde ait l'app ?", "Pas pour tous les jeux. Le Mode bar, On se découvre, Tête-à-tête, les fléchettes et La Pyramide en mode « Un seul tél » se jouent avec un seul iPhone. Les Dossiers, Cap d'assumer ? et La Tournée demandent un iPhone par joueur."),
        ("Comment rejoindre une partie ?", "Celui qui crée le salon partage un code de 6 caractères, un lien ou un QR code. Les autres ouvrent PAFOU, choisissent « Rejoindre avec un code » ou scannent le QR code."),
        ("Faut-il créer un compte ?", "Non. Le compte est facultatif. Il garde tes statistiques et tes titres, et il est nécessaire seulement pour les bandes de potes."),
        ("Faut-il une connexion internet ?", "Pour les jeux à plusieurs téléphones, oui. Le Mode bar, On se découvre, Tête-à-tête et les fléchettes fonctionnent sans réseau."),
        ("Peut-on tester PAFOU tout seul ?", "Oui. Dans le salon d'une partie, le bouton « + démo » ajoute des joueurs simulés pour découvrir un jeu avant la soirée."),
    ]),
    ("Le contenu", [
        ("PAFOU est-il un jeu à boire ?", "Non. PAFOU est un jeu de soirée : les jeux se jouent aux points, aux votes ou aux gages. Une option « verre » existe dans certains jeux, facultative, réglée par chaque joueur, avec ou sans alcool. L'abus d'alcool est dangereux pour la santé."),
        ("Peut-on jouer sans alcool ?", "Oui, à tous les jeux. Le Mode bar, On se découvre et Tête-à-tête ne contiennent aucune référence à l'alcool."),
        ("Combien y a-t-il de cartes ?", "Plus de 400, écrites en français. Une carte déjà sortie pendant la soirée ne revient pas."),
        ("PAFOU enregistre-t-il ce qu'on dit ?", "Non. Tout se joue à voix haute. L'app n'enregistre jamais les réponses, et ne demande ni photo ni contact."),
        ("Peut-on refuser une carte ?", "Oui, toujours, et sans se justifier. Le joueur ne marque simplement pas les points de la carte."),
    ]),
    ("Le payant", [
        ("Qu'est-ce qui est payant dans PAFOU ?", "Les niveaux Piquant et Spicy des Dossiers et de Cap d'assumer ?, La Tournée, le Mode bar, On se découvre et Tête-à-tête. Chacun s'essaie une fois gratuitement. Les prix sont affichés dans l'app avant tout achat."),
        ("Faut-il que chaque joueur paie ?", "Non. Dans une partie à plusieurs téléphones, il suffit qu'un joueur de la table ait débloqué un mode pour que tout le salon y joue pendant cette partie."),
        ("Comment retrouver un achat sur un nouveau téléphone ?", "Sur l'écran d'achat de l'app, touche « Restaurer mes achats »."),
    ]),
]
