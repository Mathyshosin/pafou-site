# Signale les nouvelles pages à Bing et aux moteurs IndexNow.
# Lit sur l'entrée standard des chemins comme blog/mon-article/index.html.
import json, sys, urllib.request

HOTE = "pafouapp.fr"  # à changer avec BASE dans generer.py si le domaine change
CLE = "4baf4f31d57b47b494722fcef72fc881"

chemins = [c.strip() for c in sys.stdin if c.strip()]
if chemins:
    urls = [f"https://{HOTE}/" + c.replace("index.html", "") for c in chemins]
    corps = json.dumps({"host": HOTE, "key": CLE, "keyLocation": f"https://{HOTE}/{CLE}.txt", "urlList": urls}).encode()
    req = urllib.request.Request("https://api.indexnow.org/indexnow", data=corps, headers={"Content-Type": "application/json; charset=utf-8"})
    print("IndexNow :", urllib.request.urlopen(req, timeout=20).status, urls)
