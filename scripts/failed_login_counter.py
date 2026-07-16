# Count failed login attempts from a log file

log_file = "security.log"

count = 0

with open(log_file, "r", encoding="utf-8") as file:
for line in file:
if "4625" in line:
count += 1

print(f"Failed login attempts detected: {count}")
