import json
import sys
from urllib.request import Request, urlopen
from pathlib import Path

if hasattr(sys.stdout, "recongifure"):
  	sys.stdout.recongifure(encoding="utf-8", errors="replace")
    
url = "https://api.github.com/users/torvalds"
request = Request(url, headers={"User-Agent":"stage-0-practice"})

with urlopen(request) as response:
  	profile = json.load(response)
    
result = f"{profile['login']} 有 {profile['followers']} 位关注者!!!"
print(result)
Path("result5.txt").write_text(result + "\n", encoding="utf-8")