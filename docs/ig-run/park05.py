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
"waltervanbeirendonckofficial":("Walter Van Beirendonck",[],["Fashion Designer"],["Antwerp"],["Belgium"],"벨기에 패션 디자이너"),
"wiedenkennedy":("Wieden+Kennedy",["W+K"],["Advertising","Creative Agency"],["Portland"],["USA"],"1982년 포틀랜드에서 설립된 독립 광고 에이전시"),
"wolfgang_tillmans":("Wolfgang Tillmans",[],["Photographer"],["Berlin","London"],["Germany","UK"],"독일 사진가"),
"ambush_official":("AMBUSH",["AMBUSH®"],["Fashion Brand"],["Tokyo"],["Japan"],"Verbal과 Yoon Ahn이 만든 도쿄 브랜드"),
"gr10k":("GR10K",[],["Fashion Brand"],[],[],"Salomon과 협업한 의류 브랜드"),
"studio.lift_off":("LIFT-OFF",[],["Design Studio"],["Seoul"],["South Korea"],"2017년 이진우가 시작한 그래픽 디자인 듀오"),
"pablo.rochat":("Pablo Rochat",[],["Advertising"],[],[],"Goodby Silverstein & Partners 임원"),
"coteetciel":("côte&ciel",["Cote&Ciel"],["Fashion Brand"],["Paris"],["France"],"2008년 파리에서 시작한 가방 브랜드"),
"eyecannndy":("EYECANNNDY",["EYECANDY"],["Media"],[],[],"영화 연출 기법을 GIF로 정리한 레퍼런스 사이트"),
"aigaeyeondesign":("AIGA Eye on Design",["Eye on Design"],["Design Magazine"],["New York"],["USA"],"2014년 창간한 AIGA의 출판 플랫폼"),
"narantsetsegkhuyagaa":("Narantsetseg Khuyagaa",["Narantsetseg"],["Photographer"],[],["Mongolia"],"몽골 사진가"),
"thetakahiromiyashita":("TAKAHIROMIYASHITA TheSoloist.",["takahiro miyashita"],["Fashion Brand"],["Tokyo"],["Japan"],"2010년 시작된 도쿄 패션 브랜드"),
"cosmopolitankorea":("코스모폴리탄 코리아",["COSMOPOLITAN KOREA","Cosmopolitan Korea"],["Magazine"],["Seoul"],["South Korea"],"월간 여성 라이프스타일 매거진"),
"interlopemagazine":("Interlope Magazine",[],["Magazine"],[],[],"인터로프 매거진"),
"letspanicmag":("Let's Panic",[],["Fashion Magazine"],["New York"],["USA"],"뉴욕 기반 패션·아트 매거진"),
"rickowensonline":("Rick Owens",["RICK OWENS"],["Fashion Designer","Fashion Brand"],["Paris"],["France"],"1994년 로스앤젤레스에서 시작한 패션 브랜드, 본사는 파리"),
"bureaubetak":("Bureau Betak",[],["Production Company"],["Paris"],["France"],"Alexandre de Betak이 설립한 패션쇼·이벤트 프로덕션"),
"unfun_studio":("unfun",[],["Design Studio"],["Nuremberg"],["Germany"],"2011년 뉘른베르크에서 시작한 디자인 스튜디오"),
"lusionltd":("Lusion",["Lusion™"],["Creative Studio","Digital Design"],["Bristol"],["UK"],"Edan Kwan이 설립한 브리스톨 기반 디지털·3D 스튜디오"),
"omni.type":("Omnitype",[],["Type Foundry"],["Lausanne"],["Switzerland"],"2017년 로잔에서 시작한 디지털 타입 파운드리"),
"wesa.seoul":("WeSA",[],["Music Festival"],["Seoul"],["South Korea"],"2014년 시작된 사운드 아트 페스티벌"),
"mtl.co.kr":("mtl",["More Than Less"],["Creative Company"],["Seoul"],["South Korea"],"서울 한남동의 라이프스타일 콘텐츠 브랜드"),
"hakgojaegallery":("학고재 갤러리",["Hakgojae Gallery"],["Art Gallery"],["Seoul"],["South Korea"],"1988년 서울에서 문을 연 갤러리"),
"goyowear.official":("GOYOWEAR",[],["Fashion Brand"],[],["South Korea"],"2020년 시작한 한국 아웃도어 브랜드"),
"helixclothing_":("HELIX CLOTHING",["Helix Clothing"],["Fashion Brand"],[],["South Korea"],"2021년 시작한 한국 남성복 브랜드"),
"jeongli_official":("JEONGLI",[],["Fashion Brand"],["Seoul"],["South Korea"],"2019년 서울에서 시작한 디자이너 브랜드"),
"viscose_journal":("Viscose Journal",[],["Journal","Fashion Magazine"],["Copenhagen","New York"],["Denmark","USA"],"2021년 창간한 패션 비평지, 편집장 Jeppe Ugelvig"),
"habokorea":("HABO",["HABO Korea","하보"],["Music Platform"],[],["South Korea"],"음악과 공간을 연결하는 서비스"),
"textpress.kr":("텍스트 프레스",["Text Press"],["Publishing Compnay"],[],["South Korea"],"정동규 대표의 한국 1인 출판사"),
"dformichetti":("Domenico Formichetti",["DOMENICO FORMICHETTI"],["Fashion Designer"],["Milan"],["Italy"],"밀라노 디자이너, PDF 브랜드 설립자"),
"andotherstories":("& Other Stories",["And Other Stories"],["Fashion Brand"],[],["Sweden"],"H&M 그룹의 여성 패션 브랜드"),
"puebco_japan":("PUEBCO",["プエブコ"],["Design"],[],["Japan"],"2007년 Hirotaka Tanaka가 설립한 일본 라이프스타일 브랜드"),
"alastairmckimm":("Alastair McKimm",["alastair mckimm"],["Stylist","Creative Director"],["New York"],["USA"],"뉴욕 스타일리스트이자 크리에이티브 디렉터"),
"huxley":("Huxley",[],["Management Agency"],["London"],["UK"],"런던 기반 탤런트·브랜드 에이전시"),
"laurids.gallee":("Laurids Gallée",[],["Designer"],["Rotterdam"],["Netherlands"],"로테르담 기반 오스트리아 디자이너"),
"gmbh_official":("GmbH",[],["Fashion Brand"],["Berlin"],["Germany"],"Serhat Isik과 Benjamin Alexander Huseby의 베를린 패션 레이블"),
"ilovecreatives":("ilovecreatives",["ilovecreatives.com"],["Media"],["Los Angeles"],["USA"],"LA 기반 크리에이티브 뉴스레터·플랫폼"),
"maansun_com":("Maansun",["만순"],["Music Platform"],[],["South Korea"],"한국 독립 음악·문화 디지털 스토어"),
"reeditionmag":("Re-Edition Magazine",[],["Fashion Magazine"],[],[],"패션·아트 매거진"),
"wk_ldn":("Wieden+Kennedy London",["W+K London"],["Advertising","Creative Agency"],["London"],["UK"],"1997년 설립된 Wieden+Kennedy 런던 사무소"),
"hwfstudio":("하우풀스튜디오",["HOWFULSTUDIO","Howful Studio"],["Design Studio"],["Seoul"],["South Korea"],"2018년 서울에서 시작한 디자인 스튜디오"),
"studiofeixen":("Studio Feixen",[],["Design Studio"],["Lucerne"],["Switzerland"],"Felix Pfäffli가 설립한 루체른 디자인 스튜디오"),
"somethingspecialstudios":("Something Special Studios",["Something Special Studios*"],["Creative Agency"],["New York","Los Angeles"],["USA"],"뉴욕과 로스앤젤레스의 크리에이티브 에이전시"),
"jealous_london":("Jealous Gallery & Print Studio",["Jealous"],["Art Gallery"],["London"],["UK"],"2008년 Dario Illari가 설립한 런던 갤러리·프린트 스튜디오"),
"cactusjack":("Cactus Jack",[],["Record Label","Fashion Brand"],[],["USA"],"Travis Scott의 레이블 및 의류 브랜드"),
"a24music":("A24 Music",[],["Record Label"],["New York"],["USA"],"A24의 음악 부문"),
}
A={
"xaviersobased":("Xaviersobased",["Xavier"],["Rapper","Producer"],["New York"],["USA"]),
"marceleverette":("XXYYXX",["Marcel Everett"],["Producer"],["Orlando"],["USA"]),
"kraejiyaeji":("Yaeji",["예지"],["DJ","Producer"],[],["USA"]),
"yunglean2001":("Yung Lean",[],["Rapper"],["Stockholm"],["Sweden"]),
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
for u,fn in done: w.writerow([u,fn+".md",4])
print(len(done))
