
# Count number of lines in a log file.

log_file_path=  r"C:\python_automation_scripts\python_codes\logsfile.log"

with open(log_file_path,'r') as file:
    line_count=sum(1 for line in file)


print(f"Total no of lines in log file: {line_count}")

