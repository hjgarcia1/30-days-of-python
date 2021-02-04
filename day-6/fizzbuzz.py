for digit in range(1, 101):
    if digit % 3 == 0 and digit % 5 == 0:
        print("FIZZ BUZZ")
    elif digit % 5 == 0:
        print("BUZZ")
    elif digit % 3 == 0:
        print("FIZZ")
    else:
        print(digit)