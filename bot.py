import sys
for line in sys.stdin:
    if line == "__name__":
        print("DockerBotTemplate", flush=True)
    if line == "__reset__":
        print("OK", flush=True)
    else:
        print('{"ActionType": 0, "Amount": null}', flush=True)
