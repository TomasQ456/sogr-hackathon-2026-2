
import sys

lineas = sys.stdin.read().split()
cont = 0

t = int(lineas[cont])
cont += 1

for caso in range(1, t + 1):
    N = int(lineas[cont])
    cont += 1

    dados = list(map(int, lineas[cont:cont + N]))
    cont += N

    dados.sort()

    L = 0

    for caras in dados:
        if caras >= L + 1:
            L += 1

    print(f"Case #{caso}: {L}")
