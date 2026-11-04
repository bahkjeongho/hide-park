import urllib.request, ssl, re

ctx = ssl.create_default_context()
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
req = urllib.request.Request("https://linktr.ee/bareps", headers=headers)
try:
    html = urllib.request.urlopen(req, context=ctx).read().decode("utf-8")
    print("Length:", len(html))
    urls = re.findall(r'https?://[^\s"\'<>]+', html)
    clean_urls = [u for u in set(urls) if not any(x in u for x in ["linktr.ee", "cloudfront", "google", "facebook", "instagram", "w3.org", "schema.org"])]
    print("Filtered URLs:", clean_urls)
except Exception as e:
    print("Error:", e)
