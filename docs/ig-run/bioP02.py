import csv,json,os,urllib.parse as up
from rec import mknote,D
S="/private/tmp/claude-503/-Users-parkjeongho-Developer-Hide-Park/873d87db-505a-43d5-8e4c-ad9523e833cb/scratchpad/"
R={o['u']:o for o in json.load(open(S+"g_100.json"))}
BATCH=2
def site(u):
    p=up.urlparse(R[u]['url']); return f"{p.scheme}://{p.netloc}/"
# u: (파일명, aliases, topics, cities, countries, tldr, website(None=사이트 루트, ''=없음))
N={
"peterashlee":("Peter Ash Lee",[],["Photographer","Video Director"],["Paris","New York","Seoul"],[],"파리, 뉴욕, 서울을 오가며 활동하는 사진가이자 감독",None),
"kunsik_":("Kunsik",["KUNSIK","Kunsik Choi","최근식"],["Design Studio"],["Stockholm"],["Sweden"],"2015년 한국 출신 디자이너 최근식이 설립한 스톡홀름 기반 디자인 스튜디오",None),
"jjokkpress":("쪽프레스",["쪽프레스|고트","JJOK PRESS"],["Publisher"],["Seoul"],["South Korea"],"서울 기반으로 활동하는 레이블",None),
"jiyongkim_official":("JiyongKim",["지용킴","Jiyong Kim"],["Fashion Brand"],[],["South Korea"],"태양만으로 의류를 탈색하는 패션 브랜드",None),
}
CHK={
"phillip.windly":"개인 포트폴리오 사이트(P-K), 분야 설명 없음",
"yangjang.type":"포트폴리오 사이트, 분야 설명 없음",
"ujeongguk":"탈영역우정국 소개 문구 없음, 성격 불명",
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
