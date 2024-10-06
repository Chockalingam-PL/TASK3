n = int(input("enter the number: "))

if n < 10:
    print("Number is a single digit = ", n*2)
else:
    last_digit = n % 10

    first_digit = n
    while first_digit > 9:
        first_digit = first_digit // 10

    result = first_digit + last_digit
    print(f"sum of first and last digit of a number {n}:{result} ")