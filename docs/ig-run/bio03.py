import csv,json,os,urllib.parse as up
from rec import mknote,D
S="/private/tmp/claude-503/-Users-parkjeongho-Developer-Hide-Park/873d87db-505a-43d5-8e4c-ad9523e833cb/scratchpad/"
R={o['u']:o for o in json.load(open(S+"f_200.json"))}
BATCH=3
def site(u):
    p=up.urlparse(R[u]['url']); return f"{p.scheme}://{p.netloc}/"
# u: (파일명, aliases, topics, cities, countries, tldr, website(None=사이트 루트, ''=없음))
N={
"twangstagram":("Twang",["트왱","Twang 트왱"],["Producer"],["Seoul"],["South Korea"],"서울 기반 음악 프로듀서이자 스튜디오 디렉터",None),
"form.community":("FORM",[],["Fashion Retail"],[],[],"세컨핸드 럭셔리를 다루는 플랫폼",None),
"codymarian_":("Cody Marian Turple",["Cody Marian","cody"],["Creative Director","3D Artist"],[],[],"2D/3D 디자인과 애니메이션을 다루는 디지털 아티스트이자 크리에이티브 디렉터",None),
"mut.magazine":("MUT Magazine",["MUT magazine"],["Magazine"],[],[],"K-pop을 비롯한 문화를 다루는 매거진",None),
"typicallife.curation":("TYPICALLIFE.CURATION",["typicallife.curation"],["Fashion Retail"],[],["South Korea"],"디자이너 브랜드와 빈티지를 소개하는 편집숍",None),
"studioapt.kr":("Studio Apt",["스튜디오 에이피티","브랜딩 스튜디오 에이피티"],["Branding Agency"],[],["South Korea"],"시각 언어로 브랜드를 정의하는 브랜딩 스튜디오",None),
"ijpowell":("Isaac Powell",[],["Designer"],[],["UK"],"2014년부터 브랜드와 디지털 전반에서 일해 온 독립 디자인 디렉터",None),
"teamvirals":("TEAMVIRALS",["팀바이럴스"],["Design Studio"],[],["South Korea"],"폭넓은 영역의 디자인 프로젝트를 다루는 디자인 팀",None),
"tedo.seoul":("tedo",["태도"],["Design Agency"],["Seoul"],["South Korea"],"브랜딩, 그래픽, 디지털, 포스터 디자인을 제공하는 디자인 에이전시",None),
"renatakats":("Renata Kats",["Riri"],["Photographer","Creative Director"],[],[],"사진가이자 크리에이티브 디렉터",None),
"cactusdigital":("Cactus Digitale",["CACTUS+","CACTUS DIGITALE"],["Creative Agency"],["Milan","Paris"],[],"브랜드 전략, 에디토리얼 디렉션, 패션·뷰티 캠페인을 다루는 밀라노·파리 럭셔리 크리에이티브 에이전시",None),
"vcode_official":("VCODE",["브이코드 스튜디오","VCODE STUDIO"],["Design Studio"],["Seoul"],["South Korea"],"코드와 디자인을 융합해 모션그래픽을 만드는 서울 스튜디오",None),
"the_megaforce":("MEGAFORCE",[],["Video Director"],[],["France"],"뮤직비디오와 캠페인을 연출하는 프랑스 디렉터 그룹",None),
"keep.us.weird":("KEEPUSWEIRD",["K.U.W","Keep Us Weird"],["Video Production"],[],[],"영상 제작을 기반으로 한 크리에이티브 컬렉티브",None),
"maxwinter.studio":("Studio Max Winter",["Max Winter"],["Design Studio"],[],[],"브랜드, 제품, 문화를 위한 이미지와 그래픽을 만드는 스튜디오",None),
"geoffreybsmall":("Geoffrey B. Small",[],["Fashion Designer"],[],[],"1979년부터 손으로 옷을 만들어 온 패션 디자이너",None),
"servicesgeneraux":("Services Généraux",["SERVICES GÉNÉRAUX"],["Creative Studio"],[],[],"Antoine과 Valentin 듀오가 이끄는 이미지 메이킹 스튜디오",None),
"serifa":("SERIFA",[],["Creative Studio"],[],[],"Nastassja Abel과 Christian Otto의 협업 아트 프랙티스이자 스튜디오",None),
"salinesweat":("Stephen Kim",[],["Art Director"],[],[],"W+K와 ORKR 등에서 일한 아트 디렉터",None),
"practice.inc":("Practice",[],["Branding Agency"],[],[],"웰니스, 컬처, 컨슈머 스타트업을 위한 브랜드 빌딩 펌",None),
"a_perspective_mag":("A PERSPECTIVE",["A PERSPECTIVE MAGAZINE"],["Media Platform"],[],["South Korea"],"크리에이터와 크리에이티브 리더의 일, 삶, 쉼에 대한 관점을 담는 인터뷰 기반 콘텐츠 플랫폼",None),
"jinandpark":("Jin & Park",["Jin and Park"],["Designer"],[],["South Korea"],"Jin dallae와 Park woohyuk의 아트·디자인 듀오",None),
"spread.works":("Spreadworks",["SPREADWORKS","SPREAD WORKS"],["Brand Consultancy"],[],[],"브랜딩을 중심에 두고 문제를 푸는 브랜딩 컨설턴트",None),
"juliahobbs_":("Julia Hobbs",["JULIA HOBBS"],["Fashion Journalism"],[],[],"Vogue의 수석 기고 패션 피처 에디터","" ),
}
CHK={
"sophiabrinkgerd":"베를린의 크리에이티브 프랙티스라는 설명뿐, 분야 불명",
"erictimothycarlson":"아트·북·디자인·인쇄 등 작업 목록뿐, 직업 불명",
"summerskythunderstorm":"Roh-haus는 비주얼 아트 팀, 맞는 topic 없음",
"carlos___tv":"바이오 링크가 자동화 단축키/Patreon 페이지, 대상 성격 불명",
"dnmt.archive":"DNMT Inc 소개 문구만 있음, 분야 불명",
"work_louder":"크리에이티브 도구(키보드) 회사, 맞는 topic 없음",
"ngr.ev":"작업 모음 인덱스 사이트, 분야 불명",
"drezzdon":"본문 정보 없음",
"9imyen":"개인 웹사이트(Rachel Yeeun Kim), 분야 불명",
"anu_seoul":"버려진 도자기를 재료로 쓰는 브랜드, 맞는 topic 없음",
"moonsickgang":"작품 목록만 있고 분야 불명",
"openroles":"크리에이티브 채용 사이트, 맞는 topic 없음",
"designeverywhere_":"멤버십 클럽 페이지, 대상 성격 불명",
}
def w(path,row,head):
    new=not os.path.exists(D+path)
    with open(D+path,"a",encoding="utf-8-sig",newline="") as f:
        c=csv.writer(f)
        if new: c.writerow(head)
        c.writerow(row)
