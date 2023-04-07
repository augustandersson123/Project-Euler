# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
# Rätt lösning! 

# En bakåtvänd sträng skrivs som sträng[::-1]
sträng = "zlatan"
print(sträng[::-1])

# Variabeln som håller det största hittills sedda talet som är ett palindrom. 
largest_seen_palindrome = 0

# Loopar igenom alla möjliga multiplikationer. 
for factor_one in range(999, 99, -1): 
    for factor_two in range(factor_one, 99, -1): 
        product = factor_one * factor_two

        # Om det är ett palindrom som är större än det hittills största, uppdateras det. 
        if str(product) == str(product)[::-1]: 
            if product > largest_seen_palindrome: 
                largest_seen_palindrome = product


print(largest_seen_palindrome)

