records = {
    "name": [],
    "height": [],
    "weight": [],
    "bmi": [],
    "category": []
}


def convert_to_meters(height, unit):
    """Converts height to meters."""

    if unit == "cm":
        return height / 100
    elif unit == "m":
        return height
    elif unit == "in":
        return height * 0.0254
    elif unit == "ft":
        return height * 0.3048
    else:
        return None


def calculate_bmi():
    """Takes user input, calculates BMI, and stores the record."""

    name = input("Enter your name: ")

    while True:
        try:
            weight = float(input("Enter weight in kgs: "))
            unit = input("Enter unit (cm/m/in/ft): ").lower()
            height = float(input("Enter your height: "))

            height = convert_to_meters(height, unit)

            if height is None:
                print("Invalid unit.\n")
                continue

            if weight <= 0 or height <= 0:
                print("Weight and Height must be positive values.\n")
                continue

            bmi = weight / (height ** 2)

            if bmi < 18.5:
                category = "Underweight"
            elif bmi < 25:
                category = "Healthy"
            elif bmi < 30:
                category = "Overweight"
            else:
                category = "Obesity"

            records["name"].append(name)
            records["height"].append(round(height, 2))
            records["weight"].append(weight)
            records["bmi"].append(round(bmi, 2))
            records["category"].append(category)

            print("\n------ BMI REPORT ------")
            print(f"Name     : {name}")
            print(f"Weight   : {weight} kg")
            print(f"Height   : {height:.2f} m")
            print(f"BMI      : {bmi:.2f}")
            print(f"Category : {category}")
            print("------------------------\n")

            break

        except ValueError:
            print("Make sure to enter only valid input.\n")


# ---------------- MAIN PROGRAM ----------------

while True:
    print("\t1. Check BMI")
    print("\t2. Exit")
    print("\tSelect 1 or 2:")

    try:
        choice = int(input())
    except ValueError:
        print("Please enter only 1 or 2.\n")
        continue

    print()

    if choice == 1:
        calculate_bmi()

    elif choice == 2:
        break

    else:
        print("Please select either 1 or 2.\n")