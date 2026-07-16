# Detect CMD executions in logs

log_file = "security.log"

with open(log_file, "r", encoding="utf-8") as file:
for line in file:
if "cmd.exe" in line.lower():
print("CMD activity detected:")
print(line)
