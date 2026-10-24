// 사용: node tools/shot.mjs <url> <out.png> <width> <height> [dark] [full]   (PROF=임시 프로필 폴더, 생략하면 자동. LS_SEED='{"키":"값"}' 이면 localStorage를 미리 채운다)
// 기기 에뮬레이션으로 스크린샷을 찍는다. 390 폭은 모바일, dark 를 주면 다크 모드.
import { spawn } from "node:child_process";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
const [url, out, w, hgt, dark, full] = process.argv.slice(2);
const profile = process.env.PROF || fs.mkdtempSync(path.join(os.tmpdir(), "hp-chrome-"));
const port = 9400 + Math.floor(Math.random()*400);
const chrome = spawn("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", [
  "--headless=new","--disable-gpu",`--remote-debugging-port=${port}`,
  `--user-data-dir=${profile}`,"about:blank"],{stdio:"ignore"});
const sleep=(ms)=>new Promise(r=>setTimeout(r,ms));
let ws,id=0; const pending=new Map();
try{
  for(let i=0;i<40;i++){ try{
    const list=await (await fetch(`http://127.0.0.1:${port}/json`)).json();
    const t=list.find(x=>x.type==="page"); if(t){ ws=new WebSocket(t.webSocketDebuggerUrl); await new Promise((res,rej)=>{ws.onopen=res;ws.onerror=rej}); break; }
  }catch{} await sleep(500);}
  ws.onmessage=(m)=>{const d=JSON.parse(m.data); if(d.id&&pending.has(d.id)){pending.get(d.id)(d.result??d.error);pending.delete(d.id)}};
  const send=(method,params={})=>new Promise(res=>{const i=++id;pending.set(i,res);ws.send(JSON.stringify({id:i,method,params}))});
  await send("Page.enable");
  await send("Emulation.setDeviceMetricsOverride",{width:+w,height:+hgt,deviceScaleFactor:2,mobile:+w<700});
  if(dark==="dark"){ await send("Page.addScriptToEvaluateOnNewDocument",{source:`try{localStorage.setItem("theme","dark")}catch(e){}`}); }
  if(process.env.LS_SEED){ await send("Page.addScriptToEvaluateOnNewDocument",{source:`try{const o=${process.env.LS_SEED};for(const k in o)localStorage.setItem(k,o[k])}catch(e){}`}); }
  await send("Page.navigate",{url}); await sleep(9000);
  const info=await send("Runtime.evaluate",{expression:"JSON.stringify({inner:innerWidth,scrollW:document.documentElement.scrollWidth,theme:document.documentElement.getAttribute('saved-theme')})",returnByValue:true});
  const params={format:"png"};
  if(full==="full"){ const m=await send("Page.getLayoutMetrics"); params.captureBeyondViewport=true; params.clip={x:0,y:0,width:+w,height:Math.min(m.cssContentSize.height,3000),scale:1}; }
  const shot=await send("Page.captureScreenshot",params);
  fs.writeFileSync(out,Buffer.from(shot.data,"base64"));
  console.log(out,info.result.value);
}finally{ await new Promise((r)=>{ chrome.once("exit", r); chrome.kill(); setTimeout(r, 3000); });
  if(!process.env.PROF){ try{ fs.rmSync(profile,{recursive:true,force:true,maxRetries:5,retryDelay:300}); }catch{} }
  process.exit(0); }
