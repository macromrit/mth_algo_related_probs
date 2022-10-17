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
