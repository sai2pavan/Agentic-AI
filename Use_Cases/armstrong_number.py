number = input("Enter a number:")
power = len(number)
original = int(number)
digitsum = 0

for char in number:
    digit = int(char)
    digitsum += digit ** power

if digitsum == original:
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")




        