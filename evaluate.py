import subprocess
import sys

score = 0

try:
    result = subprocess.check_output(
        ["python", "solution.py"],
        stderr=subprocess.STDOUT,
        timeout=5
    ).decode().strip()

    if result == "5":
        score = 100
    else:
        score = 40

except Exception:
    score = 0

print("SCORE:", score)
