# to check whether a number n is a perfect power of a number x
n = int(input())
x = int(input())
print(round(n**(1/x))**x == n)
