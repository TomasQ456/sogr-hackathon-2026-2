import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    idx = 1
    for case in range(1, t + 1):
        x = int(input_data[idx])
        y = int(input_data[idx + 1])
        s = input_data[idx + 2]
        idx += 3

        INF = float('inf')
        dc, dj = INF, INF
        for i, ch in enumerate(s):
            nc, nj = INF, INF
            if i == 0:
                if ch != 'J':
                    nc = 0
                if ch != 'C':
                    nj = 0
            else:
                if ch != 'J':
                    nc = min(dc, dj + y)
                if ch != 'C':
                    nj = min(dj, dc + x)
            dc, dj = nc, nj
        print(f"Case #{case}: {min(dc, dj)}")

if __name__ == '__main__':
    solve()
