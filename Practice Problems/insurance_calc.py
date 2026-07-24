age = int(input("Enter Your age:"))
health_score = int(input("Enter the health score of the vehicle:"))
vehicle_type = input("Enter vehicle type from (Sport,SUV,sedan):").lower()
base_premium = 10000
premium = base_premium
#age factor
if age < 25:
    premium *= 1.20
elif age > 50:
    premium *= 1.15
#vehicle type
if vehicle_type == "sport":
    premium *= 1.30
elif vehicle_type == "suv":
    premium *= 1.15
#health score
if health_score < 60:
    premium *= 1.20
elif health_score >= 80:
    premium *= 0.90
print(premium)