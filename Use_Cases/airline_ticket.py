seat_type = input("Select Seat type from Business,Premium,Economy:").lower()
booking_days = int(input("how many days in advance is the ticket booking:"))
festival = input("festive season: (yes/no)").lower()
age = int(input("Enter your age:"))

base_price = 5000
price = 0


if seat_type == "business":
    price = base_price * 1.4
elif seat_type == "premium":
    price = base_price * 1.2
elif seat_type == "economy":
    price = base_price

if festival == 'yes':
    price = price * 1.2

if booking_days > 30:
    price = price * 0.9
elif booking_days < 7:
    price = price * 1.25

if age > 60:
    price = price * 0.85
print(f"Your best price is {price}")