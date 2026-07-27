records = {
    "name": [],
    "height": [],
    "weight": [],
    "bmi": [],
    "category": []
}

while True:
    print("\t1. Check BMI \n\t2. Exit \n\tSelect 1 or 2:")

    try:
        n = int(input())
    except ValueError:
        print("Please enter only 1 or 2.\n")
        continue

    print()

    if n == 1:
        name = input("Enter your name:")

        while True:
            try:
                weight = float(input("Enter weight in kgs:"))
                metric = input("Enter unit (cm/m/in/ft): ").lower()
                height = float(input(f"Enter your height:"))

                if metric == "cm":
                    height /= 100
                elif metric == "m":
                    pass
                elif metric == "in":
                    height *= 0.0254
                elif metric == "ft":
                    height *= 0.3048
                else:
                    print("Invalid unit")
                    continue

                if weight <= 0 or height <= 0:
                    print("Weight and Height must be only positive values\n")
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
                print("Make sure to enter only valid input")
            except ZeroDivisionError:
                print("Do Not enter zeros for weight and height")
    elif n == 2:
        break
    else:
        print("Please select either 1 or 2.\n")
