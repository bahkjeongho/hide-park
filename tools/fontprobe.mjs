// 사용: node tools/fontprobe.mjs <url> <css selector>...   (PROF=임시 프로필 폴더, 생략하면 자동)
// 각 요소의 글자가 실제로 어떤 글꼴(웹폰트/시스템)로 그려지는지 Chrome에서 조회한다.
import { spawn } from "node:child_process";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
const port = 9400 + Math.floor(Math.random() * 400);
const profile = process.env.PROF || fs.mkdtempSync(path.join(os.tmpdir(), "hp-chrome-"));
const [url, ...sels] = process.argv.slice(2);
const chrome = spawn("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", [
  "--headless=new","--disable-gpu",`--remote-debugging-port=${port}`,
  `--user-data-dir=${profile}`,"--window-size=1440,900","about:blank"],{stdio:"ignore"});
const sleep=(ms)=>new Promise(r=>setTimeout(r,ms));
let ws, id=0; const pending=new Map();
async function connect(){
  for(let i=0;i<40;i++){ try{
    const list=await (await fetch(`http://127.0.0.1:${port}/json`)).json();
    const t=list.find(x=>x.type==="page"); if(t){ ws=new WebSocket(t.webSocketDebuggerUrl); await new Promise((res,rej)=>{ws.onopen=res;ws.onerror=rej}); return; }
  }catch{} await sleep(500);} throw new Error("no chrome");
}
const send=(method,params={})=>new Promise(res=>{const i=++id;pending.set(i,res);ws.send(JSON.stringify({id:i,method,params}))});
try{
  await connect();
  ws.onmessage=(m)=>{const d=JSON.parse(m.data); if(d.id&&pending.has(d.id)){pending.get(d.id)(d.result??d.error);pending.delete(d.id)}};
  await send("Page.enable"); await send("DOM.enable"); await send("CSS.enable");
  await send("Page.navigate",{url}); await sleep(9000);
  const doc=await send("DOM.getDocument",{depth:0});
  for(const sel of sels){
    const q=await send("DOM.querySelector",{nodeId:doc.root.nodeId,selector:sel});
    if(!q.nodeId){console.log(sel,"-> (요소 없음)");continue}
    const f=await send("CSS.getPlatformFontsForNode",{nodeId:q.nodeId});
    console.log(sel,"->",(f.fonts||[]).map(x=>`${x.familyName} [${x.isCustomFont?"웹폰트":"시스템"}] ${x.glyphCount}자`).join(" | ")||JSON.stringify(f));
  }
}finally{ await new Promise((r)=>{ chrome.once("exit", r); chrome.kill(); setTimeout(r, 3000); });
  if(!process.env.PROF){ try{ fs.rmSync(profile,{recursive:true,force:true,maxRetries:5,retryDelay:300}); }catch{} }
  process.exit(0); }
