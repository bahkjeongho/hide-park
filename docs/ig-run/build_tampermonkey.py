import json
import os
import csv

D = "/Users/parkjeongho/Developer/Hide-Park/docs/ig-run"
accounts = []
with open(os.path.join(D, "no-evidence-accounts-park.csv"), "r", encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        accounts.append({
            "username": r["username"].strip(),
            "url": r["url"].strip(),
            "display_name": r.get("display_name", "").strip(),
            "분류": r.get("분류", "").strip(),
            "사유": r.get("사유", "").strip()
        })

accounts_json = json.dumps(accounts, ensure_ascii=False)

with open(os.path.join(D, "ig_tampermonkey_template.js"), "r", encoding="utf-8") as f:
    tpl = f.read()

target = '""" + accounts_json + """'
final_code = tpl.replace(target, accounts_json)

out_path = os.path.join(D, "ig_tampermonkey.js")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(final_code)

print("SUCCESS: ig_tampermonkey.js created! Size:", len(final_code))
