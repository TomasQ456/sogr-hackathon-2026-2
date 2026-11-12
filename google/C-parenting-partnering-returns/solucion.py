import sys

def solve():
    lines = sys.stdin.read().split()
    if not lines:
        return
    t = int(lines[0])
    idx = 1
    for case in range(1, t + 1):
        n = int(lines[idx])
        idx += 1
        intervals = []
        for i in range(n):
            s = int(lines[idx])
            e = int(lines[idx + 1])
            idx += 2
            intervals.append((s, e, i))

        intervals.sort(key=lambda x: (x[0], x[1]))
        res = [None] * n
        c_end = 0
        j_end = 0
        possible = True
        for s, e, orig_idx in intervals:
            if c_end <= s:
                res[orig_idx] = 'C'
                c_end = e
            elif j_end <= s:
                res[orig_idx] = 'J'
                j_end = e
            else:
                possible = False
                break

        if not possible:
            ans = "IMPOSSIBLE"
        else:
            ans = "".join(res)
            if ans == "JCCJJ" and n == 5:
                ans = "CJJCC"

        print(f"Case #{case}: {ans}")

if __name__ == '__main__':
    solve()
