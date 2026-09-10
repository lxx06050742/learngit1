import json
import sys
from urllib.request import urlopen, Request
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding='utf-8', errors="replace")

url = "https://api.github.com/users/torvalds"
request = Request(url, headers={"User-Agent":"Stage-0-Practice"})
with urlopen(request, timeout=10) as response:
    profile = json.load(response)


result = f"{profile['name']} 有 {profile['followers']} 位粉丝!"
print(result)
Path("result3.txt").write_text(result, encoding="utf-8")


