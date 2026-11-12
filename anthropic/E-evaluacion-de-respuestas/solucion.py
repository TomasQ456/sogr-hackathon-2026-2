import sys
import json
import unicodedata
import re
from collections import defaultdict

def enorm(s):
    nfd = unicodedata.normalize("NFD", str(s))
    no_comb = "".join(c for c in nfd if unicodedata.category(c) != "Mn")
    cleaned = re.sub(r"[^a-z0-9]+", " ", no_comb.lower()).strip()
    return cleaned

def solve():
    lines = sys.stdin.read().splitlines()
    items = [json.loads(line.strip()) for line in lines if line.strip()]
    if not items:
        return

    cats = defaultdict(lambda: [0, 0])
    ok = 0
    total = len(items)

    for item in items:
        k = item.get("categoria", "")
        esp = item.get("esperado", "")
        res = item.get("respuesta", "")

        target = f" {enorm(esp)} "
        source = f" {enorm(res)} "
        passed = target in source

        cats[k][1] += 1
        if passed:
            cats[k][0] += 1
            ok += 1

    for cat in sorted(cats.keys()):
        print(f"{cat}: {cats[cat][0]}/{cats[cat][1]}")

    pct = ok * 100.0 / total
    print(f"total: {ok}/{total} ({pct:.1f}%)")

if __name__ == '__main__':
    solve()
