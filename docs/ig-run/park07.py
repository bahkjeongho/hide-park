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
"starch.haus":("Starch Haus",[],["Creative Studio"],[],[],"OKOK Services가 2025년 새 웹사이트를 만든 스튜디오"),
"hidden.ny":("HIDDEN NY",["HIDDEN®","Hidden"],["Fashion Brand"],["New York"],["USA"],"뉴욕 스트리트웨어 브랜드"),
"bodyamplificationdevices":("Body Amplification Devices",["BAD"],["Fashion Brand"],["London"],["UK"],"런던의 3D 프린팅 웨어러블 브랜드"),
"monibelle":("Moni Haworth",[],["Photographer"],["Los Angeles"],["USA"],"1962년 영국 출생, 로스앤젤레스 기반 사진가이자 아티스트"),
"teoyang":("Teo Yang Studio",["TeoYang Studio","테오양 스튜디오"],["Design Studio"],["Seoul"],["South Korea"],"서울 기반 인테리어 디자인 스튜디오"),
"takahiromiyashitathesoloist":("TAKAHIROMIYASHITA TheSoloist.",["TAKAHIROMIYASHITATheSoloist."],["Fashion Brand"],["Tokyo"],["Japan"],"2010년 시작된 도쿄 패션 브랜드"),
"thedieline":("The Dieline",["Dieline"],["Design Magazine"],[],["USA"],"2007년 Andrew Gibbs가 설립한 패키징 디자인 사이트"),
"heaz":("HEAZ",["헤즈"],["Branding Agency"],["Seoul"],["South Korea"],"2003년 설립된 서울 기반 브랜딩·디자인 에이전시"),
"juliendossena":("Julien Dossena",[],["Fashion Designer","Creative Director"],["Paris"],["France"],"Rabanne의 전 아티스틱 디렉터이자 ATTO 창립자"),
"luar":("LUAR",[],["Fashion Brand"],["New York"],["USA"],"Raul Lopez의 브루클린 패션 브랜드"),
"bluemarbleparis":("Bluemarble",["BLUEMARBLE"],["Fashion Brand"],["Paris"],["France"],"Anthony Alvarez의 파리 남성복 브랜드"),
"juancp":("Juan Costa Paz",[],["Creative Director"],[],[],"LOVE 매거진 재출범을 이끈 리더"),
"nordineb":("Nordine Benotmane",["نور الدين"],["Creative Director"],[],[],"LOVE 매거진 재출범을 이끈 리더"),
"lucienpagescommunication":("Lucien Pagès Communication",[],["Marketing Agency"],["Paris","New York"],["France","USA"],"2006년 설립된 파리·뉴욕 PR 에이전시"),
"pieter_mulier":("Pieter Mulier",["PIETER MULIER"],["Creative Director","Fashion Designer"],["Paris"],["France"],"Alaïa의 크리에이티브 디렉터"),
"mastbooks":("Mast Books",[],["Book Store"],["New York"],["USA"],"2010년 문을 연 뉴욕 이스트빌리지 서점이자 갤러리"),
"climaxbooks":("Climax Books",["CLIMAX"],["Book Store"],["London"],["UK"],"Isabella Burley가 설립한 런던 독립 서점"),
"fumitoganryu":("Fumito Ganryu",["FUMITO GANRYU"],["Fashion Designer","Fashion Brand"],["Tokyo"],["Japan"],"전 Comme des Garçons Junya Watanabe 패턴사가 론칭한 일본 브랜드"),
"transwhitestudio":("Transwhite Studio",["TRANSWHITE STUDIO","非白工作室"],["Design Studio"],["Hangzhou"],["China"],"2011년 항저우에서 시작한 디자인 스튜디오"),
"winnienewyork":("Winnie New York",["WINNIE"],["Fashion Brand"],["New York"],["USA"],"2019년 Idris Balogun이 설립한 뉴욕 브랜드"),
"trippin.world":("Trippin",[],["Media"],[],[],"독립 여행 플랫폼"),
"guizioo":("Danielle Guizio",[],["Fashion Designer"],["New York"],["USA"],"뉴욕 브랜드 Guizio의 디자이너"),
"lolitajacobs":("Lolita Jacobs",[],["Creative Director"],["Paris"],["France"],"Jacobs+Talbourdet-Napoleone의 공동 창업자"),
"oliverhadleepearch":("Oliver Hadlee Pearch",[],["Photographer","Film Director"],["New York"],["USA"],"뉴욕 기반 패션 사진가이자 영화감독"),
"visual.instruments.lab":("KAIST 시각도구연구실",["Visual Instruments Lab","KAIST Visual Instruments Lab"],["Creative Research"],["Daejeon"],["South Korea"],"KAIST의 시각도구연구실"),
"visualjournal.it":("Visual Journal",[],["Design Magazine"],[],["Italy"],"Alessandro Scarpellini가 운영하는 브랜딩·그래픽 디자인 블로그"),
"kapitalglobal":("KAPITAL",[],["Fashion Brand"],[],["Japan"],"일본 패션 브랜드로 추정"),
"whitecube":("White Cube",[],["Art Gallery"],["London"],["UK"],"1993년 Jay Jopling이 설립한 런던 갤러리"),
"8division":("8DIVISION",[],["Fashion"],["Seoul"],["South Korea"],"2011년 시작된 서울 패션 셀렉트숍"),
"idologykr":("Idology",["아이돌로지"],["Culture Magazine"],[],["South Korea"],"2014년 Mimyo가 창간한 아이돌 비평 웹진"),
"yuliamahr":("Yulia Mahr",[],["Filmmaker"],["London"],["UK"],"Studio Richter Mahr의 시각예술가"),
"workbyworks.studio":("Workbyworks",["WKS"],["Graphic Design"],["New York","Shanghai"],["USA","China"],"뉴욕과 상하이를 기반으로 한 디자인 스튜디오"),
"hahouse_":("HAHOUSE",[],["Fashion"],["Seoul"],["South Korea"],"서울 이태원의 라이프스타일 스토어"),
"addictedseoul":("Addicted Seoul",[],["Fashion"],["Seoul"],["South Korea"],"2003년 압구정에서 시작한 한국 멀티브랜드 패션 리테일러"),
"edward.cuming":("Edward Cuming",["EDWARD CUMING"],["Fashion Designer"],[],["UK"],"패션 디자이너"),
"harleyweir":("Harley Weir",["HARLEY"],["Photographer"],["London"],["UK"],"AnOther와 Dazed 등에서 작업한 사진가"),
"duranlantinkyo":("Duran Lantink",[],["Fashion Designer"],["Amsterdam"],["Netherlands"],"네덜란드 패션 디자이너"),
"skeltonjohn":("John Alexander Skelton",[],["Designer"],[],["UK"],"디자이너"),
"sharnaosborne":("Sharna Osborne",[],["Photographer"],[],["UK"],"Fendi와 Dazed 등에서 작업한 사진가"),
"archived.dreams":("Archived Dreams",[],["Media"],[],[],"패션·컬처 매체"),
"linakutsovskaya":("Lina Kutsovskaya",[],["Creative Director"],[],[],"Be Good Studios의 창업자이자 크리에이티브 디렉터"),
"mafcsm":("MA Fashion (Central Saint Martins)",["MA Fashion Central Saint Martins","MA FASHION CENTRAL SAINT MARTINS"],["Academic Program","Fashion Design Program"],["London"],["UK"],"`Master\'s Program` in Fashion of Central Saint Martins"),
"henrialexanderlevy":("Henri Alexander Levy",["Henri Alexander"],["Fashion Designer"],["Paris"],["France"],"Enfants Riches Déprimés의 디자이너"),
"clim_studio":("Clim Studio",[],["Design Studio"],["Barcelona"],["Spain"],"바르셀로나의 애니메이션·디자인 스튜디오"),
"codeastudio":("Codea Studio",["CODEA"],["Design Studio"],[],[],"Codea Studio"),
"design360magazine":("Design360°",["Design360 Magazine"],["Design Magazine"],[],["China"],"2006년 창간한 중국의 이중언어 디자인 매거진"),
"neubauberlin":("Neubau",["Stefan Gandl"],["Design Studio"],["Berlin"],["Germany"],"Stefan Gandl이 설립한 베를린 디자인 스튜디오"),
"studiosaworl":("Studio Saworl",["스튜디오4월","스튜디오 4월"],["Design Studio"],["Seoul"],["South Korea"],"2006년 서울에서 시작한 디자인 스튜디오"),
}
A={
"ssion_official":("SSION",["Cody Critcheloe"],[],[],["USA"]),
"bekhyunjin_official":("백현진",["Bek Hyunjin","白鉉眞"],[],[],["South Korea"]),
}
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
for u,fn in done: w.writerow([u,fn+".md",6])
print(len(done))
