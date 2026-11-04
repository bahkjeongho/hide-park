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
"lippincottbrand":("Lippincott",[],["Branding Agency"],["New York"],["USA"],"1943년 설립된 브랜드 컨설팅 회사, Oliver Wyman 소속"),
"markgong_official":("Markgong",["MARKGONG","龔子銘"],["Fashion Brand"],[],["China"],"Mark Gong이 2018년 설립한 중국 패션 브랜드"),
"ludovicdesaintsernin":("Ludovic de Saint Sernin",[],["Fashion Designer","Fashion Brand"],["Paris"],["France"],"프랑스 패션 디자이너"),
"lvmhprize":("LVMH Prize",["LVMH PRIZE"],["Award"],["Paris"],["France"],"2013년 시작된 젊은 디자이너 상"),
"macguffinmagazine":("MacGuffin",["MacGuffin - The Life of Things"],["Design Magazine"],["Amsterdam"],["Netherlands"],"암스테르담의 디자인·공예 매거진"),
"maisonalaia":("Alaïa",["ALAÏA","Maison Alaïa","Azzedine Alaïa"],["Fashion Brand"],["Paris"],["France"],"Azzedine Alaïa가 설립한 패션 하우스"),
"mazarinegroup":("Mazarine Group",["MAZARINE GROUP"],["Creative Group"],["Paris"],["France"],"1993년 Paul-Emmanuel Reiffers가 설립한 파리의 커뮤니케이션 그룹"),
"middleplanemagazine":("Middle Plane",[],["Fashion Magazine"],["London"],["UK"],"2018년 런던에서 창간한 아트·패션 매거진"),
"mingalondon":("Minga London",[],["Fashion Brand"],["London"],["UK"],"2018년 시작된 윤리적 패션 브랜드"),
"marfajournal":("MARFA Journal",["MARFA","Marfamily"],["Journal"],["Yekaterinburg"],["Russia"],"예카테린부르크에서 시작한 저널, 현재 Marfamily로 개명"),
"newinc":("NEW INC",[],["Art Platform"],["New York"],["USA"],"뉴 뮤지엄의 문화·기술 인큐베이터"),
"poeticallypunk":("Angelo Flaccavento",["angelo flaccavento"],["Fashion Critique"],[],["Italy"],"패션 저널리스트이자 큐레이터"),
"nssmagazine":("nss magazine",["nssmagazine"],["Fashion Magazine"],[],["Italy"],"이탈리아 패션·스트리트웨어 매체"),
"selfservicemagazine":("Self Service Magazine",[],["Fashion Magazine"],["Paris"],["France"],"파리의 패션·문화 연간지"),
"okaydevs":("Okay Dev",["OkayDev"],["Programmer"],[],[],"Eric Van Holtz가 만든 크리에이티브 개발자 커뮤니티"),
"r13":("R13",[],["Fashion Brand"],["New York"],["USA"],"2009년 Chris Leba가 설립한 뉴욕 데님 브랜드"),
"owhyworks":("Owhyworks",["오와이웍스"],["Design Studio"],["Seoul"],["South Korea"],"크리에이티브 디렉터 연철민의 서울 디자인 스튜디오"),
"doxpeter":("Peter Do",[],["Fashion Designer","Creative Director"],["New York"],["USA"],"Helmut Lang의 크리에이티브 디렉터를 지낸 디자이너"),
"sacaiofficial":("sacai",[],["Fashion Brand"],["Tokyo"],["Japan"],"일본 패션 브랜드"),
"nutype.info":("누타입",["Nutype"],["Type Foundry"],[],["South Korea"],"한국 타입 파운드리"),
"muglerofficial":("Mugler",["MUGLER"],["Fashion Brand"],["Paris"],["France"],"1974년 Thierry Mugler가 설립한 패션 하우스"),
"schiaparelli":("Schiaparelli",[],["Fashion Brand"],["Paris"],["France"],"패션 하우스"),
"shushu__tong":("SHUSHU／TONG",["shushutongstudio","SHUSHU/TONG"],["Fashion Brand"],["Shanghai"],["China"],"2015년 Liushu Lei와 Yutong Jiang가 시작한 상하이 브랜드"),
"ksawerykomputery":("Ksawery Komputery",["Ksawery Kirklewski"],["Programmer"],[],["Poland"],"아티스트이자 크리에이티브 코더 프로젝트"),
"uns__nstudio":("Unseen Studio",[],["Digital Design"],["Bristol"],["UK"],"브리스톨 기반 디지털·모션 스튜디오"),
"grillitype":("Grilli Type",["Grilli Type Foundry"],["Type Foundry"],["Lucerne"],["Switzerland"],"2009년 루체른에서 설립한 스위스 타입 파운드리"),
"commissionofficial":("Commission",[],["Fashion Brand"],["New York"],["USA"],"2018년 시작된 뉴욕 레이블"),
"thomkrom_official":("thom／krom",["thom/krom"],["Fashion Brand"],[],["Germany"],"2009년 Thomas Kromik이 시작한 독일 패션 레이블"),
"mikemeire":("Mike Meiré",[],["Art Director"],["Cologne"],["Germany"],"쾰른 기반 아트 디렉터, Meiré und Meiré 설립"),
"biggamedesign":("BIG-GAME",[],["Design Studio"],["Lausanne"],["Switzerland"],"2004년 로잔에서 설립한 디자인 스튜디오"),
"svrnshop":("SVRN",["SVRN®"],["Fashion"],["Chicago","San Francisco"],["USA"],"시카고와 샌프란시스코의 편집숍"),
"takeninagawa":("Take Ninagawa",[],["Art Gallery"],["Tokyo"],["Japan"],"2008년 문을 연 도쿄 갤러리"),
"thedesignersrepublic":("The Designers Republic",["The Designers Republic™"],["Design Studio"],["Sheffield"],["UK"],"셰필드 기반 그래픽 디자인 스튜디오"),
"figma":("Figma",[],["Tech Product Company"],["San Francisco"],["USA"],"디자인 협업 도구를 만드는 회사"),
"on":("On",["On Running"],["Fashion Brand"],["Zurich"],["Switzerland"],"스위스 러닝 브랜드"),
"rokhofficial":("Rokh",["ROKH"],["Fashion Brand"],["London"],["UK"],"2016년 Rok Hwang이 설립한 런던 브랜드"),
"imprimeriedumarais":("Imprimerie du Marais",[],["Design"],["Paris"],["France"],"1971년 설립된 파리 인쇄소"),
"faustseoul":("FAUST",["Faust Seoul"],["Promoter"],["Seoul"],["South Korea"],"이태원의 테크노 클럽"),
"spacemue_seoul":("MUE",["Space MUE"],["Fashion"],["Seoul"],["South Korea"],"서울 강남의 멀티 브랜드 스토어"),
"vurt_seoul":("vurt",["vurt."],["Promoter"],["Seoul"],["South Korea"],"합정의 언더그라운드 테크노 클럽"),
"lacreole_":("La Creole",["LA CREOLE + CREOLE SOUL","Creole Soul"],["Promoter"],["Paris"],["France"],"파리의 파티 컬렉티브"),
"studiorichtermahr":("Studio Richter Mahr",[],["Creative Studio"],[],["UK"],"Max Richter와 Yulia Mahr가 세운 옥스퍼드셔의 멀티아트 스튜디오"),
"__dreamspaces":("dreamspaces",["Isabelle Angèle Wuilloud"],["Art Platform"],["Vienna"],["Austria"],"Isabelle Angèle Wuilloud가 운영하는 디자인 플랫폼"),
"commedesgarconsseoul":("COMME des GARÇONS SEOUL",["Comme des Garçons Seoul"],["Fashion"],["Seoul"],["South Korea"],"2010년 한남동에 문을 연 플래그십 스토어"),
"vbuntitled":("Vanessa Beecroft",[],["Photography"],[],["Italy"],"이탈리아 출신 퍼포먼스 아티스트"),
"hedmayner":("Hed Mayner",["HED MAYNER"],["Fashion Designer","Fashion Brand"],[],["Israel"],"2015년 설립한 이스라엘 디자이너"),
"soapseoul":("Soap Seoul",["Soap"],["Promoter"],["Seoul"],["South Korea"],"2017년 이태원에 문을 연 클럽"),
"raullopez":("Raul Lopez",["RAUL LOPEZ"],["Fashion Designer"],["New York"],["USA"],"LUAR 디자이너이자 Hood By Air 공동 창업자"),
"zetafonts":("Zetafonts",["Zetafonts® Type Foundry"],["Type Foundry"],["Florence"],["Italy"],"2001년 피렌체에서 설립한 타입 파운드리"),
"togaarchives":("TOGA",["TOGA ARCHIVES"],["Fashion Brand"],["Tokyo"],["Japan"],"일본 패션 브랜드"),
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
for u,fn in done: w.writerow([u,fn+".md",8])
print(len(done))
