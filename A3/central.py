import sympy
from helper import strong_prime,D_Rsa


# Generate Central Authority's Private Key
a = sympy.randprime(1,1000)
b = sympy.nextprime(a)

PrivateKeyCA  = (strong_prime(a,b))


n = strong_prime(b,a)

num = 2

for i in range(1,num+1):
    
