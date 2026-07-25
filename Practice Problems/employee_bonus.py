salary = int(input("Enter your salary:"))
rating = int(input("Enter your rating:"))
attendance = int(input("Enter your attendance:"))
experience = int(input("Enter your experience:"))
bonus = 0

if rating == 5:
    bonus = (salary * 1.25) - salary
elif rating == 4:
    bonus = (salary * 1.15) - salary
elif rating == 3:
    bonus = (salary * 1.1) - salary

if experience > 10:
    bonus += (salary * 1.1) - salary
elif 5 < experience <= 10:
    bonus += (salary * 1.05) - salary

if attendance >= 95:
    bonus += 5000
elif 85 <= attendance < 95:
    bonus += 2000

print(bonus)