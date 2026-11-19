# L'ordre de publication du blog : DEBUT reçoit les LANCEMENT premiers articles,
# puis un article par jour. Ajouter un stock = ajouter des slugs à la fin de la liste.
# Un article déjà publié ne doit plus changer de place.
# DEBUT = le jour de la mise en ligne du site : à régler ce jour-là, une seule fois.
from datetime import date, timedelta

DEBUT = date(2026, 11, 19)
LANCEMENT = 3

ORDRE = [
    "jeux-de-soiree-entre-potes",
    "questions-action-ou-verite",
    "regles-jeu-de-la-pyramide",
    "jeux-pour-un-premier-date",
    "jeux-de-soiree-sans-alcool",
    "regles-flechettes-301-501",
    "questions-qui-de-nous",
    "jeux-a-deux-en-soiree",
    "phrases-je-n-ai-jamais",
    "jeux-de-bar-entre-amis",
    "jeux-a-boire-sans-materiel",
    "questions-premier-date",
    "jeux-pour-briser-la-glace",
    "idees-de-gages-soiree",
    "regles-jeu-du-menteur",
    "jeux-de-noel-entre-amis",
    "questions-tu-preferes",
    "compter-les-points-aux-flechettes",
    "jeux-grande-tablee",
    "deux-verites-un-mensonge",
    "un-telephone-ou-chacun-le-sien",
    "jeux-anniversaire-adulte",
    "jeu-de-l-intrus-regles",
    "jeux-nouvel-an-entre-amis",
    "regles-cricket-flechettes",
    "jeux-a-deux-en-couple",
    "mots-a-mimer",
    "relancer-une-soiree-qui-retombe",
    "organiser-une-soiree-jeux",
    "jeux-cremaillere",
]


def date_de(slug):
    i = ORDRE.index(slug)
    return DEBUT if i < LANCEMENT else DEBUT + timedelta(days=i - LANCEMENT + 1)
