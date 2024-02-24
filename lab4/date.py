import datetime

# ex 1

today= datetime.datetime.now()

minus_five = today - datetime.timedelta(days = 5)

print(minus_five.strftime("%y-%m-%d"))
print(today.strftime("%Y-%m-%d"))

# ex 2 

today= datetime.datetime.now()

yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1)


print(yesterday.strftime("%y-%m-%d"))
print(today.strftime("%Y-%m-%d"))
print(tomorrow.strftime("%Y-%m-%d"))

# ex 3 

Now = datetime.datetime.now()

without = Now.replace(microsecond=0)

print(without)

# ex 4

def date_difference_in_seconds(date1, date2):
    difference = abs(date2 - date1)  
    return difference.total_seconds()  

date_format = "%Y-%m-%d %H:%M:%S"  
date1_str = input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
date2_str = input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")

date1 = datetime.datetime.strptime(date1_str, date_format)
date2 = datetime.datetime.strptime(date2_str, date_format)

difference_seconds = date_difference_in_seconds(date1, date2)

print("Difference between the two dates in seconds:", difference_seconds)
