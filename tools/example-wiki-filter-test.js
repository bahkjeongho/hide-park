(async()=>{
  const q=(s)=>document.querySelector(s), qa=(s)=>[...document.querySelectorAll(s)];
  const wait=(ms)=>new Promise(r=>setTimeout(r,ms));
  const rows=()=>qa(".folder-index__item").length;
  const first=()=>q(".folder-index__item .folder-index__title")?.textContent;
  const [topicBtn,regionBtn,sortBtn]=qa(".folder-index__button");
  const out={start:rows(),firstAZ:first()};
  topicBtn.click(); await wait(100);
  out.topicOptions=qa(".folder-index__option").length;
  const opt=(name)=>qa(".folder-index__option").find(b=>b.firstChild&&b.firstChild.textContent===name);
  opt("Photographer").click(); await wait(100);
  out.photographer=rows(); out.topicBtn=topicBtn.textContent; out.head=qa(".folder-index__head span")[1].textContent;
  regionBtn.click(); await wait(100);
  out.regionOptions=qa(".folder-index__option").map(b=>b.textContent).slice(0,6);
  opt("UK").click(); await wait(100);
  out.photographerUK=rows();
  topicBtn.click(); await wait(100); qa(".folder-index__option")[0].click(); await wait(100);
  out.uk=rows(); out.regionBtn=regionBtn.textContent; out.ukTitles=qa(".folder-index__title").map(a=>a.textContent).slice(0,4);
  sortBtn.click(); await wait(100);
  out.sort=sortBtn.textContent; out.firstZA=first();
  regionBtn.click(); await wait(100); qa(".folder-index__option")[0].click(); await wait(100);
  out.reset=rows();
  return out;
})()
