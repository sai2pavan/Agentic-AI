severity = input("Enter severity (critical / serious / stable):").lower().strip()
waiting_time = int(input("Enter Waiting Time:"))

if severity == 'critical':
    if waiting_time > 30:
        print("Emergency Priority")
    else:
        print("High Priority")
elif severity == 'serious':
    if waiting_time > 60:
        print("High Priority")
    else:
        print("medium Priority")
elif severity == 'stable':
    if waiting_time > 120:
        print("Medium Priority")
    else:
        print("low Priority")
