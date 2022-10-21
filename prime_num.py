from math import sqrt

#here's how the prob works
#first we have to figure out the given num's sqrt... then have to floor it
#after doin those stuff... have to get on a condition whether ints from the range 2 to the given particular  
#sqrt(inclusive) can be used to divide the given num without any residual reminder then that num's a composite one

def find_prime(num: int)->bool:
    if num>1:
        for i in range(2, int(sqrt(num))+1):
            if num%i==0:
                return False
            else:
                return True
    else:
        return False

    '''
    #figuring out a list of prime numbe to a give range from 2
    from math import sqrt

def prime(x: int) -> list:
    if x==1:
        return -1
    elif x>1:
        def prime_nums(n: int)->list:
            for i in range(2, int(sqrt(n)+1)):
                if n%i==0:
                    return False
                else:
                    pass
                
            return True
        
        return list(filter(prime_nums, range(2, x+1)))
    else: return 

    '''
