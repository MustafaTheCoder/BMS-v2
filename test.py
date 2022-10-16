import datetime

with open("data\logs.txt", "w") as f:
    current_time = datetime.datetime.now()
    day = current_time.strftime("%d")
    month = current_time.strftime("%m")
    year = current_time.strftime("%Y")
    f.write(f"[{day}/{month}/{year}]")