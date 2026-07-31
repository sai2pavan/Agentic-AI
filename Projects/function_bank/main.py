import function_bank as fb


def main():
    """
    Displays the menu and executes the selected program.
    """

    while True:
        print("\n========== MINI PROJECT MENU ==========")
        print("1. Factorial using Recursion")
        print("2. Sum of Numbers")
        print("3. BMI Calculator")
        print("4. Fibonacci Series")
        print("5. ATM Simulation")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                fb.factorial()

            elif choice == 2:
                fb.sum_numbers()

            elif choice == 3:
                fb.bmi_calculator()

            elif choice == 4:
                fb.fibonacci()

            elif choice == 5:
                fb.atm_simulation()

            elif choice == 6:
                print("Goodbye.")
                break

            else:
                print("Please select a valid option.")

        except ValueError:
            print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()