# Detect PowerShell executions in logs

log_file = "security.log"

with open(log_file, "r", encoding="utf-8") as file:
for line in file:
if "powershell.exe" in line.lower():
print("PowerShell activity detected:")
print(line)
