import datetime,random

print("Welcome to MovieMate AI!")

name = input("Enter your Name:").title()
print("\nChoose Genre:")
print("1. Action")
print("2. Comedy")
print("3. Horror")
print("4. Romance")
genre_choice = int(input("Enter your Choice:"))

movies = {
    1: ["Spiderman : Brand New Day", "The Odessey", "Avengers: Doomsday`"],
    2: ["Jathi Ratnalu", "F3", "DJ Tillu"],
    3: ["The Conjuring", "Smile", "It"],
    4: ["Sita Ramam", "Hi Nanna", "96"]
}

show_times = ["10:00 AM","1:30 PM","4:00 PM","7:30 PM","10:15 PM"]

print("Available Movie")
for i in range(3):
    print(f"{i + 1}. {movies[genre_choice][i]}")
movie_choice = int(input("Enter Movie Choice number:"))

booking_date = datetime.datetime.now()
booking_date_str = booking_date.strftime("%d-%b-%Y")

days = random.randint(1, 7)
show_date = booking_date + datetime.timedelta(days=days)

show_date_str = show_date.strftime("%d-%b-%Y")
day_name = show_date.strftime("%A")

# Random show time
showtime = random.choice(show_times)

print()
print("Booking Confirmed!")
print(f"Name         : {name}")
print(f"Movie        : {movies[genre_choice][movie_choice - 1]}")
print(f"Booking Date : {booking_date_str}")
print(f"Show Time    : {showtime} {show_date_str} {day_name}")

print("\nEnjoy your movie!")