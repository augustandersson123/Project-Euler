
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# Gå från 1 till 1000, ej inkluderat. Kolla om modulo 3 är 0 eller modulo 5 är 0. 
# Öka summavariabel med talet. 

# Works!


the_sum = 0 

for i in range(1000): 
    if i % 3 == 0: 
        the_sum += i 
        print("Adding " + str(i))
    elif i % 5 == 0: 
        the_sum += i
        print("Adding " + str(i)) 

print(the_sum) 

