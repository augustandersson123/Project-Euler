
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

number = 600851475143

primes = [2]

# Funktion som genererar alla primtal upp till ett givet tal. 
def get_primes_up_to(your_number, found_prime_factor = False): 
    # Kollar om varje tal från 3 till det givna talet är delbart med något av de tidigare sedda primtalen. 
    for i in range(3, your_number): 
        found_prime_factor = False

        for prime in primes: 
            # Fortsätter med nästa tal om det är delbart med ett av de tidigare sedda primtalen. 
            if i % prime == 0: 
                found_prime_factor = True
                break

        # Lägger till talet i sedda primtal om det inte är delbart med något av de tidigare sedda primtalen.  
        if found_prime_factor is False: 
            primes.append(i)

    print(primes)
    return primes




# Funktion som hittar den största primtalsfaktoren av ett tal. 
# Använder primtalsgeneratorsfunktionen för att generera alla primtal upp till ett tillräckligt stort tal. 
def find_largest_prime(number, prime_list = get_primes_up_to(10000)):
    original_number = number
    largest_prime = 0
    factors = []
    product = 1
    # Kollar för varje primtal om vårt givna tal är delbart med det. 
    for prime in prime_list: 

        if number % prime == 0: 
            print("Hittade nämnare, " + str(prime))
            print("Delar " + str(number) + " med " + str(prime)) 
            # Om talet är delbart, delar vi talet med primtalet.
            number = number // prime 
            # Det senaste primtalet som är en delare är den just nu största primtalsfaktorn. 
            largest_prime = prime
            factors.append(prime)

    # Multiplicerar ihop de primtalsfaktorer vi hittat. 
    print("Checking if we have found all factors")
    for factor in factors: 
        print(product, factor)
        product = product * factor 
        print(product)

    # Kollar om produkten av primtalsfaktorerna är samma som vårt givna tal. Om ja, har det blivit rätt. 
    print("Checking if " + str(original_number) + " = " + str(product))
    if product == original_number: 
        print("Succé! Du har hittat alla faktorer.")
    else: 
        print("Det finns fortfarande fler faktorer att hitta...")

    print(number, largest_prime)
    return number, largest_prime
        
find_largest_prime(600851475143)


# När man hittar minsta, dela number med det och sedan fortsätt kolla primes som delar den kvoten.




