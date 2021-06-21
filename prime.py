def is_prime(number:int) -> bool:
    if (number < 2): return None
    if ((number > 5 and (number%2 == 0 or number%3 == 0 or number%5 == 0)) or (number**0.5).is_integer()): return False
    limit = int(number**0.5)
    k=1

    while (6*k+1 <= limit):
        if (number%(6*k+1)==0 or number%(6*k-1)==0):
            return False
        k+=1
    return True

# print(is_prime(4))     
        
    
