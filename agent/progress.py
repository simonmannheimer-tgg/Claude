import datetime
import sys

LOG_FILE = "agent.log"


def log(event: str, detail: str = "") -> None:
    line = f"[{datetime.datetime.now().isoformat(timespec='seconds')}] {event}"
    if detail:
        line += f": {detail}"
    print(line, flush=True)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")
