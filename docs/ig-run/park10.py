import re
from park03 import *
import park03
tp=set(re.findall(r"^- (.+?) \(\d+\)",open(D+"topics.md",encoding="utf-8").read(),re.M))

def fix(fn,ts):
    p=D+"notes/"+fn+".md"; t=open(p,encoding="utf-8").read()
    t=re.sub(r"topic:\n(?:  - .*\n)*","topic:\n"+"".join(f'  - "[[{x}]]"\n' for x in ts),t,count=1); open(p,"w",encoding="utf-8").write(t)
def wk2(r):
    d=r[3].replace("en.wikipedia.com","en.wikipedia.org")
    return [d] if "wikipedia.org" in d else []
W={
"aurgdesign":("AURG",["AURG Design"],["Design Studio"],["Seoul"],["South Korea"],"서울 기반 디자인 스튜디오"),
"showstudio":("SHOWstudio",[],["Media"],["London"],["UK"],"런던의 패션 플랫폼"),
"tba21academy":("TBA21–Academy",["TBA21-Academy","TBA21 Academy"],["Art Platform"],["Venice"],["Italy"],"Thyssen-Bornemisza Art Contemporary의 아카데미"),
"zoeygrossman":("Zoey Grossman",["zoey grossman"],["Photographer"],[],["USA"],"사진가"),
"roelnabuurs":("Roel Nabuurs",[],["Fashion"],[],["Netherlands"],"모델"),
"choquelegoff":("Atelier Choque Le Goff",["Choque Le Goff"],["Design Studio"],["Paris"],["France"],"파리 기반 디자인 스튜디오"),
"julianklincewicz":("Julian Klincewicz",[],["Photographer"],[],["USA"],"사진가"),
"kaleidoscopemagazine":("Kaleidoscope",["KALEIDOSCOPE"],["Art Magazine"],["Milan"],["Italy"],"밀라노의 현대미술 매거진"),
"spurmagazine":("SPUR",[],["Fashion Magazine"],["Tokyo"],["Japan"],"슈에이샤가 발행하는 일본 패션 매거진"),
"studio_okgo":("STUDIO OKGO",["스튜디오 오케이고"],["Design Studio"],["Seoul"],["South Korea"],"서울 기반 디자인 스튜디오"),
"tabula.rasa.records":("Tabula Rasa Record Company",["Tabula Rasa"],["Record Label"],["San Francisco"],["USA"],"샌프란시스코의 레코드 컴퍼니"),
"actualobjects":("Actual Objects",[],["Creative Studio"],["Los Angeles"],["USA"],"2019년 설립된 로스앤젤레스 크리에이티브 스튜디오"),
"circuscircuscircuscircus":("Circus Magazine",["CIRCUS MAGAZINE"],["Magazine"],["London"],["UK"],"2021년 Jackson Bowley가 창간한 런던의 뷰티 매거진"),
"newschoolrepresents":("New School Represents",[],["Creative Collective"],["London"],["UK"],"2021년 설립된 런던 크리에이티브 컬렉티브이자 에이전시"),
}
A={}
done=[]
for u,(fn,al,ts,ci,co,tl) in W.items():
    assert all(t in tp for t in ts),(fn,[t for t in ts if t not in tp])
    if exists(fn): print("exists",fn);continue
    r=rows[u]; mknote(fn,al,ts,norm(r[1]),website=site(r),wikis=wk2(r),cities=ci,countries=co,tldr=tl); done.append((u,fn))
for u,(fn,al,ex,ci,co) in A.items():
    if exists(fn): print("exists",fn);continue
    r=rows[u]; ts=["Music Artist"]+ex; assert all(t in tp for t in ts),fn
    artist(fn,al,norm(r[1]),web=site(r),wikis=wk2(r),cities=ci,countries=co); fix(fn,ts); done.append((u,fn))
import csv as c
w=c.writer(open(D+"park-done.csv","a",newline="",encoding="utf-8-sig"))
for u,fn in done: w.writerow([u,fn+".md",9])
print(len(done))
