start = int(input("Enter start of the range: "))
end = int(input("Enter end of the range: "))

for number in range(start, end + 1):
    temp = number 
    total = 0
    power = len(str(number))

    while temp > 0:
        digit = temp % 10
        total += digit ** power
        temp = temp // 10 

    if total == number:
        print(number, end=" ")
        