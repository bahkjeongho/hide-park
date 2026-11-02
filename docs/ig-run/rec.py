import csv,os,json,sys,re,unicodedata
D="/Users/parkjeongho/Developer/Hide-Park/docs/ig-run/"
Q=json.load(open(D+"queue.json"))
by={r["username"]:r for r in Q}
def done():
    if not os.path.exists(D+"progress.csv"): return set()
    return {r["username"] for r in csv.DictReader(open(D+"progress.csv",encoding="utf-8-sig"))}
def rec(u,cls,topic="",ev="",note="",access=0,reason="",cand=""):
    new=not os.path.exists(D+"progress.csv")
    with open(D+"progress.csv","a",encoding="utf-8-sig",newline="") as f:
        w=csv.writer(f)
        if new: w.writerow(["username","분류","topic","증거 URL","노트 경로","웹 접근 횟수"])
        w.writerow([u,cls,topic,ev,note,access])
    if cls!="found":
        r=by[u]
        new=not os.path.exists(D+"manual-todo.csv")
        with open(D+"manual-todo.csv","a",encoding="utf-8-sig",newline="") as f:
            w=csv.writer(f)
            if new: w.writerow(["username","url","display_name","분류","사유","후보 topic","archived","note"])
            w.writerow([u,r["url"],r["display_name"],cls,reason,cand,r["archived"],r["note"]])

def mknote(fn,aliases,topics,ig,website="",urls=(),wikis=(),cities=(),countries=(),tldr="",ko="",en="",summary=None,sports=None):
    def lst(k,vs,wl=False):
        if not vs: return f"{k}:\n"
        return f"{k}:\n"+"".join((f'  - "[[{v}]]"\n' if wl else f"  - {v}\n") for v in vs)
    fm="---\n"+lst("aliases",aliases)+lst("topic",topics,True)+lst("IG",[ig])+lst("Website",[website] if website else [])+lst("URL",urls)+lst("Wikis",wikis)+lst("Cities",cities,True)+lst("Countries",countries,True)+"tags:\nRelated:\n---\n"
    info="> [!Info]\n"+(f"> {ko}\n>\n> {en}\n" if ko and en else (f"> {en}\n" if en else ""))
    summ="> [!Summary]\n"+("".join(["> |   |   |\n> |---|---|\n"]+[f"> |{a}|{b}|\n" for a,b in summary]) if summary else "")
    body=f">[!tldr] tl;dr\n>{tldr}\n\n{info}\n{summ}\n---\n\n# Portfolio\n\n\n---\n\n# People\n\n"
    p=D+"notes/"+fn+".md"
    open(p,"w",encoding="utf-8").write(fm+body)
    return "ig-run/notes/"+fn+".md"

def artist(fn,al,ig,web="",urls=(),wikis=(),cities=(),countries=()):
    L=lambda k,vs,wl=False: f"{k}:\n"+"".join((f'  - "[[{v}]]"\n' if wl else f"  - {v}\n") for v in vs)
    fm="---\n"+L("aliases",al)+L("topic",["Music Artist"],True)+"Genre:\nLabels:\nMember of:\n"+L("IG",[ig])+L("Website",[web] if web else [])+L("URL",urls)+L("Wikis",wikis)+L("Cities",cities,True)+L("Countries",countries,True)+"tags:\nRelated:\n---\n"
    open(D+"notes/"+fn+".md","w",encoding="utf-8").write(fm+"> [!Summary]\n\n---\n\n# People\n\n\n---\n\n# Discography\n\n"); return "ig-run/notes/"+fn+".md"
def exists(fn):
    import json,unicodedata
    return unicodedata.normalize("NFC",fn).lower() in set(json.load(open(D+"vault_names.json")))
