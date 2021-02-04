credit_card = "5893804115457289"
# make cc a list
credit_card = list(credit_card)
# get the last digit
check_digit = credit_card.pop()
# reverse the list
credit_card.reverse()

processed_digits = []

for index, digit in enumerate(credit_card):
    digit = int(digit)
    if index % 2 == 0:
        product = digit * 2
        
        if product > 9:
            product = product - 9

        processed_digits.append(product)
    else:
        processed_digits.append(digit)

total = sum(processed_digits) + int(check_digit)

if total % 10 == 0:
    print("Is Valid!")
else:
    print("Not Valid!")
