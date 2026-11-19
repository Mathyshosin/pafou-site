# Contrôle les articles du blog avant publication. Usage : python3 _outils/verifier_blog.py [slug ...]
# Sans argument : tous les articles, et le calendrier doit être complet.
import html, importlib.util, os, re, sys

sys.path.insert(0, os.path.dirname(__file__))
from blog_calendrier import ORDRE
from slugs import CATEGORIES, GUIDES_SLUGS, JEUX_SLUGS, PERSOS

DOSSIER = os.path.join(os.path.dirname(__file__), "articles")
CHAMPS = ["slug", "categorie", "mot_cle", "titre", "titre_seo", "titre_court", "description", "resume", "perso", "jeu", "lire_aussi", "reponse", "en_bref", "corps", "faq"]
INTERDITS = [
    "cul sec", "cul-sec", "shot", "bourré", "ivre", "ivresse", "se mettre une mine", "finir son verre", "finis ton verre", "beuverie", "gueule de bois",
    "n° 1", "numéro 1", "numéro un", "la meilleure app", "le meilleur jeu de soirée", "100 % gratuit", "entièrement gratuit", "totalement gratuit", "tout est gratuit",
    "des milliers de joueurs", "des millions", "étude", "selon une enquête", "android", "€",
    "sexe", "sexuel", "coucher avec", "nu ", "nue ", "strip",
]
CONCURRENTS_OK = ["picolo", "toz", "juduku", "undercover", "insight", "vakarm", "chouic", "dartcounter"]
AUTRES_APPS = ["heads up", "psych", "kahoot", "jackbox", "bazar", "sans tact", "party up", "chopine", "guess up", "cray cray", "paired"]
EMOJI = re.compile("[\U0001F000-\U0001FAFF☀-➿⬀-⯿️]")


def charger(slug):
    spec = importlib.util.spec_from_file_location("a_" + slug.replace("-", "_"), os.path.join(DOSSIER, slug + ".py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.ARTICLE


def tous_les_slugs():
    return sorted(f[:-3] for f in os.listdir(DOSSIER) if f.endswith(".py"))


def mots(fragment):
    return len(re.sub(r"<[^>]+>", " ", fragment).split())


def controler(a, slug):
    pb = []
    for c in CHAMPS:
        if c not in a:
            pb.append(f"champ manquant : {c}")
    if pb:
        return pb
    if a["slug"] != slug: pb.append("le slug ne correspond pas au nom du fichier")
    if a["categorie"] not in CATEGORIES: pb.append(f"catégorie inconnue : {a['categorie']}")
    if a["perso"] not in PERSOS: pb.append(f"personnage inconnu : {a['perso']}")
    if a["jeu"] is not None and a["jeu"] not in JEUX_SLUGS: pb.append(f"jeu inconnu : {a['jeu']}")
    if not 45 <= len(a["titre"]) <= 95: pb.append(f"titre : {len(a['titre'])} caractères (45 à 95)")
    if len(a["titre_seo"]) > 60: pb.append(f"titre_seo : {len(a['titre_seo'])} caractères (60 au plus)")
    if len(a["titre_court"]) > 40: pb.append(f"titre_court : {len(a['titre_court'])} caractères (40 au plus)")
    if not 120 <= len(a["description"]) <= 160: pb.append(f"description : {len(a['description'])} caractères (120 à 160)")
    if len(a["resume"]) > 110: pb.append(f"resume : {len(a['resume'])} caractères (110 au plus)")
    n = len(a["reponse"].split())
    if not 40 <= n <= 75: pb.append(f"reponse : {n} mots (40 à 75)")
    if not 3 <= len(a["en_bref"]) <= 4: pb.append("en_bref : 3 ou 4 points")
    if not 3 <= len(a["faq"]) <= 4: pb.append("faq : 3 ou 4 questions")
    for q, r in a["faq"]:
        if not q.strip().endswith("?"): pb.append(f"question de FAQ sans point d'interrogation : {q}")
    n = mots(a["corps"])
    if not 700 <= n <= 1400: pb.append(f"corps : {n} mots (700 à 1 300)")
    if a["corps"].count("<h2>") < 4: pb.append("corps : au moins 4 <h2>")
    if re.search(r"<(h1|img|script|style|a )", a["corps"]): pb.append("balise interdite dans le corps (h1, img, script, style, a)")
    if "PAFOU" not in a["corps"]: pb.append("PAFOU n'apparaît pas dans le corps")
    liens = re.findall(r"\[\[([^\]|]+)\|[^\]]+\]\]", a["corps"])
    if len(liens) < 2: pb.append("au moins 2 liens internes [[slug|texte]]")
    if not any(l.startswith(("jeu:", "guide:")) for l in liens): pb.append("au moins un lien vers une page de jeu ou un guide")
    for l in liens:
        if l.startswith("jeu:"):
            if l[4:] not in JEUX_SLUGS: pb.append(f"lien vers un jeu inconnu : {l}")
        elif l.startswith("guide:"):
            if l[6:] not in GUIDES_SLUGS: pb.append(f"lien vers un guide inconnu : {l}")
        elif l not in ORDRE or l == slug: pb.append(f"lien vers un article inconnu : {l}")
    if not 2 <= len(a["lire_aussi"]) <= 3: pb.append("lire_aussi : 2 ou 3 articles")
    for s in a["lire_aussi"]:
        if s not in ORDRE or s == slug: pb.append(f"lire_aussi inconnu : {s}")
    tout = " ".join([a["titre"], a["titre_seo"], a["description"], a["resume"], a["reponse"], " ".join(a["en_bref"]), a["corps"], " ".join(q + " " + r for q, r in a["faq"])])
    bas = html.unescape(re.sub(r"<[^>]+>", " ", tout)).lower().replace(" ", " ").replace(" ", " ")
    for mot in INTERDITS:
        if re.search(r"(?<![a-zàâçéèêëîïôûùüÿœ])" + re.escape(mot), bas): pb.append(f"expression à éviter : « {mot.strip()} »")
    for app in AUTRES_APPS:
        if re.search(r"\b" + re.escape(app) + r"\b", bas): pb.append(f"app non autorisée citée : {app}")
    if re.search(r"\b(vous|votre|vos)\b", bas.replace("rendez-vous", "rdv")): pb.append("tutoiement obligatoire (vous/votre/vos trouvé)")
    if EMOJI.search(tout): pb.append("emoji ou symbole décoratif trouvé")
    return pb


def main():
    demandes = sys.argv[1:]
    slugs = demandes or tous_les_slugs()
    erreurs = 0
    vus = {}
    for slug in slugs:
        try:
            a = charger(slug)
            pb = controler(a, slug)
        except Exception as e:
            a, pb = {}, [f"fichier illisible : {e}"]
        for c in ("titre", "titre_seo", "description", "mot_cle"):
            if a.get(c) and (c, a[c]) in vus: pb.append(f"{c} en double avec {vus[(c, a[c])]}")
            vus[(c, a.get(c))] = slug
        if pb:
            erreurs += len(pb)
            print(f"✗ {slug}")
            for p in pb: print("   -", p)
    if not demandes:
        for s in ORDRE:
            if s not in slugs:
                erreurs += 1
                print(f"✗ {s} : dans le calendrier, mais pas écrit")
        for s in slugs:
            if s not in ORDRE:
                erreurs += 1
                print(f"✗ {s} : écrit, mais absent du calendrier")
    print(f"{len(slugs)} articles, {erreurs} problème(s)")
    sys.exit(1 if erreurs else 0)


if __name__ == "__main__":
    main()
