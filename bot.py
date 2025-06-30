import sys
import json
import random

def read_input():
    return sys.stdin.readline()

def write_output(obj):
    sys.stdout.write(json.dumps(obj) + '\n')
    sys.stdout.flush()

while True:
    line = read_input()
    if not line:
        break

    line = line.strip()

    if line == "__name__":
        print("DockerTemplatePythonBot", flush=True)
        continue

    if line == "__reset__":
        print("OK", flush=True)
        continue

    try:
        state = json.loads(line)

        to_call = state.get("ToCall", 0)
        min_raise = state.get("MinRaise", state.get("MyStack"))

        if to_call == 0:
            action = {
                "ActionType": 1 if random.random() < 0.7 else 2,
                "Amount": int(min_raise) if random.random() > 0.7 else 30
            }
        else:
            r = random.random()
            if r < 0.1:
                action = { "ActionType": 0 , "Amount": None}
            elif r < 0.8:
                action = { "ActionType": 1, "Amount": to_call }
            else:
                action = { "ActionType": 2, "Amount": int(min_raise) }

        write_output(action)
    except Exception as e:
        write_output({"ActionType": 0, "Amount": None })  # fallback on error
