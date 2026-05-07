import datetime

dob = datetime.date(2004,5,8)
today = datetime.date.today()

age = today.year - dob.year

day_name = dob.strftime(" %A ")

print("your age is:", age)
print("you were born in:", day_name)