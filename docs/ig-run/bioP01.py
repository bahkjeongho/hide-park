import csv,json,os,urllib.parse as up
from rec import mknote,D
S="/private/tmp/claude-503/-Users-parkjeongho-Developer-Hide-Park/873d87db-505a-43d5-8e4c-ad9523e833cb/scratchpad/"
R={o['u']:o for o in json.load(open(S+"g_0.json"))}
BATCH=1
def site(u):
    p=up.urlparse(R[u]['url']); return f"{p.scheme}://{p.netloc}/"
# u: (파일명, aliases, topics, cities, countries, tldr, website(None=사이트 루트, ''=없음))
N={
"galeriebahnhof":("바노프",["Galerie Bahnhof","galeriebahnhof"],["Design"],[],["South Korea"],"프렌치 모던 등 디자인 가구를 소개하는 갤러리 겸 상점",None),
"brutusmag":("BRUTUS",["ブルータス","BRUTUS magazine"],["Magazine"],[],["Japan"],"의식주 여행 등 호기심을 다루는 일본 잡지",None),
"sogi.sogi.sogi":("소기박",[],["Graphic Designer"],[],["South Korea"],"그래픽 디자이너",None),
"oddflat":("오드플랫",["Oddflat"],["Design"],[],["South Korea"],"Eames를 비롯한 디자이너 빈티지 가구를 소개하는 숍",None),
"jaeyeonkim.kr":("Jaeyeon Kim",["김재연","재연"],["Graphic Designer"],["Seoul"],["South Korea"],"서울 기반 그래픽 디자이너",None),
"ffmfed":("Federico Valla",[],["Creative Director"],[],[],"독립 크리에이티브 디렉터이자 개발자",None),
"querida__si":("Querida",[],["Creative Consultancy"],[],[],"기관, 브랜드, 개인을 위한 콘텐츠와 크리에이티브 디렉션을 개발하는 크리에이티브·전략 컨설턴시",None),
"kangjungseok.official":("강정석",["KANGJUNGSEOK"],["Fashion Brand"],[],["South Korea"],"강정석이 전개하는 패션 브랜드",None),
"sculpstore_official":("스컬프스토어",["SCULP STORE","sculpstore"],["Fashion Retail"],[],["South Korea"],"Needles, RRL, Capital 등을 다루는 셀렉트숍",None),
"sonayong":("Ayong Son",["AYONG"],["Designer"],[],[],"다양한 매체와 형식을 넘나드는 디자이너이자 아티스트",None),
"caracalpress":("카라칼",["Caracal","caracalpress"],["Publisher"],[],["South Korea"],"도전적인 논픽션 콘텐츠를 만드는 작은 출판 브랜드",None),
"yoon_ambush":("Yoon Ahn",["YOON"],["Fashion Designer","Creative Director"],[],[],"주얼리와 레디투웨어 브랜드 AMBUSH의 창립자이자 크리에이티브 디렉터",None),
"paulolivennes":("Paul Olivennes",[],["Publisher"],[],[],"큐레이터, 아트 퍼블리셔, 아티스틱 디렉터이자 MAGMA 설립자",None),
"choiyumi___":("Choi Yumi",["YUMI CHOI","최유미"],["Stylist"],[],["South Korea"],"NewJeans 스타일링을 맡은 프리랜서 스타일리스트","" ),
"yfactorial":("y!",["yfactorial","y! - yfactorial ltd."],["Design Studio"],["Seoul"],["South Korea"],"서사를 시각화하는 솔루션을 제공하는 서울 기반 멀티디서플린 스튜디오",None),
"constant_practice":("Constant Practice",[],["Fashion Retail"],[],[],"뉴 앤 빈티지 디자이너 패션을 큐레이션하는 숍",None),
}
CHK={
"satoshinakamoto._":"사이트에 소개 문구 없음",
"spineseoul":"쪽프레스|고트 워크숍 페이지, 계정이 가리키는 대상이 불명확",
"ssmen.k":"바이오 링크가 디자인 스튜디오 보부오피스(소속), 계정 본인 정보 없음",
"tomandnick_official":"소개 문구뿐, 분야 불명",
"openpath.kr":"디자이너를 위한 교육 플랫폼, 맞는 topic 없음",
"kolroystudio":"Nike archive 페이지뿐, 분야 불명",
"philoelectroray":"철학 학문 공동체, 맞는 topic 없음",
"computer_format_":"본문 정보 없음",
"sandollcloud":"볼트에 Sandoll 노트가 이미 있음 (산돌구름은 Sandoll의 서비스, IG 추가 여부 확인)",
"_kwangho_lee":"공식 웹사이트, 분야 설명 없음",
"wepractice":"그래픽 디자인 스튜디오 추정이나 본문 정보 없음",
"chae.hee.park":"포트폴리오 사이트, 분야 불명",
"ica.snu":"서울대 문화예술원(대학 내 기관), 맞는 topic 없음",
"josiehall.g":"MMXX Artists 에이전시의 아티스트 프로필, 분야 불명",
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
    w("bio-done-2.csv",[u,fn+".md",BATCH],["username","노트 파일","배치"])
for u,o in R.items():
    if o.get('match') and u not in N and u not in CHK: CHK[u]='사이트가 아이디를 링크하지만 대상 성격 판단 불충분'
for u,why in CHK.items():
    o=R[u]; w("manual-check-4.csv",[u,f"https://www.instagram.com/{u}/",o['n'],"사이트가 아이디를 링크함. "+why,o['url']],["username","인스타 주소","display_name","확인할 내용","바이오 링크"])
# 사이트가 아이디를 링크하지 않음 -> no-evidence-3, 열리지 않음 -> unverifiable-links
for u,o in R.items():
    if u in N or u in CHK: continue
    if 'err' in o: w("unverifiable-links-2.csv",[u,f"https://www.instagram.com/{u}/",o['n'],o['url'],o['err']],["username","인스타 주소","display_name","확인 못 한 링크","사유"])
    else: w("no-evidence-4.csv",[u,f"https://www.instagram.com/{u}/",o['n'],o['url'],o['title'][:60],"사이트가 이 인스타 아이디를 링크하지 않음"],["username","인스타 주소","display_name","바이오 링크","사이트 제목","사유"])
print(len(N),len(CHK))
