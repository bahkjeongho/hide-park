// "2. Wiki" → "2 Wiki": 번호 뒤의 온점을 빼서 주소가 /2-wiki 로 나오게 한다. (볼트 원본은 그대로)
import fs from "node:fs";
import path from "node:path";

const root = process.argv[2] || "content";
let count = 0;

function walk(dir) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    if (!e.isDirectory()) continue;
    const full = path.join(dir, e.name);
    walk(full); // 안쪽부터 바꿔서 경로가 어긋나지 않게 한다
    const renamed = e.name.replace(/^(\d+)\.\s+/, "$1 ");
    if (renamed !== e.name) {
      fs.renameSync(full, path.join(dir, renamed));
      count++;
    }
  }
}

walk(root);
console.log(`폴더 이름 정리: ${count}개`);
