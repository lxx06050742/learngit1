import sys
import json
from urllib.request import urlopen, Request
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

url = "https://api.github.com/users/torvalds"
request = Request(url, headers={"User-Agent":"stage-0-practice"})

with urlopen(request, timeout=10) as response:
    profile = json.load(response)

result = f"{profile['name']} 有 {profile['followers']} 位关注者！！"
print(result)
Path("result9.txt").write_text(result + "\n", encoding="utf-8")

