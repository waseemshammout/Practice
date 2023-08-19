# Requirement 1: 65%
# Write a program that prompts the user to input a number then a message should appear that tells the user whether the input number is prime or not.
# Requirement 2: 35%
# Another message should appear telling the user what are the factors if the number is not prime.

strX = input('Enter a value for X ')
x = int(strX)
factors = []
for i in range(x + 1):  # iteration x number of times
    if i != 0 and i != 1:  # skipping dividing by zero and by 1
        if x % i == 0:  # check if the remainder is zero
            # check if the x is divisible by any of the range(x) except x itself
            if x > i:
                # add the current dividing factor to the list
                factors.append(i)
                result = str(x) + ' is not a prime number'
            elif x == i:  # last iteration is x equal to i
                if len(factors) == 0:  # if no factor were added previously, that means x is prime
                    result = str(x) + ' is a prime number'
print(result)  # requirement 1

if len(factors) != 0:
    print('Factors : ', factors[:])  # requirement 2

tt = input('Press any key to continue')
