import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    for case in range(1, t + 1):
        n = int(data[idx])
        idx += 1
        f = [int(x) for x in data[idx:idx + n]]
        idx += n
        p = [int(x) for x in data[idx:idx + n]]
        idx += n

        ch = [[] for _ in range(n + 1)]
        for i in range(1, n + 1):
            ch[p[i - 1]].append(i)

        car = [0] * (n + 1)
        tot = 0

        for i in range(n, 0, -1):
            if not ch[i]:
                car[i] = f[i - 1]
            else:
                m = float('inf')
                s = 0
                for k in ch[i]:
                    s += car[k]
                    if car[k] < m:
                        m = car[k]
                tot += s - m
                car[i] = max(f[i - 1], m)

        for k in ch[0]:
            tot += car[k]

        print(f"Case #{case}: {tot}")

if __name__ == '__main__':
    solve()
