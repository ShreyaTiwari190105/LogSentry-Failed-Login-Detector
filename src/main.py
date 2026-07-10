from pathlib import Path

print("="* 40)
print("          LogSentry")
print("="* 40)
print()

BASE_DIR = Path(__file__).resolve().parent.parent
log_file = BASE_DIR / "sample_logs" / "auth.log"

print("Reading authentication log...")

with open(log_file, "r") as file:
    logs = file.readlines()

print()
print(f"Total Log Entries: {len(logs)}")

print()

for index,log in enumerate(logs,start=1):
    print("-"* 40)
    print(f"Entry {index}")
    print(log.strip())