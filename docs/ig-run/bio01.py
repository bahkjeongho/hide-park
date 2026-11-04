import csv,json,os,urllib.parse as up
from rec import mknote,D
S="/private/tmp/claude-503/-Users-parkjeongho-Developer-Hide-Park/873d87db-505a-43d5-8e4c-ad9523e833cb/scratchpad/"
R={o['u']:o for o in json.load(open(S+"f_0.json"))}
BATCH=1
def site(u):
    p=up.urlparse(R[u]['url']); return f"{p.scheme}://{p.netloc}/"
# u: (파일명, aliases, topics, cities, countries, tldr, website(None=사이트 루트, ''=없음))
N={
"sunhye_sunhye":("Kim Sunhye",["김선혜","Kimsunhye"],["Photographer"],[],[],"후츠파에이전시 소속 사진가","" ),
"ilya_lipkin":("Ilya Lipkin",[],["Photographer"],["New York","Berlin"],[],"리가 출생, 뉴욕과 베를린을 오가며 활동하는 사진가이자 비주얼 아티스트",""),
"joshuahughesgames":("Joshua Hughes-Games",[],["Creative Director","Designer"],[],[],"크리에이티브 디렉터, 디자이너, 프린터",None),
"550bc":("550BC",[],["Publisher"],[],[],"조직범죄 문화와 분쟁 현실을 기록하는 사진집을 내는 독립 출판사",None),
"empiredesign.studio":("Empire Design",[],["Creative Agency"],["London","New York"],[],"영화·엔터테인먼트 키아트와 AV 캠페인을 만드는 런던·뉴욕 크리에이티브 에이전시",None),
"hohoho.group":("HOHOHO",["HOHOHO GROUP"],["Design Agency"],["Seoul"],["South Korea"],"서울 기반 멀티디서플린 디자인 에이전시",None),
"julien_hebert":("Julien Hébert",["Julien Hebert"],["Graphic Designer","Art Director"],["Montréal"],["Canada"],"몬트리올 기반 그래픽 디자이너이자 아트 디렉터",None),
"celine_le_chien":("David Beauchemin",[],["Graphic Designer","Art Director"],["Montréal"],["Canada"],"몬트리올의 그래픽 디자이너이자 아트 디렉터",None),
"baw_bak_":("Babak Khoshnoud",["deep persian blue"],["Creative Director","Video Director"],[],[],"독립 스튜디오 deep persian blue를 운영하는 디렉터이자 크리에이티브 디렉터",None),
"concretereplimited":("Concrete Rep",["Concrete","Concrete Rep."],["Creative Agency"],[],[],"아트·패션·에디토리얼·광고 분야 아티스트를 대리하는 에이전시",None),
"hellohellohteam":None,
"hellohelloteam":("++hellohello",["hellohello"],["Design Agency"],[],[],"브랜드를 위한 경험을 만드는 디자인·테크놀로지 에이전시",None),
"daleluiza":("Luiza Dale",[],["Designer"],[],[],"그래픽 시스템, 전시, 브랜딩, 캠페인을 다루는 디자이너이자 디자인 디렉터. 스튜디오 The Aliens와 함께 활동",None),
"beige.sst_design":("SST Design",["SST","이진일"],["Design Studio"],[],[],"브랜드 전략과 아트 디렉션을 다루는 디자인 스튜디오 (2018–2023)",None),
"textureontexture":("Texture on Texture",["TEXTURE ON TEXTURE"],["Photography"],[],[],"2015년부터 이미지를 만들어 온 사진 기반 스튜디오",None),
"newapologyprojects":("New Apology",["New Apology Projects"],["Design Studio"],[],[],"브랜드 정체성을 정리하고 전달해 주는 디자인 스튜디오",None),
"studioenok":("Studioenok",["Studioenok嗯好的"],["Design Studio"],[],[],"브랜드 아이덴티티, 패키징, 디지털 디자인을 다루는 스튜디오",None),
"evening.fyi":("EVENING",["EVENING."],["Creative Studio"],[],[],"MØRNING의 자매 스튜디오, 문화 전략을 실행으로 옮기는 크리에이티브·커뮤니티 프로덕션 스튜디오",None),
"morning.fyi":("MØRNING",["MØRNING.","MORNING"],["Creative Studio"],["London"],["UK"],"런던 기반 크리에이티브 스트래티지 스튜디오",None),
"27b.ureau":("27b",["27b.","27b Bureau"],["Creative Studio"],["Amsterdam","Los Angeles"],[],"엔터테인먼트·문화·커머스 브랜드를 위한 독립 크리에이티브 스튜디오",None),
"studio_okens":("Studio Okens",["studio okens®","스튜디오 오켄스"],["Design Studio"],["Seoul"],["South Korea"],"서울 기반 디자인 스튜디오",None),
"isleofany":("Isle of Any",[],["Creative Company"],[],[],"스스로를 새로운 아이디어 회사로 소개하는 크리에이티브 회사",None),
"ecru_official":("ÉCRU",["에크루","ÉCRU OFFICIAL"],["Fashion"],[],["South Korea"],"국내외 브랜드를 소개하는 패션 라이프스타일 편집숍",None),
"xjulianaross":("Juliana Ross",[],["Designer"],[],[],"Manual의 디자인 디렉터",None),
"tinywins":("TinyWins",[],["Branding Agency"],[],[],"브랜드, 디지털, 캠페인을 만드는 감정 중심 브랜드·디지털 에이전시",None),
"named.design":("named. design co.",["네임드 디자인 컴퍼니","named"],["Brand Design"],[],[],"브랜드 디자인 전문 회사",None),
"_miabarnes":("Mia Barnes",[],["Video Director","Photographer"],["Los Angeles"],["USA"],"상업 광고, 뮤직비디오, 아티스트 프로젝트를 다루는 LA 기반 감독이자 사진가",None),
"snyder.erica":("Erica Snyder",["Erica Devin Snyder","Erica Baby Snyder"],["Photographer","Video Director"],[],[],"사진, 뮤직비디오 연출, 에디토리얼을 다루는 작업자",None),
"yourstrulycreative":("Yours Truly Creative",[],["Design Studio"],[],[],"디자인과 스토리 스튜디오",None),
"nova.lab_design":("N.O.V.A LAB",["NOVA LAB"],["Design Studio"],[],[],"그래픽 디자인과 크리에이티브 디렉션으로 새로운 서사를 만드는 비주얼 랩",None),
"junheum.na":("나준흠",["Na Junheum"],["Graphic Designer"],[],["South Korea"],"전시·책·아이덴티티·포스터 등을 다루는 디자이너",None),
}
N={k:v for k,v in N.items() if v}
CHK={ # 사이트가 아이디를 링크하지만 대상 분야를 확인하지 못함
"behind_the_lenssse":"사이트는 크리에이티브 채용·이벤트 정보 모음 (적합한 topic 없음)",
"marvellouslastnight":"Coffee Table Gallery 페이지라는 것만 확인, 분야 불명",
"everyday_io":"집의 공기·물·에너지를 통합하는 회사, 맞는 topic 없음",
"progra.mm.e":"뉴스레터 구독 페이지뿐, 분야 불명",
"_elsamueller":"Studio Elsa Mueller 포트폴리오, 분야 설명 없음",
"studiotemp":"Studio Temp 소개 문구 없음, 분야 불명",
"susannahayward":"언론 매체 이름만 나열, 분야 불명",
"sevv.up":"서울의 음악 CD 판매 페이지, 대상 성격 불명",
"patchroom":"홈·스톡리스트만 있는 페이지, 분야 불명",
"oliclarke__":"연락처와 인스타그램만 있는 페이지, 분야 불명",
"jeong.chanwoong":"프로젝트 목록만 있고 분야 설명 없음",
"yooodowon":"작품 목록과 CV만 있고 분야 설명 없음",
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
