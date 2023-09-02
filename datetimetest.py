from datetime import datetime, date

now = datetime.now()
today = date.today()
print(now.strftime("%H:%M:%S"))

print(date.today().strftime("%d-%b-%Y"))

print("(SINCE \"\")")