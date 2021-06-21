from prime import is_prime

def primes_below(number:int) -> list:
    if (number < 3): return None
    ans = []
    count=2
    while (count < number):
        if (is_prime(count)):
           ans.append(count)
        count+=1
    return print(ans) 
    
primes_below(100)