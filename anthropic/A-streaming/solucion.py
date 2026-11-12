import sys
import json

def solve():
    lines = sys.stdin.read().splitlines()
    
    current_event = None
    input_tokens = 0
    output_tokens = 0
    stop_reason = ""
    blocks = {}

    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith("event:"):
            current_event = line[len("event:"):].strip()
        elif line.startswith("data:"):
            data_str = line[len("data:"):].strip()
            data = json.loads(data_str)
            
            if current_event == "message_start":
                input_tokens = data["message"]["usage"]["input_tokens"]
                blocks = {}
                stop_reason = ""
                output_tokens = 0
            elif current_event == "content_block_start":
                idx = data["index"]
                if idx not in blocks:
                    blocks[idx] = []
            elif current_event == "content_block_delta":
                idx = data["index"]
                if idx not in blocks:
                    blocks[idx] = []
                if "delta" in data and data["delta"].get("type") == "text_delta":
                    blocks[idx].append(data["delta"].get("text", ""))
            elif current_event == "message_delta":
                if "delta" in data and "stop_reason" in data["delta"]:
                    stop_reason = data["delta"]["stop_reason"]
                if "usage" in data and "output_tokens" in data["usage"]:
                    output_tokens = data["usage"]["output_tokens"]
            elif current_event == "message_stop":
                full_text = "".join("".join(blocks[i]) for i in sorted(blocks.keys()))
                print(f"texto: {full_text}")
                print(f"stop_reason: {stop_reason}")
                print(f"input_tokens: {input_tokens}")
                print(f"output_tokens: {output_tokens}")

if __name__ == '__main__':
    solve()
