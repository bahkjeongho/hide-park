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
"maison_kimhekim":("KIMHĒKIM",["Kimhekim","Maison Kimhekim"],["Fashion Brand"],[],[],"Kiminte Kimhekim이 설립한 패션 브랜드"),
"cecileparavina":("Cécile Paravina",["Cecile Paravina"],["Stylist"],[],["France"],"메이크업 아티스트"),
"cavempt":("Cav Empt",["CAVEMPT","C.E"],["Fashion Brand"],["Tokyo"],["Japan"],"일본 스트리트웨어 레이블"),
"wkorea":("W Korea",["더블유 코리아"],["Fashion Magazine"],["Seoul"],["South Korea"],"2005년 창간한 두산 발행 패션 매거진"),
"charlesdevilmorin":("Charles de Vilmorin",[],["Fashion Designer"],["Paris"],["France"],"프랑스 패션 디자이너"),
"laurapitcher":("Laura Pitcher",[],["Writer"],["New York"],["USA"],"뉴욕 기반 패션·컬처 작가, Dazed US 시니어 라이터"),
"media.work":("Media.Work",[],["Design Studio"],[],[],"디자인 스튜디오"),
"antoniberlin":("antoni",["antoni Berlin","antoni_"],["Creative Agency"],["Berlin"],["Germany"],"André Kemper와 Tonio Kröger가 설립한 에이전시"),
"koreansocietyoftypography":("한국타이포그라피학회",["Korean Society of Typography"],["Design Association"],[],["South Korea"],"저널 LetterSeed를 발행하는 타이포그래피 학회"),
"elizavetaporodina":("Elizaveta Porodina",[],["Photographer"],["Munich"],["Germany"],"뮌헨 기반 사진가"),
"magazine.filo":("FILO",["필로"],["Magazine"],[],["South Korea"],"영화 비평 격월간지로 추정되는 매거진"),
"aladinbook":("알라딘",["알라딘 인터넷서점","Aladin"],["Book Store"],[],["South Korea"],"1998년 창업한 인터넷 서점"),
"castorfleuriste":("Louis-Géraud Castor",["Castor Fleuriste"],["Entrepreneur"],["Paris"],["France"],"파리의 플로리스트 Castor Fleuriste 창립자"),
"matibooks":("도서출판 마티",["Mati Books"],["Publishing Compnay"],[],["South Korea"],"정희경 대표가 이끄는 출판사"),
"ninamcneely":("Nina McNeely",[],["Film Director"],[],["USA"],"안무가이자 감독"),
"optimisticrunners":("Optimistic Runners",["Optimistic Runners™"],["Fashion Brand"],["Berlin"],["Germany"],"2023년 베를린에서 시작한 러닝 브랜드이자 커뮤니티"),
"coyseio":("COYSEIO",[],["Fashion Brand"],["Seoul"],["South Korea"],"서울 기반 의류 브랜드"),
"lamodeenimages":("La Mode en Images",["LA MODE EN IMAGES"],["Production Company"],["Paris"],["France"],"Mazarine 그룹 소속 패션쇼 제작사"),
"seoulmediacitybiennale":("서울미디어시티비엔날레",["Seoul Mediacity Biennale"],["Art Platform"],["Seoul"],["South Korea"],"서울시립미술관이 주관하는 미디어아트 비엔날레"),
"abc_artbookinchina":("abC art book in China",["abC_art book in China"],["Art Platform"],[],["China"],"중국의 아트북 페어"),
"scr_radio":("Seoul Community Radio",["SCR"],["Radio"],["Seoul"],["South Korea"],"2016년 Rich SCR이 설립한 서울 온라인 전자음악 라디오"),
"houseofhighlights":("House of Highlights",[],["Media"],[],["USA"],"Omar Raja가 설립한 스포츠 영상 브랜드"),
"danielsannwald":("Daniel Sannwald",[],["Photographer","Video Director"],[],["Germany"],"독일 사진가이자 영상 감독"),
"niceworkshop_":("NICEWORKSHOP",[],["Design Studio"],["Seoul"],["South Korea"],"서울 기반 실험 디자인 스튜디오"),
"moreorlessmag":("More Or Less",[],["Fashion Magazine"],[],[],"Jaime Perlman이 창간한 패션 매거진"),
"bae.minkee":("배민기",["Minkee Bae","Bae Min Ki"],["Fashion"],[],["South Korea"],"Valuable Artist Agency 소속 모델"),
"juliannn_song":("Julian Song",["Song Wanjie"],["Photographer"],[],["China"],"중국 북동부 출신 사진가"),
"empty.seoul.kr":("무신사 엠프티",["MUSINSA EMPTY"],["Fashion Brand"],["Seoul"],["South Korea"],"무신사의 편집숍 브랜드"),
"kusikohc":("KUSIKOHC",[],["Fashion Brand"],[],["South Korea"],"조기석 작가의 패션 브랜드"),
"alainpaul":("ALAINPAUL",["Alain Paul"],["Fashion Brand"],["Paris"],["France"],"2023년 파리에서 Alain Paul과 Luis Philippe가 설립한 브랜드"),
"blumarine":("Blumarine",[],["Fashion Brand"],[],["Italy"],"1977년 Anna Molinari가 설립한 이탈리아 패션 하우스"),
"magliano.insta":("Magliano",[],["Fashion Brand"],["Bologna"],["Italy"],"Luca Magliano가 2017년 볼로냐에서 시작한 레이블"),
"ottolinger":("Ottolinger",["OTTOLINGER"],["Fashion Brand"],["Berlin"],["Germany"],"Christa Bösch와 Cosima Gadient의 베를린 레이블"),
"objekteunserertage":("OUT",["Objekte unserer Tage"],["Furniture Design"],["Berlin"],["Germany"],"베를린의 가구 브랜드"),
"hejishin":("Heji Shin",[],["Photographer"],["New York","Berlin"],["USA","Germany"],"뉴욕과 베를린을 오가는 사진가"),
"oddamagazine":("ODDA",["ODDA Magazine"],["Fashion Magazine"],[],[],"2012년 David Martin이 창간한 패션 매거진"),
"pinupmagazine":("PIN–UP",["PIN-UP","PIN–UP®"],["Magazine"],["New York"],["USA"],"2006년 뉴욕에서 창간한 건축·디자인 매거진"),
"qualitymeatscreative":("Quality Meats",["Quality Meats Creative"],["Creative Agency"],[],[],"크리에이티브 에이전시"),
"cakeshopseoul":("Cakeshop",["케이크샵"],["Promoter"],["Seoul"],["South Korea"],"Samuel Swanson이 설립한 이태원의 언더그라운드 클럽"),
"chenpengstudio":("CHENPENG",["Chen Peng"],["Fashion Brand"],[],[],"Peng Chen의 패션 레이블"),
"refrigiwear1954.kr":("RefrigiWear",["RefrigiWear Korea","RefrigiWear® korea"],["Fashion Brand"],[],["USA"],"1954년 시작된 미국 워크웨어 브랜드"),
"schoolofartsgent":("KASK & Conservatorium",["School of Arts Ghent"],["Art School"],["Ghent"],["Belgium"],"겐트의 예술학교"),
"sfpc.study":("School for Poetic Computation",["SFPC"],["Art School"],["New York"],["USA"],"2013년 뉴욕에서 시작한 시적 컴퓨팅 학교"),
"creativecodeart":("Creative Code Art",[],["Art Platform"],[],[],"Shotgun에 등록된 크리에이티브 코드 아트 주최자"),
"sibf_official":("서울국제도서전",["SIBF","Seoul International Book Fair"],["Culture Festival"],["Seoul"],["South Korea"],"서울에서 열리는 국제도서전"),
"danielleguizio":("Guizio",["GUIZIO","Danielle Guizio"],["Fashion Brand"],["New York"],["USA"],"Danielle Guizio의 2014년 뉴욕 브랜드"),
"encore.label":("Encore Label",["ENCORE"],["Record Label"],[],[],"예술 레이블"),
"squama.rec":("Squama Recordings",[],["Record Label"],["Munich"],["Germany"],"2019년 뮌헨에서 시작한 재즈 레이블"),
}
A={
"maartenvos_":("Maarten Vos",[],["Producer"],[],["Netherlands"]),
"freerangeneighborkid":("FRNK",["박진수","Jinsu Park"],["Producer"],[],["South Korea"]),
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
for u,fn in done: w.writerow([u,fn+".md",5])
print(len(done))
