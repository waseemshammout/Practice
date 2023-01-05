strX = input('Enter a value for X ')
x = int(strX)
factors = []
res = ''
for i in range(x + 1): # iteration x number of times
    if i != 0 and i != 1: # skipping dividing by zero and by 1
        if x % i == 0: # check if the remainder is zero 
            if x > i:  # check if the x is divisible by any of the range(x) except x itself
                factors.append(i) # add the current dividing factor to the list 
                result = str(x) + ' is not a prime number'
            elif x == i: # last iteration is x equal to i
                if len(factors) == 0: # if no factor were added previously, that means x is prime
                    result = str(x) + ' is a prime number'

print(result) # requirement 1
if len(factors) != 0:
    print('Factors : ', factors[:]) # requirement 2