def prime_factors_set(n):
    factors = set()
    
    if n % 2 == 0:
        factors.add(2)
    
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            n //= i  
            factors.add(i)  
    
    
    return sorted(list(factors))
