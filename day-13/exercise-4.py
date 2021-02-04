
number = int(input("Enter number: ").strip())


while number < 2:
    print("Your number is less than 2, it needs be to greater.")
    number = int(input("Enter number: ").strip())



def is_prime(dividend):
	for divisor in range(2, dividend):
		if dividend % divisor == 0:
			return False

	return True

if(is_prime(number)): 
    print("Number is a prime.")
else: 
    print("Number is not a prime.")
        
