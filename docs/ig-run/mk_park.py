import csv,sys,os,re
from urllib.parse import urlparse
from rec import *
rows={r[0]:r for r in list(csv.reader(open(D+"manual-check-Park.csv",encoding="utf-8-sig")))[1:]}
def make(E):
    made=[];skip=[]
    for u,(fn,al,tp,ci,co,tl) in E.items():
        r=rows[u]; ig=r[1] if r[1].endswith("/") else r[1]+"/"
        web=r[2]; url=r[3]
        if not web:
            m=re.search(r"\b([a-z0-9-]+(?:\.[a-z0-9-]+)*\.(?:com|kr|co\.kr|net|org|studio|agency|be|fr|co|io)(?:\.[a-z]{2})?)\b",r[4])
            if m and "." in m.group(1) and not m.group(1).startswith("hello@"): web="https://"+m.group(1)
        if web:
            pu=urlparse(web if "//" in web else "https://"+web); web=f"{pu.scheme}://{pu.netloc}"
        if exists(fn): skip.append((u,fn)); continue
        p=mknote(fn,al,tp,ig,website=web,urls=[url] if url else [],cities=ci,countries=co,tldr=tl)
        made.append(fn)
    return made,skip
