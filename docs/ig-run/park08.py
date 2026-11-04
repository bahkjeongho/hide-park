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
"thomas_studio_official":("Thomas Studio",["Thomas Studio™"],["Design Studio"],["Seoul"],["South Korea"],"2015년 시작된 서울 패키지 디자인 사무소"),
"veig.design":("VEIG",["VEIG DESIGN"],["Design Agency"],["Seoul"],["South Korea"],"서울 기반 브랜드·모션 디자인 컨설턴시"),
"coach":("Coach",[],["Fashion Brand"],["New York"],["USA"],"미국 패션 브랜드"),
"cca_comdesign":("Communication Design (California College of the Arts)",["CCA Communication Design"],["Academic Program","Graphic Design Program"],["San Francisco"],["USA"],"`Bachelor's Program` in Communication Design of [[California College of the Arts]]"),
"yuka_hirac":("Yuka Hirac",["ユカハイラック"],["Stylist"],["Tokyo"],["Japan"],"도쿄 기반 아티스트이자 메이크업 아티스트"),
"brody_associates":("Brody Associates",[],["Design Studio"],["London"],["UK"],"Neville Brody의 런던 디자인 스튜디오"),
"ifucktokyo":("I FUCK TOKYO",["IFUCKTOKYO","I FUCK TOKYO!"],["Photography"],["Tokyo"],["Japan"],"Kido Mafon의 도쿄 서브컬처 사진 프로젝트이자 파티"),
"entire_studios":("Entire Studios",["ES"],["Fashion Brand"],["Los Angeles"],["USA"],"2020년 Sebastian Hunt와 Dylan Richards Diaz가 설립한 로스앤젤레스 브랜드"),
"apocstore":("APOC Store",["APOC STORE"],["Fashion"],[],[],"2020년 Ying Suen과 Jules Volleberg가 설립한 온라인 편집숍"),
"francescalakeofficial":("Francesca Lake",["FRANCESCA LAKE"],["Fashion Designer"],["London"],["UK"],"자메이카 출신 패션 디자이너, Central Saint Martins 출신"),
"ayham_hassan_99":("Ayham Hassan",["Ayham Hassan Musleh"],["Fashion Designer"],["London"],["UK"],"팔레스타인 출신 패션 디자이너, Central Saint Martins 재학"),
"whodecideswar":("Who Decides War",["W H O D E C I D E S W A R"],["Fashion Brand"],["New York"],["USA"],"뉴욕 패션 브랜드"),
"egon_lab":("Egonlab",["EGONLAB"],["Fashion Brand"],[],[],"패션 레이블"),
"smut_press":("SMUT Press",[],["Publishing Compnay"],["Dublin","London"],["Ireland","UK"],"2022년 시작된 더블린·런던의 퀴어 출판 프로젝트"),
"weirdcoretv":("Weirdcore",["w3iRdc0r3"],["Visual Director"],["London"],["UK"],"익명의 비주얼 아티스트"),
"jackdavisonphoto":("Jack Davison",[],["Photographer"],["London"],["UK"],"에식스 출신 사진가"),
"isabellaburley":("Isabella Burley",[],["Editor-in-Chief","Entrepreneur"],["London"],["UK"],"전 Dazed 편집장이자 Climax Books 설립자"),
"hwawon_mediabus":("화원",["花園","Hwawon"],["Publishing Compnay"],["Seoul"],["South Korea"],"서울 디자인 출판사 Mediabus의 임프린트"),
"designkorea.official":("Design Korea",["DESIGN KOREA"],["Design Festival"],["Seoul"],["South Korea"],"KIDP가 주관하는 디자인 박람회"),
"swna.office":("SWNA",[],["Design Studio"],["Seoul"],["South Korea"],"2009년 Sukwoo Lee가 설립한 서울 디자인 오피스"),
"designhistory.kr":("한국디자인사학회",["Designhistory Kr","Korean Society of Design History"],["Design Association"],[],["South Korea"],"한국디자인사학회"),
"studiopaack":("StudioPaack",["StudioPaack™"],["Creative Studio"],["Paris"],["France"],"2016년 파리에서 시작한 크리에이티브 스튜디오"),
"mariotsai_studio":("Mario Tsai Studio",[],["Design Studio"],["Hangzhou"],["China"],"2014년 항저우에서 시작한 디자인 스튜디오"),
"alternativespaceloop":("대안공간 루프",["ALT SPACE LOOP","Alternative Space Loop"],["Art Platform"],["Seoul"],["South Korea"],"1999년 시작된 서울의 비영리 대안공간"),
"futuraseoul":("푸투라서울",["Futura Seoul"],["Art Platform"],["Seoul"],["South Korea"],"2024년 북촌에 문을 연 아트 스페이스"),
"eamesinstitute":("Eames Institute",[],["Museum"],[],["USA"],"Ray와 Charles Eames의 유산을 다루는 비영리 기관"),
"sean.mcgirr":("Seán McGirr",["Sean McGirr"],["Fashion Designer","Creative Director"],["London"],["Ireland","UK"],"Alexander McQueen의 크리에이티브 디렉터를 지낸 아일랜드 디자이너"),
"endclothing":("END.",["END Clothing"],["Fashion"],[],["UK"],"영국 패션 리테일러"),
"roahiking":("ROA",["ROA Hiking"],["Fashion Brand"],["Florence"],["Italy"],"2015년 시작된 이탈리아 아웃도어 브랜드"),
"mm6maisonmargiela":("MM6 Maison Margiela",[],["Fashion Brand"],["Paris"],["France"],"Margiela의 컨템포러리 라인"),
"willychavarria":("Willy Chavarria",["WILLY CHAVARRIA"],["Fashion Designer","Fashion Brand"],["New York"],["USA"],"멕시코계 미국 패션 디자이너"),
"seoul_recordfair":("서울레코드페어",["Seoul Record Fair"],["Music Festival"],["Seoul"],["South Korea"],"2011년 시작된 음반 축제"),
"alyxstudio":("1017 ALYX 9SM",["ALYX"],["Fashion Brand"],[],["USA"],"2015년 Matthew M. Williams가 시작한 패션 브랜드"),
"namesak3":("NAMESAKE",[],["Fashion Brand"],["Paris"],["France"],"세 형제와 아버지가 만든 패션 브랜드"),
"allcapstype":("aLLcAPS",["AllCaps","ALLCAPS"],["Type Foundry"],[],["Czech Republic"],"2018년 Ondřej Báchor와 Jan Novák이 설립한 타입 디자인 스튜디오"),
"magmajournal":("MAGMA",[],["Journal"],[],[],"미술 문화 저널"),
"fotografiska":("Fotografiska",[],["Museum"],["Stockholm"],["Sweden"],"2010년 스톡홀름에서 시작한 사진 미술관 네트워크"),
"friendsoffriends":("Freunde von Freunden",["Friends of Friends"],["Magazine"],["Berlin"],["Germany"],"2009년 베를린에서 시작한 온라인 매거진"),
"bruder.works":("BRUDER",["Art & Design by BRUDER"],["Graphic Designer"],["Seoul"],["South Korea"],"정규혁과 유유리의 서울 그래픽 디자인 듀오"),
"ypc.seoul":("Yellow Pen Club",["yellowpenclub","옐로우 펜 클럽"],["Art Collective"],["Seoul"],["South Korea"],"2016년 시작된 서울의 미술 글쓰기 집단"),
"satisfyrunning":("SATISFY",["SATISFY Running"],["Fashion Brand"],["Paris"],["France"],"2015년 Brice Partouche가 설립한 파리 러닝 브랜드"),
"cmmawear":("CMMAWEAR",["C M M A W E A R"],["Fashion Brand"],[],[],"2020년 Giz Moon과 Val Choi가 시작한 스트리트웨어"),
"harvarddesignpress":("Harvard Design Press",[],["Publishing Compnay"],["Cambridge"],["USA"],"하버드 GSD의 출판 임프린트"),
"studioga.ze":("STUDIO GA.ZE",["GA•ZE","스튜디오 가제"],["Video Production"],["Seoul"],["South Korea"],"서울 기반 영상 제작팀"),
"welcomerecords_seoul":("Welcome Records",["Welcome Records est. 2019"],["Book Store"],["Seoul"],["South Korea"],"서울 용산의 레코드숍"),
"herzogdemeuron":("Herzog & de Meuron",[],["Architecture Firm"],["Basel"],["Switzerland"],"1978년 바젤에서 설립된 건축사무소"),
"hommemade":("Hommemade",["hOMMEMADE"],["Furniture Design"],[],["USA"],"A$AP Rocky의 가구·홈 브랜드"),
"airtomyearth":("Jamie-Maree Shipton",[],["Art Director","Stylist"],["London"],["UK"],"멜버른 출신 런던 기반 아트디렉터이자 스타일리스트"),
"itsnicethat":("It's Nice That",[],["Media"],["London"],["UK"],"2007년 Will Hudson과 Alex Bec이 설립한 크리에이티브 컬처 웹사이트"),
"leeummuseumofart":("리움미술관",["Leeum Museum of Art","Leeum","호암미술관","Hoam Museum of Art"],["Museum"],["Seoul"],["South Korea"],"2004년 삼성문화재단이 개관한 사립 미술관"),
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
for u,fn in done: w.writerow([u,fn+".md",7])
print(len(done))
