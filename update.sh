#!/bin/bash
set -e
cd "$(dirname "$0")"

VAULT="/Users/parkjeongho/Library/Mobile Documents/iCloud~md~obsidian/Documents/Hide Park"

rm -rf content && mkdir content
cp -R "$VAULT/." content/
rm -rf "content/0. Clipping Origin" "content/00. Template" content/.obsidian content/.smart-env
find content -name ".DS_Store" -delete
# 홈 노트: 볼트 루트에 index.md 가 없으면(2. Wiki 로 옮겨 둔 경우 등) 빈 홈 노트를 만든다. 없으면 홈 주소가 index.xml(RSS)로 열린다.
[ -f content/index.md ] || printf -- '---\ntitle: Hide Park\n---\n' > content/index.md
find content -name "*.md" -print0 | LC_ALL=C xargs -0 sed -i '' 's/\[! /[!/g'
node rename-folders.mjs content
node clean-frontmatter.mjs content
node make-labels.mjs content

git add -A
if git diff --cached --quiet; then
  echo "변경 사항 없음"
  exit 0
fi

git commit -m "Update wiki $(date '+%Y-%m-%d %H:%M')"
git pull --no-rebase --no-edit origin v5
git push origin v5
echo "완료: 1~3분 뒤 사이트에 반영됩니다."
