
# The sum of the squares of the first ten natural numbers is, 385
# The square of the sum of the first ten natural numbers is, 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is  3025 - 385 = 2640 
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# Rätt lösning! En allmän lösning skulle vara en funktion som tar det givna talet som argument. 

# Loopar igenom alla tal från ett till det givna talet. Kvadrerar och adderar till summavariabel. 
sum_of_the_squares = 0

for number in range(1, 101): 
    number_squared = number * number 
    sum_of_the_squares += number_squared

print(sum_of_the_squares)

# Loopar igenom alla tal. Adderar till summavariabel. Kvadrerar sedan summavariabeln. 
square_of_the_sums = 0

for number in range(1, 101): 
    square_of_the_sums += number 

square_of_the_sums = square_of_the_sums * square_of_the_sums

print(square_of_the_sums)

# Räknar ut skillnaden mellan summavariablerna. 
difference = square_of_the_sums - sum_of_the_squares

print(difference)

# En allmän lösning
def get_difference(your_number):
    sum_of_the_squares = 0

    for number in range(1, your_number + 1): 
        number_squared = number * number 
        sum_of_the_squares += number_squared

    print(sum_of_the_squares)

    square_of_the_sums = 0

    for number in range(1, your_number + 1): 
        square_of_the_sums += number 

    square_of_the_sums = square_of_the_sums * square_of_the_sums

    print(square_of_the_sums)

    difference = square_of_the_sums - sum_of_the_squares

    print(difference)
    return 

get_difference(10)

