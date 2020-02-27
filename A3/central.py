import sympy
from helper import strong_prime, d_Rsa, text_to_int, int_to_text

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    return x%m
# Generate Central Authority's Private Key

a = sympy.randprime(1,1000)
b = sympy.nextprime(a)

PrivateKeyCA  = (strong_prime(a,b))


n = strong_prime(b,a)

num = 2

publickeys = []
privatekeys = []
sign_pk = []

for i in range(1,num+1):
    public_key = sympy.randprime(sympy.randprime(1,num+100),sympy.randprime(num+101,1000))
    n3 = sympy.nextprime(public_key)
    n2 = strong_prime(public_key,n3)
    n1 = n2*n3
    phi = (n2-1)*(n3-1)
    private_key = modinv(public_key,phi)
    temp = private_key
    private_key = public_key
    public_key = temp
    publickeys.append((int_to_text(public_key),int_to_text(n1)))
    privatekeys.append(int_to_text(private_key))
    sign_pk.append((int_to_text(d_Rsa(int_to_text(public_key),int_to_text(PrivateKeyCA),n)),(int_to_text(d_Rsa(int_to_text(n1),int_to_text(PrivateKeyCA),n)))))

print(sign_pk)
print(publickeys)
print(privatekeys)
