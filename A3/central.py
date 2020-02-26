import sympy
from helper import strong_prime, d_Rsa, text_to_int, int_to_text


# Generate Central Authority's Private Key
a = sympy.randprime(1,1000)
b = sympy.nextprime(a)

PrivateKeyCA  = (strong_prime(a,b))


n = strong_prime(b,a)

num = 2

sign_pk = []

for i in range(1,num+1):
    public_key = "User" + str(sympy.randprime(num,1000))
    sign_pk.append((int_to_text(d_Rsa(public_key,int_to_text(PrivateKeyCA),n)),public_key))

print(sign_pk)
