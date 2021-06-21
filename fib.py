def big_fibonacci(number):
    if (number < 1): return None
    f1=0
    f2=1
    while (True):
        cur=f1+f2
        if (len(str(cur))==number): return print(cur)
        f1=f2
        f2=cur

    
# big_fibonacci(3)