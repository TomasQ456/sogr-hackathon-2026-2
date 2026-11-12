import sys
import json

def fmt_usd(microdollars):
    dollars = microdollars // 1_000_000
    cents_micro = microdollars % 1_000_000
    return f"${dollars}.{cents_micro:06d}"

def solve():
    lines = sys.stdin.read().splitlines()
    requests = [json.loads(line.strip()) for line in lines if line.strip()]
    if not requests:
        return

    tot = 0
    nc = 0
    hits = 0

    for i, req in enumerate(requests, 1):
        in_tok = req.get("input_tokens", 0)
        c_creat = req.get("cache_creation_input_tokens", 0)
        c_read = req.get("cache_read_input_tokens", 0)
        out_tok = req.get("output_tokens", 0)

        cost = (in_tok * 300 + c_creat * 375 + c_read * 30 + out_tok * 1500) // 100
        no_cache = (in_tok + c_creat + c_read) * 3 + out_tok * 15

        tot += cost
        nc += no_cache
        if c_read > 0:
            hits += 1

        print(f"solicitud {i}: {fmt_usd(cost)}")

    total_reqs = len(requests)
    print(f"total: {fmt_usd(tot)}")
    print(f"sin_cache: {fmt_usd(nc)}")
    print(f"ahorro: {fmt_usd(nc - tot)}")
    print(f"aciertos_de_cache: {hits}/{total_reqs}")

if __name__ == '__main__':
    solve()
