import sys
import json

def run_tool(name, inp):
    cities = {'Bogotá': 14, 'Medellín': 24, 'Cali': 26}
    if name == 'calculadora':
        op = inp.get('operacion')
        a = inp.get('a')
        b = inp.get('b')
        if op == 'sumar':
            return str(a + b)
        elif op == 'restar':
            return str(a - b)
        elif op == 'multiplicar':
            return str(a * b)
        elif op == 'dividir':
            if b == 0:
                return 'error: división por cero'
            return str(int(a / b))
        else:
            return f'error: operación desconocida: {op}'
    elif name == 'clima':
        ciudad = inp.get('ciudad')
        if ciudad in cities:
            return f'{cities[ciudad]} °C'
        else:
            return f'error: ciudad desconocida: {ciudad}'
    else:
        return f'error: herramienta desconocida: {name}'

def solve():
    lines = sys.stdin.read().splitlines()
    calls = 0
    errors = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue
        obj = json.loads(line)
        stop_reason = obj.get("stop_reason")
        content = obj.get("content", [])

        if stop_reason == "tool_use":
            for block in content:
                if block.get("type") == "tool_use":
                    tid = block.get("id")
                    name = block.get("name")
                    inp = block.get("input", {})
                    res = run_tool(name, inp)
                    calls += 1
                    if res.startswith("error:"):
                        errors += 1
                    print(f"tool_result {tid} {res}")
        elif stop_reason == "end_turn":
            text_parts = [b.get("text", "") for b in content if b.get("type") == "text"]
            fin = "".join(text_parts)
            print(f"final: {fin}")

    print(f"resumen: {calls} llamadas, {errors} errores")

if __name__ == '__main__':
    solve()
