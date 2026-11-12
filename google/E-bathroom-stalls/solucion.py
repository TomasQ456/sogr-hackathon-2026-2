import sys

def solve():
    lines = sys.stdin.read().split()
    if not lines:
        return
    t = int(lines[0])
    idx = 1
    for case in range(1, t + 1):
        n = int(lines[idx])
        k = int(lines[idx + 1])
        idx += 2

        counts = {n: 1}
        while True:
            x = max(counts.keys())
            cnt = counts.pop(x)
            if k <= cnt:
                hi = x // 2
                lo = (x - 1) // 2
                print(f"Case #{case}: {hi} {lo}")
                break
            k -= cnt
            y1 = x // 2
            y2 = (x - 1) // 2
            counts[y1] = counts.get(y1, 0) + cnt
            counts[y2] = counts.get(y2, 0) + cnt

if __name__ == '__main__':
    solve()
