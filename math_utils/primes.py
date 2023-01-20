def isprime(n):
    
    indicate = 0
    square = int(n**(1/2))

    if (n>1):
        for i in range(2,square+1):
            if (n % i == 0):
                indicate = 1
                break
        
        if (indicate == 0):
            return True
        else:
            return False
    
    else:
        return False
