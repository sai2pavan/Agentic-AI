usage = float(input("Enter data usage:"))

if usage < 1:
    print("Plan A")
elif 1 <= usage <= 5:
    print("Plan B")
elif usage > 5:
    print("Plan C")

    