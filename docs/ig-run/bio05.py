import csv,json,os,urllib.parse as up
from rec import mknote,D
S="/private/tmp/claude-503/-Users-parkjeongho-Developer-Hide-Park/873d87db-505a-43d5-8e4c-ad9523e833cb/scratchpad/"
R={o['u']:o for o in json.load(open(S+"f_400.json"))}
BATCH=5
def site(u):
    p=up.urlparse(R[u]['url']); return f"{p.scheme}://{p.netloc}/"
# u: (파일명, aliases, topics, cities, countries, tldr, website(None=사이트 루트, ''=없음))
N={
"wgnb.kr":("WGNB",[],["Architecture Studio"],[],["South Korea"],"프로젝트, 공간, 건축, 제품을 다루는 스튜디오",None),
"beattitude.magazine":("BE(ATTITUDE)",["비애티튜드","BE(ATTITUDE) 비애티튜드"],["Magazine"],[],["South Korea"],"동시대 한국의 떠오르는 작가와 브랜드를 소개하는 매거진",None),
"adocs_official":("Adocs",["에이독스","adocs"],["Art Platform"],[],["South Korea"],"국내외 예술가의 개인 출판물을 웹에 쌓아 소개하는 아트북 플랫폼",None),
"cerric.official":("CERRIC",["세릭"],["Fashion Brand"],[],["South Korea"],"자유롭고 대담한 컨템포러리 브랜드",None),
"aieul.co":("Aieul",[],["Fashion Brand"],[],[],"컬렉션과 룩북을 선보이는 패션 브랜드",None),
"tune.kr":("TUNE",["TUNE.KR"],["Fashion Retail"],["Seoul"],["South Korea"],"성수에 있는 크리에이티브 컨셉 스토어이자 커뮤니티",None),
"youngnsang":("Young n Sang",["young n sang - ageless wear"],["Fashion Brand"],[],[],"스케치, 핸드 위븐, 캔버스 컬렉션을 선보이는 패션 브랜드",None),
"safarispot":("SAFARISPOT",["사파리스팟"],["Fashion Brand"],[],["South Korea"],"일상에서 입는 유니섹스 캐주얼웨어 브랜드",None),
"jichoinet":("JICHOI",["지초이","JICHOI.NET"],["Fashion Brand"],[],["South Korea"],"Ji Choi(지초이)가 JICHOI, JICHOI COMFORT 등을 전개하는 브랜드",None),
"costperkilo":("Cost per Kilo",["CPK","코스트퍼킬로","COSTPERKILO"],["Fashion Brand"],[],["South Korea"],"온라인 스토어와 룩북을 운영하는 패션 브랜드",None),
"recto_official":("RECTO",[],["Fashion Brand"],[],[],"컬렉션을 선보이는 패션 브랜드",None),
"12345studio":("12345",["1-2-3-4-5"],["Design Studio"],[],[],"다분야 협업형 디자인 스튜디오",None),
"corpus.kr":("CORPUS",[],["Creative Studio"],["Seoul"],["South Korea"],"2002년 그래픽 디자이너 안병학이 시작한 출판·전시 컬렉티브",None),
"ee_etiquettevide":("ÉÉ",["이이","ÉTIQUETTE VIDÉ","NOUVMARÉE"],["Fashion Brand"],[],["South Korea"],"비워진 라벨이라는 뜻의 ÉTIQUETTE VIDÉ를 줄인 이름의 패션 브랜드 (누마레)",None),
"degs_studio":("DEGS",["덱스","DEGS Studio"],["Creative Consultancy"],[],["South Korea"],"프로젝트를 위한 크리에이티브 컨설턴시이자 디자인 스튜디오",None),
"samplaskr":("SAMPLAS",["샘플라스"],["Fashion Retail"],["Seoul"],["South Korea"],"2012년부터 80개 이상의 디자이너 브랜드를 큐레이션한 도산 편집숍",None),
"carnetarchive":("CARNET-ARCHIVE",["CARNET ARCHIVE"],["Fashion Brand"],[],["South Korea"],"실험적 럭셔리를 내세운 패션 브랜드",None),
"kate.farm":("KATE FARM",["케이트팜"],["Creative Agency"],["Seoul"],["South Korea"],"서울 연희동의 전시 기획·홍보·운영 에이전시",None),
"revuemagazine_":("REVUE MAGAZINE",["Revue Magazine"],["Magazine"],[],["France"],"프랑스 매거진",None),
"rawpiece.magazine":("Rawpiece Magazine",["rawpiecemagazine"],["Magazine"],[],[],"금속, 직물, 유리, 도자 등 분야의 작가를 에피소드로 소개하는 매거진",None),
"archivepdf":("ARCHIVE.pdf",["ARCHIVE PDF"],["Fashion Journalism"],[],[],"패션의 과거와 현재를 잇는 서브스택과 아티클 매체","" ),
"magazinemagazine.fr":("Magazine magazine",[],["Magazine"],[],["France"],"프랑스 매거진",None),
"xlimlink":("XLIM",[],["Fashion Brand"],[],["South Korea"],"에피소드 형식으로 컬렉션을 소개하는 브랜드",None),
"nuhwacontemporary":("Nuhwa Contemporary",[],["Art Gallery"],[],[],"동시대 미술을 선보이는 갤러리이자 전시 실험실",None),
"luciole.playtime":("플레이타임",["리시올/플레이타임","리시올","Playtime"],["Publisher"],[],["South Korea"],"리시올/플레이타임 출판사",None),
}
CHK={
"oaahagency":"주식회사 예술고래상회가 운영, OA WORKS/OA BRANDS 사업 성격이 불명확",
"langleeschool":"공식 웹사이트라는 문구뿐, 대상 정보 불충분",
"plastic_product":"Mass-Produced articles라는 문구뿐, 성격 불명",
"passage.group":"프로젝트 목록만 있고 성격 불명",
"ignotaonline":"온라인 스토어, 분야 설명 없음",
"nvrfrgt_official":"일본 사이트, 브랜드 성격 설명 불충분",
"lostairseoul":"Bio, CV 페이지뿐, 분야 불명",
"ringotv.kr":"신디사이저 숍, 맞는 topic 없음",
"rainmakers7":"본문 정보 없음",
"gigantpr":"본문 정보 없음",
"pressworks":"인쇄·제작 업체, 맞는 topic 없음",
"bellboyclothing":"CLOTHING MAGAZINE CONSULTANCY 표기, 성격이 섞여 불명확",
"keigo__okazaki":"바이오 링크가 에이전시 프로필 페이지(모델 프로필), 맞는 topic 없음",
"spidi_on_track":"모터사이클 기어 브랜드, 맞는 topic 없음",
"melted.potato":"쇼핑몰 신상품 페이지, 성격 불명",
"primary_practice":"전시·출판 메뉴만 있고 성격 불명",
"fstvl.life":"바이오 링크가 링크 모음 페이지, 성격 불명",
"newmedium.seoul":"본문 정보 없음",
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
