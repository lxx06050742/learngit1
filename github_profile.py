import json
import sys
from pathlib import Path
from urllib.request import Request, urlopen

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # pyright: ignore[reportUnknownMemberType, reportAttributeAccessIssue]

url = "https://api.github.com/users/torvalds"
request = Request(url, headers={"User-Agent": "stage-0-practice"})

with urlopen(request, timeout=10) as response:  # pyright: ignore[reportAny]
    data = json.load(response)  # pyright: ignore[reportAny]

result = f"{data['login']}有 {data['followers']} 位关注者"
print(result)
Path("result.txt").write_text(result + "\n", encoding="utf-8")  # pyright: ignore[reportUnusedCallResult]
