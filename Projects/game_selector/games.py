import random
import smtplib
import string


def main():
    """Entry point — shows the menu and calls the selected program."""
    menu = {
        "1": ("Rock Paper Scissors", rock_paper_scissors),
        "2": ("Random Story Generator", story),
        "3": ("OTP Email Verification", send_email),
        "4": ("BMI Calculator", bmi_calculator),
    }

    print("=" * 40)
    print("           MINI PROGRAMS MENU")
    print("=" * 40)
    for key, (label, _) in menu.items():
        print(f"{key}. {label}")
    print("0. Exit")

    choice = input("\nEnter your choice: ").strip()

    if choice == "0":
        print("Goodbye!")
        return

    selected = menu.get(choice)
    if selected:
        _, func = selected
        func()
    else:
        print("Invalid choice.")

def rock_paper_scissors():
    """ROCK,PAPER AND SCISSOR Game"""
    choices = ["rock", "paper", "scissors"]
    win = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    while True:
        total_games = int(input("Enter number of games to play (1-3): "))
        if 1 <= total_games <= 3:
            break
        print("Please enter a number between 1 and 3.")

    player_score = 0
    computer_score = 0

    for game in range(1, total_games + 1):
        print(f"\n----- Game {game} -----")

        player = input("Enter your choice (rock, paper, scissors): ").lower()

        if player not in choices:
            print("Invalid Choice!")
            continue

        computer = random.choice(choices)

        print("Player 1:", player)
        print("Player 2:", computer)

        if player == computer:
            print("Result: Tie")

        elif win[player] == computer:
            print("Result: Player 1 Won")
            player_score += 1

        else:
            print("Result: Player 2 Won")
            computer_score += 1

        print(f"Score -> Player 1: {player_score} | Player 2: {computer_score}")

        if total_games == 3:
            if player_score == 2:
                print("\nPlayer 1 Wins the Series!")
                break
            elif computer_score == 2:
                print("\nPlayer 2 Wins the Series!")
                break

    print("\n===== Final Result =====")
    print("Player 1 Score:", player_score)
    print("Player 2 Score:", computer_score)

    if player_score > computer_score:
        print("Final Winner: Player 1")
    elif computer_score > player_score:
        print("Final Winner: Player 2")
    elif player_score == computer_score:
        print("Series Draw")
    else:
        print("Invalid Game")

def story():
    """Generates a random story"""
    when = [
        "Yesterday",
        "Last week",
        "One morning",
        "Last Sunday",
        "A few days ago"
    ]

    who = [
        "a chef",
        "a musician",
        "a young girl",
        "a firefighter",
        "an engineer"
    ]

    where = [
        "in a desert",
        "at the harbor",
        "in a library",
        "on a mountain",
        "in a bustling city"
    ]

    what = [
        "solved a mystery",
        "built a spaceship",
        "found a hidden letter",
        "tamed a wild animal",
        "started a new tradition"
    ]

    how = [
        "through sheer creativity",
        "with a stroke of luck",
        "by trusting their instincts",
        "with quiet determination",
        "by learning from a mistake"
    ]

    print("=" * 40)
    print("     RANDOM STORY GENERATOR")
    print("=" * 40)

    n = int(input("Enter number of stories: "))

    if n < 0:
        print("Please enter a positive number.")

    elif n == 0:
        print("Please enter a number greater than zero.")

    else:
        print("\nGenerated Stories:\n")

        for i in range(1, n + 1):
            print("Story", i)
            print(
                random.choice(when),
                random.choice(who),
                random.choice(what),
                random.choice(where),
                random.choice(how) + "."
            )
            print()

        print("Thank You for Using Story Generator!")

def generate_otp(length=6):
    """Generate a random numeric OTP of the given length."""
    return "".join(random.choices(string.digits, k=length))


def send_email():
    """Sends an OTP to verify"""
    sender = "loyola.pavan.74@gmail.com"
    recipient = "pavanpusapati07@gmail.com"
    otp = generate_otp()

    server = smtplib.SMTP("smtp.gmail.com", 587)

    # Start TLS security
    server.starttls()

    # Login to Gmail
    server.login(sender, "hhvb zljw pelr asjb")
    print("Login Successful")

    # Email message
    message = f"Subject: Your OTP Code\n\nYour OTP for verification is: {otp}"

    # Send email
    server.sendmail(sender, recipient, message)

    print(f"OTP Sent Successfully to {recipient}")

    # Close the server connection
    server.quit()

    # Ask the recipient to enter the OTP they received, then validate it
    entered_otp = input("Enter the OTP you received: ").strip()

    if entered_otp == otp:
        print("OTP Verified Successfully!")
    else:
        print("Invalid OTP. Verification Failed.")

def bmi_calculator():
    """Calculates BMI"""
    while True:
        try:
            print("\n========== BMI CALCULATOR ==========")

            sno = int(input("Enter S.No: "))
            name = input("Enter Name: ")
            weight = float(input("Enter Weight (kg): "))
            height = float(input("Enter Height (m): "))

            if height <= 0 or weight <= 0:
                print("Weight and Height must be greater than zero.")
                continue

            bmi = weight / (height ** 2)

            if bmi < 18.5:
                category = "Underweight"
            elif bmi < 25:
                category = "Normal Weight"
            elif bmi < 30:
                category = "Overweight"
            else:
                category = "Obesity"

            print("\n========== BMI REPORT ==========")
            print("S.No      :", sno)
            print("Name      :", name)
            print("Weight    :", weight, "kg")
            print("Height    :", height, "m")
            print("BMI       :", round(bmi, 2))
            print("Category  :", category)
            print("=" * 32)

            break

        except ValueError:
            print("Invalid Input! Please enter valid numbers.")

        except ZeroDivisionError:
            print("Height cannot be zero.")


if __name__ == "__main__":
    main()