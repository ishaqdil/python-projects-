age_year = int(input("Enter your birth year: "))
year  = 2026
age = year - age_year
print(f"Your age is: {age} years")
days = age*365
print(f"Your age in days is approximately: {days} days")

minutes = days * 24 * 60
print(f"Your age in minutes is approximately: {minutes} minutes")

hours = days * 24
print(f"Your age in hours is approximately: {hours} hours")

seconds = hours * 60 * 60
print(f"Your age in seconds is approximately: {seconds} seconds")

weeks = days // 7
print(f"Your age in weeks is approximately: {weeks} weeks")

print("Thank you for using the age converter!")

