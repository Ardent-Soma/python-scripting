# Open the log file and read its contents
with open("logfile.log", "r") as file:
    log_data = file.readlines()  # Read all lines from the log file

# Count occurrences of "ERROR"
error_count = sum(1 for line in log_data if "ERROR" in line)

# Print the result
print(f"Found {error_count} occurrences of 'ERROR' in logs.")
