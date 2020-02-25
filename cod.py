import binascii

# generate a binary message 'm'

message = "Hello World!"
m1 = ' '.join(format(ord(x), 'b') for x in message)

# convert to decimal
if len(m1) %2 == 1:
    m1 = '0' + m1
print(m1)
print(str(m1).replace(" ", ""))
m = int(str(m1).replace(" ", ""), 2)

print(m)

n = 642401
p = 569
q = 1129
# n = p*q , phi = (p-1)*(q-1)
phi = 640704
# Public Key = (e,n)
e = 887
# Private Key = (d,n)
d = 603143


# pre-compute signature of bank on m

signature1 = pow(m,d,n)

print(bin(signature1).replace("0b",""))

# blind with a blinding factor 'k'
k = 883

m_blind = ( m * pow(k,e,n) ) % n

print(bin(m_blind).replace("0b",""))


# sign with private key d of bank

sig_m_blind = pow(m_blind,d,n)
print(bin(sig_m_blind).replace("0b",""))

# un-blind by dividing by k mod n
for i in range(1,n):
    p = i*k
    if p % n == 1:
        k = i
        break
signature2 = (sig_m_blind*k) % n
print(bin(signature2).replace("0b",""))
# verify if both values are same or not
if signature1 == signature2:
    print("Blind Signature Through RSA")
