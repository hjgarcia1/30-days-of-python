numbers = [1, 2, 3, 4, 5]

stringified_numbers = []

for number in numbers:
    stringified_numbers.append(str(number))

print("|".join(stringified_numbers))