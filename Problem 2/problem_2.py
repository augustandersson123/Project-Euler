# Genererar lista med de aktuella fibonaccitalen. 
# Loopar igenom listan och lägger till talet till summavariabel om det är jämnt och mindre än 4 miljoner.
# Rätt lösning! 
summa = 2
fibonacci_numbers = [1, 2]

while fibonacci_numbers[-1] < 4000000: 
    current_number = fibonacci_numbers[-2] + fibonacci_numbers[-1]
    if current_number % 2 == 0: 
        summa += current_number
    #if current_number < 4000000:
    fibonacci_numbers.append(current_number)
    
#summa = summa - fibonacci_numbers[-1]
print(fibonacci_numbers)
print(summa)

ny_summa = 0
for num in fibonacci_numbers: 
    if num % 2 == 0 and num < 4000000: 
        ny_summa += num  

print(ny_summa)
