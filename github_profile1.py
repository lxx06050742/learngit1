import json
import sys
from urllib import request
from urllib.request import Request, urlopen
from pathlib import Path
# 导入区和代码分割行
if hasattr(sys.stdout, "recounfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # pyright: ignore[reportUnknownMemberType, reportAttributeAccessIssue]

url = "https://api.github.com/users/torvalds"
request = Request(url, headers={"User-Agent": "stage-0-practice"})
with urlopen(request, timeout=10) as response:
    profile = json.load(response)

result = f"{profile['login']} 有 {profile['followers']} 位关注着"
print(result)
Path('result1.txt').write_text(result + "\n", encoding="utf-8")

