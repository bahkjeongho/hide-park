import re
from park03 import *
tp=set(re.findall(r"^- (.+?) \(\d+\)",open(D+"topics.md",encoding="utf-8").read(),re.M))
# wiki: user:(file,aliases,topics,cities,countries,tldr)
W={
"lollapalooza":("Lollapalooza",[],["Music Festival"],["Chicago"],["USA"],"1991년 시작된 시카고의 음악 페스티벌"),
"louisianamuseum":("Louisiana Museum of Modern Art",["Louisiana"],["Museum"],["Humlebæk"],["Denmark"],"1958년 개관한 덴마크 훔레벡의 현대미술관"),
"lovemagazine":("LOVE",["Love Magazine"],["Fashion Magazine"],["London"],["UK"],"2009년 Katie Grand가 창간한 패션 매거진"),
"mmparisdotcom":("M/M (Paris)",["M/M Paris"],["Graphic Designer","Art Collective"],["Paris"],["France"],"1992년 Mathias Augustyniak와 Michael Amzalag가 결성한 아트·디자인 듀오"),
"marcjacobs":("Marc Jacobs",[],["Fashion Designer","Fashion Brand"],["New York"],["USA"],"미국 패션 디자이너이자 그의 브랜드"),
"marcnewsonofficial":("Marc Newson",[],["Designer"],[],["Australia"],"호주 출신 산업 디자이너"),
"margaretzhang":("Margaret Zhang",["章凝"],["Editor-in-Chief","Creative Director"],[],["Australia"],"전 Vogue China 편집장"),
"matthewmwilliams":("Matthew M. Williams",["Matthew M Williams"],["Fashion Designer","Creative Director"],[],["USA"],"1017 ALYX 9SM의 공동 창업자"),
"mbierut":("Michael Bierut",[],["Graphic Designer"],["New York"],["USA"],"Pentagram의 파트너"),
"mixmag":("Mixmag",[],["Music Magazine"],["London"],["UK"],"1983년 창간한 런던의 댄스 음악 매거진"),
"mowalola":("Mowalola",["Mowalola Ogunlesi"],["Fashion Brand","Fashion Designer"],["London"],["UK"],"Mowalola Ogunlesi가 이끄는 런던 브랜드"),
"mschf":("MSCHF",[],["Art Collective"],["New York"],["USA"],"브루클린 기반 아트 컬렉티브"),
"mubi":("MUBI",[],["Media Company"],["London"],["UK"],"2007년 시작된 런던 기반 영화 스트리밍·배급사"),
"moca_busan":("부산현대미술관",["Museum of Contemporary Art Busan","MoCA Busan"],["Museum"],["Busan"],["South Korea"],"2018년 개관한 부산의 현대미술관"),
"smkmuseum":("SMK",["Statens Museum for Kunst","National Gallery of Denmark"],["Museum"],["Copenhagen"],["Denmark"],"덴마크 국립미술관"),
"ninjatune":("Ninja Tune",[],["Record Label"],["London"],["UK"],"1990년 Coldcut이 설립한 런던 레이블"),
"numeromagazine":("Numéro",["Numero"],["Fashion Magazine"],["Paris"],["France"],"1998년 Elisabeth Djian이 창간한 프랑스 패션·컬처 매거진"),
"oakley":("Oakley",["Oakley, Inc."],["Fashion Brand"],[],["USA"],"1975년 Jim Jannard가 설립한 아이웨어 브랜드"),
"pppiccioli":("Pierpaolo Piccioli",[],["Fashion Designer","Creative Director"],[],["Italy"],"이탈리아 패션 디자이너"),
"purplefashionmagazine":("Purple Fashion Magazine",["Purple"],["Fashion Magazine"],["Paris"],["France"],"2004년 분리 창간한 패션 매거진"),
"rhizomedotorg":("Rhizome",["rhizome.org"],["Art Platform"],["New York"],["USA"],"디지털 아트를 다루는 비영리 단체"),
"sbnation":("SB Nation",["Sports Blog Nation"],["Media"],[],["USA"],"2003년 시작된 스포츠 블로그 네트워크"),
"sereeeenam":("Serena Motola",[],["Fashion"],[],["Japan"],"일본 모델이자 배우"),
"sharjahart":("Sharjah Art Foundation",[],["Art Platform"],["Sharjah"],["United Arab Emirates"],"2009년 설립된 샤르자의 예술 재단"),
"simon_porte_jacquemus":("Simon Porte Jacquemus",["SIMON PORTE JACQUEMUS"],["Fashion Designer","Creative Director"],[],["France"],"Jacquemus의 창립자"),
"slanted_publishers":("Slanted Publishers",["Slanted"],["Publishing Compnay"],["Karlsruhe"],["Germany"],"Lars Harmsen과 Julia Kahl이 2014년 설립한 카를스루에 출판사"),
"snohetta":("Snøhetta",["Snohetta"],["Architecture Firm"],["Oslo"],["Norway"],"노르웨이의 건축·조경·디자인 회사"),
"ssense":("SSENSE",[],["Fashion"],["Montreal"],["Canada"],"2003년 몬트리올에서 시작한 럭셔리 리테일러"),
"stefanopilati":("Stefano Pilati",[],["Fashion Designer"],["Milan"],["Italy"],"1965년 밀라노 출생 패션 디자이너"),
"stuartvevers":("Stuart Vevers",[],["Creative Director"],[],["UK"],"Coach의 크리에이티브 디렉터"),
"susiebubble":("Susie Lau",["Susie Bubble","Susanna Lau"],["Blogger","Writer"],["London"],["UK"],"영국 패션 블로거이자 작가"),
"systemmagazine":("System",["System Magazine"],["Fashion Magazine"],["London"],["UK"],"패션 매거진"),
"szilvesztermako":("Szilveszter Makó",["SZILVESZTER MAKÓ"],["Photographer"],[],["Hungary"],"1992년생 헝가리 사진가"),
"therow":("The Row",[],["Fashion Brand"],["New York"],["USA"],"Olsen 자매가 설립한 패션 레이블"),
"thewiremagazine":("The Wire",["The Wire magazine"],["Music Magazine"],["London"],["UK"],"1982년 창간한 런던의 음악 매거진"),
"touchdesigner":("TouchDesigner",[],["Tech Product Company"],[],["Canada"],"Derivative의 실시간 비주얼 프로그래밍 도구"),
"typedirectors":("Type Directors Club",["TDC"],["Design Association"],["New York"],["USA"],"1946년 뉴욕에서 설립된 타이포그래피 단체"),
"wallpapermag":("Wallpaper*",["Wallpaper"],["Design Magazine"],["London"],["UK"],"1996년 창간한 런던의 디자인 매거진"),
}
# artists: (file,aliases,extra topics,cities,countries)
A={
"hwimmm":("HWIMIN",["Lee Hwi-min","이휘민","Lil Moshpit"],["Producer"],[],["South Korea"]),
"madisonbeer":("Madison Beer",[],[],[],["USA"]),
"maxcoopermax":("Max Cooper",[],["Producer"],[],["UK"]),
"mfdoom":("MF DOOM",["Daniel Dumile"],["Rapper"],[],["USA"]),
"modelactriz":("Model／Actriz",["Model/Actriz"],["Rock Band"],["New York"],["USA"]),
"partynextdoor":("PARTYNEXTDOOR",["PartyNextDoor"],[],[],["Canada"]),
"peggygou_":("Peggy Gou",["구민지","피기 구"],["DJ"],["Berlin"],["South Korea","Germany"]),
"philipglass":("Philip Glass",[],[],[],["USA"]),
"rinasonline":("Rina Sawayama",[],[],["London"],["UK","Japan"]),
"skepta":("Skepta",["Big Smoke"],["Rapper"],["London"],["UK"]),
"thesmiletheband":("The Smile",[],["Rock Band"],[],["UK"]),
"tinashenow":("Tinashe",[],[],[],["USA"]),
}
def fix(fn,ts):
    p=D+"notes/"+fn+".md"; s=open(p,encoding="utf-8").read()
    s=re.sub(r"topic:\n(?:  - .*\n)*","topic:\n"+"".join(f'  - "[[{t}]]"\n' for t in ts),s,count=1); open(p,"w",encoding="utf-8").write(s)
done=[]
for u,(fn,al,ts,ci,co,tl) in W.items():
    assert all(t in tp for t in ts),(fn,[t for t in ts if t not in tp])
    if exists(fn): print("exists",fn);continue
    r=rows[u]; mknote(fn.replace("/","／"),al,ts,norm(r[1]),website=site(r),wikis=wk(r),cities=ci,countries=co,tldr=tl); done.append((u,fn))
for u,(fn,al,ex,ci,co) in A.items():
    if exists(fn): print("exists",fn);continue
    r=rows[u]; ts=["Music Artist"]+ex
    assert all(t in tp for t in ts),(fn,)
    artist(fn.replace("/","／"),al,norm(r[1]),web=site(r),wikis=wk(r),cities=ci,countries=co); fix(fn.replace("/","／"),ts); done.append((u,fn))
import csv as c
w=c.writer(open(D+"park-done.csv","a",newline="",encoding="utf-8-sig"))
for u,fn in done: w.writerow([u,fn.replace("/","／")+".md",3])
print(len(done))
