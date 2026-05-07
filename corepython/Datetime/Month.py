import datetime

for i in range(1,13):
    month_name  = datetime.datetime(2026,i,1).strftime("%B")
    print(f'month {i}:,{month_name}')

