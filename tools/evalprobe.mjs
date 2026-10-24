// 사용: node tools/evalprobe.mjs <url> '<JS 식>'   (PROF=임시 프로필 폴더, 생략하면 자동)
// 페이지를 연 뒤 JS 식(Promise 가능)을 실행하고 결과를 JSON으로 출력한다.
import { spawn } from "node:child_process";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
const port = 9400 + Math.floor(Math.random() * 400);
const profile = process.env.PROF || fs.mkdtempSync(path.join(os.tmpdir(), "hp-chrome-"));
const [url, expr] = process.argv.slice(2);
const chrome = spawn("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", [
  "--headless=new","--disable-gpu",`--remote-debugging-port=${port}`,
  `--user-data-dir=${profile}`,"--window-size=1440,900","about:blank"],{stdio:"ignore"});
const sleep=(ms)=>new Promise(r=>setTimeout(r,ms));
let ws,id=0; const pending=new Map();
try{
  for(let i=0;i<40;i++){ try{
    const list=await (await fetch(`http://127.0.0.1:${port}/json`)).json();
    const t=list.find(x=>x.type==="page"); if(t){ ws=new WebSocket(t.webSocketDebuggerUrl); await new Promise((res,rej)=>{ws.onopen=res;ws.onerror=rej}); break; }
  }catch{} await sleep(500);}
  ws.onmessage=(m)=>{const d=JSON.parse(m.data); if(d.id&&pending.has(d.id)){pending.get(d.id)(d.result??d.error);pending.delete(d.id)}};
  const send=(method,params={})=>new Promise(res=>{const i=++id;pending.set(i,res);ws.send(JSON.stringify({id:i,method,params}))});
  await send("Page.enable"); await send("Page.navigate",{url}); await sleep(10000);
  const r=await send("Runtime.evaluate",{expression:expr,returnByValue:true,awaitPromise:true});
  console.log(JSON.stringify(r.result?.value ?? r, null, 1));
}finally{ await new Promise((r)=>{ chrome.once("exit", r); chrome.kill(); setTimeout(r, 3000); });
  if(!process.env.PROF){ try{ fs.rmSync(profile,{recursive:true,force:true,maxRetries:5,retryDelay:300}); }catch{} }
  process.exit(0); }
