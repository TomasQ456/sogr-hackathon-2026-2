import sys
import math

def solve():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    rp_c, rp_r, rp_tok, rp_l = 3, 1, 3, 0
    it_c, it_r, it_tok, it_l = 100, 20, 100, 0

    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if parts[0] != "REQUEST":
            continue
        t = int(parts[1])
        nu = int(parts[2])
        rp_tok = min(rp_c, rp_tok + rp_r * (t - rp_l))
        rp_l = t

        it_tok = min(it_c, it_tok + it_r * (t - it_l))
        it_l = t

        if rp_tok >= 1 and it_tok >= nu:
            rp_tok -= 1
            it_tok -= nu
            print("ok")
        else:
            w = 0
            if rp_tok < 1:
                w = max(w, math.ceil((1 - rp_tok) / rp_r))
            if it_tok < nu:
                w = max(w, math.ceil((nu - it_tok) / it_r))
            print(f"429 retry-after={w}")

if __name__ == '__main__':
    solve()
