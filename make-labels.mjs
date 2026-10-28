import fs from "node:fs";
import path from "node:path";

const root = process.argv[2] || "content";
const wiki = path.join(root, "2 Wiki");
const thoughts = path.join(root, "1 Thoughts");

const walk = (d) =>
  fs.readdirSync(d, { withFileTypes: true }).flatMap((e) =>
    e.isDirectory() ? walk(path.join(d, e.name)) : e.name.endsWith(".md") ? [path.join(d, e.name)] : [],
  );

const clean = (v) => {
  v = v.trim().replace(/^["']|["']$/g, "").trim();
  const m = v.match(/^\[\[([^\]]*)\]\]$/);
  return m ? m[1].split("|").pop().trim() : v;
};

// frontmatter 의 속성 값을 배열로 읽는다. (한 줄 값, `- 항목` 목록 모두)
function readProp(text, key) {
  const lines = text.split(/\r?\n/);
  const end = lines[0] === "---" ? lines.indexOf("---", 1) : -1;
  if (end < 0) return [];
  const i = lines.findIndex((l, n) => n > 0 && n < end && l.startsWith(`${key}:`));
  if (i < 0) return [];
  const out = [];
  const inline = clean(lines[i].slice(key.length + 1));
  if (inline && !inline.startsWith("[")) out.push(inline);
  for (let j = i + 1; j < end && !/^\S/.test(lines[j]); j++) {
    if (/^\s+-/.test(lines[j])) {
      const v = clean(lines[j].replace(/^\s+-\s*/, ""));
      if (v) out.push(v);
    }
  }
  return out;
}

const rel = (f) => path.relative(root, f).split(path.sep).join("/");

// 1) 노트별 세부 라벨(topic 첫 값): 홈 목록용 (random-labels.json)
const files = fs.existsSync(wiki) ? walk(wiki) : [];
const labels = {};
for (const f of files) {
  const label = readProp(fs.readFileSync(f, "utf8"), "topic")[0];
  if (label) labels[rel(f)] = label;
}
fs.writeFileSync(path.join(root, "random-labels.json"), JSON.stringify(labels));
console.log(`라벨 생성: ${Object.keys(labels).length}개 / Wiki 노트 ${files.length}개`);

// 2) 폴더 목록 페이지의 필터용 (wiki-meta.json)
//    Wiki: topics(topic 전체), regions(Countries + Cities)
//    Thoughts: date(Date), type(Type)
const meta = {};
for (const f of files) {
  const text = fs.readFileSync(f, "utf8");
  const topics = readProp(text, "topic");
  const regions = [...new Set([...readProp(text, "Countries"), ...readProp(text, "Cities")])];
  if (topics.length || regions.length) {
    const entry = {};
    if (topics.length) entry.topics = topics;
    if (regions.length) entry.regions = regions;
    meta[rel(f)] = entry;
  }
}
const thoughtFiles = fs.existsSync(thoughts) ? walk(thoughts) : [];
for (const f of thoughtFiles) {
  const text = fs.readFileSync(f, "utf8");
  const date = readProp(text, "Date")[0];
  const type = readProp(text, "Type")[0];
  if (date || type) meta[rel(f)] = { ...(date && { date }), ...(type && { type }) };
}
fs.writeFileSync(path.join(root, "wiki-meta.json"), JSON.stringify(meta));
console.log(`메타 생성: ${Object.keys(meta).length}개 (Wiki + Thoughts)`);

// 3) 속성에 값이 하나라도 있는 노트 (note-props.json): 링크 색에서 "완전히 빈 페이지"를 가를 때 쓴다.
//    본문이 비어도 아래 속성에 값이 있으면 빈 페이지로 보지 않는다. (aliases, topic, tags 는 값으로 세지 않는다.)
const DATA_KEYS = ["IG", "Website", "URL", "Wikis", "Cities", "Countries", "Related", "Genre", "Labels", "Member of"];
const withProps = [];
for (const dir of [wiki, path.join(root, "3 Object"), thoughts]) {
  if (!fs.existsSync(dir)) continue;
  for (const f of walk(dir)) {
    const text = fs.readFileSync(f, "utf8");
    if (DATA_KEYS.some((k) => readProp(text, k).length)) withProps.push(rel(f));
  }
}
fs.writeFileSync(path.join(root, "note-props.json"), JSON.stringify(withProps));
console.log(`속성 값이 있는 노트: ${withProps.length}개`);