for u,v in N.items():
    fn,al,tp,ci,co,tl,web=v
    web=site(u) if web is None else web
    mknote(fn,al,tp,f"https://www.instagram.com/{u}/",website=web,cities=ci,countries=co,tldr=tl)
    w("bio-done.csv",[u,fn+".md",BATCH],["username","노트 파일","배치"])
for u,why in CHK.items():
    o=R[u]; w("manual-check-3.csv",[u,f"https://www.instagram.com/{u}/",o['n'],"사이트가 아이디를 링크함. "+why,o['url']],["username","인스타 주소","display_name","확인할 내용","바이오 링크"])
# 사이트가 아이디를 링크하지 않음 -> no-evidence-3, 열리지 않음 -> unverifiable-links
for u,o in R.items():
    if u in N or u in CHK: continue
    if 'err' in o: w("unverifiable-links.csv",[u,f"https://www.instagram.com/{u}/",o['n'],o['url'],o['err']],["username","인스타 주소","display_name","확인 못 한 링크","사유"])
    else: w("no-evidence-3.csv",[u,f"https://www.instagram.com/{u}/",o['n'],o['url'],o['title'][:60],"사이트가 이 인스타 아이디를 링크하지 않음"],["username","인스타 주소","display_name","바이오 링크","사이트 제목","사유"])
print(len(N),len(CHK))
