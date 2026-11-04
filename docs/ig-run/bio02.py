import csv,json,os,urllib.parse as up
from rec import mknote,D
S="/private/tmp/claude-503/-Users-parkjeongho-Developer-Hide-Park/873d87db-505a-43d5-8e4c-ad9523e833cb/scratchpad/"
R={o['u']:o for o in json.load(open(S+"f_100.json"))}
BATCH=2
def site(u):
    p=up.urlparse(R[u]['url']); return f"{p.scheme}://{p.netloc}/"
# u: (파일명, aliases, topics, cities, countries, tldr, website(None=사이트 루트, ''=없음))
N={
"dabinkiim":("Dabin Kiim",[],["Graphic Designer"],["Seoul"],["South Korea"],"서울 기반 그래픽 디자이너이자 개발자",None),
"imago.xyz":("이마고픽쳐스",["Imago Pictures","imagopictures"],["Creative Production"],[],[],"LED 미디어파사드, 미디어아트, 프로젝션 맵핑 콘텐츠를 만드는 공간형 뉴미디어 스튜디오",None),
"onepointzerone":("one point zero one",["ONE POINT ZERO ONE","1.01"],["Design Studio"],[],[],"브랜딩과 패키지 디자인을 다루는 스튜디오",None),
"designedbyforge":("Forge",[],["Design Studio"],[],[],"디자인과 개발을 함께 하는 작은 협동조합",None),
"_invisibledynamics":("Invisible Dynamics",[],["Brand Consultancy"],[],[],"브랜드가 미래를 만들도록 돕는 차세대 브랜드 트랜스포메이션 컨설팅",None),
"momandson_store":("MOMANDSON",["momandson_store"],["Fashion"],[],[],"아우터, 상의, 원피스 등을 파는 패션 쇼핑몰",None),
"automatic_for_the_people":("AUTOMATIC FOR THE PEOPLE",["오토매틱 포 더 피플"],["Fashion"],[],[],"CITY OUTDOOR를 내세운 패션 브랜드",None),
"ni_gnoej_":("Jeongin Byeon",[],["Designer"],["London","Seoul"],[],"1999년 서울 출생, 런던과 서울을 오가며 활동하는 디자이너",None),
"yiv.kr":("YIV",["yiv.kr"],["Creative Agency"],[],[],"브랜드의 미학을 다듬는 크리에이티브 에이전시",None),
"emerald_costantino":("Emily Costantino",[],["Stylist"],["New York"],[],"영화와 패션을 오가는 뉴욕 기반 의상 디자이너이자 스타일리스트",None),
"_hanayagi":("Hana Yagi",["八木 華"],["Fashion Designer"],[],["Japan"],"일본의 신진 디자이너","" ),
"esteem_collective":("ESteem Collective",[],["Fashion Platform"],[],["South Korea"],"에스팀 그룹이 운영하는 글로벌 브랜드 매니지먼트·세일즈 플랫폼","" ),
"ernestonaranjo":("Ernesto Naranjo",["NARANJO"],["Fashion Brand"],[],[],"컬렉션을 발표하는 패션 브랜드",None),
"futuraproject_":("FUTURA PROJECT",[],["Creative Production"],["Madrid"],["Spain"],"프로덕션, 세트 디자인, 한시적 건축, 조경을 다루는 마드리드 기반 스튜디오",None),
"extrasmall.kr":("extrasmall",[],["Design Studio"],["Seoul"],["South Korea"],"서울 기반 디자인 스튜디오",None),
"dent.studio":("Dent Studio",["DENT studio"],["Creative Agency"],[],[],"스포츠·문화·패션 분야 브랜드와 일하는 360도 크리에이티브 에이전시",None),
"kitten_production":("Kitten Production",["KITTEN"],["Creative Production"],[],[],"패션·라이프스타일·뷰티·럭셔리 산업의 스틸, 모션, 디지털 콘텐츠를 만드는 프로덕션",None),
"marquelrw":("Marquel Williams",["Marquel Rashaad Williams"],["Designer"],[],[],"가구와 오브제를 만드는 디자이너",None),
"noas_____studio":("Noas Studio",["noas"],["Design Studio"],[],[],"디자인 스튜디오",None),
"studiograylab":("Studio Gray Lab",["Studio Gray Lab™"],["Branding Agency"],[],[],"브랜딩과 아이덴티티 디자인을 다루는 크리에이티브 에이전시",None),
"sia.arnika":("Sia Arnika",["SIA ARNIKA"],["Fashion Brand"],["Berlin"],["Germany"],"덴마크 출신 디자이너의 이름을 딴 베를린 기반 레이블",None),
"grid_office":("Grid",[],["Creative Consultancy"],["Seoul"],["South Korea"],"서울 기반 크리에이티브 컨설턴시",None),
"paolalaf":("Paola Laforgia",["Paola Laf"],["Writer"],[],["South Korea"],"한국과 유럽을 오가며 한류의 역사를 다룬 책을 쓴 작가",None),
"at_paris":("AT PARIS",["At Paris"],["Creative Agency"],[],[],"전략, 탤런트 매니지먼트, 스케노그래피, 아트 디렉션을 다루는 에이전시",None),
"gabrielahansenxo":("Gabriela Hansen",[],["Creative Director","Video Director","Photographer"],["Los Angeles"],["USA"],"LA 기반 크리에이티브 디렉터, 영상 감독, 에디터, 사진가, 작곡가",None),
"_boyheart_":("Joel Palmer",["BOYHEART"],["Photographer","Video Director","Creative Director"],["London"],["UK"],"런던 기반 패션 사진가이자 영화 감독, 크리에이티브 디렉터",None),
}
CHK={
"oli.xl":"Warp Records 소속 음악가로 보이나 사이트 문구뿐, 아티스트 노트 정보 부족",
"paris_image_unlimited":"문의 페이지만 있고 분야 불명",
"kaylaconnors":"연락처 페이지뿐, 분야 불명",
"kendalwalkerr":"TRACKS Book 포트폴리오, 분야 설명 없음",
"timothygibbons":"클라이언트 목록(Charli XCX 등)만 있고 직업 설명 없음",
"_asahina__":"도쿄 기반 비주얼 아티스트이나 맞는 topic 없음",
"elise.bosmans.portfolio":"포트폴리오 화살표 화면뿐, 분야 불명",
"alt.er.seoul":"스튜디오 대여·프로젝트 아카이브 사이트, 성격 불명",
"___systum":"유틸리티 모듈 쇼핑몰, 대상 성격 불명",
"oldfriendsbookends_":"후원 페이지(buymeacoffee), 크리에이터 성격 불명",
"studio_saints":"연락처만 있는 페이지, 분야 불명",
"br.and.ing":"바이오 링크가 Qurrv 제출 페이지(대상 사이트 아님)",
"oja.seoul":"도자 브랜드 오자크래프트의 공간, 맞는 topic 없음 (기사 링크가 근거)",
"ojacraft":"핸드메이드 도자 브랜드, 맞는 topic 없음",
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
