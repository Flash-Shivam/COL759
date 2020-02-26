import sympy


def message(number_list):
    res = ""
    for i in number_list:
        res = res + chr(i+97)
    return res


def int_list(text):
    a = []
    for i in range(0,len(text)):
        a.append(ord(text[i])-97)
    return a


def E_vigenere(text,key):
    m = len(key)
    index = 0
    int_key = int_list(key)
    int_text = int_list(text)
    for i in range(0,len(int_text)):
        int_text[i] = (int_text[i] + int_key[index%m])%26
        index = index + 1
    return int_text


def D_vigenere(text,key):
    m = len(key)
    index = 0
    int_key = int_list(key)
    int_text = int_list(text)
    for i in range(0,len(int_text)):
        int_text[i] = (int_text[i] - int_key[index%m])%26
        if int_text[i] < 0:
            int_text[i] = int_text[i] + 26
        index = index + 1
    return int_text


def text_to_int(text):
    int_text = int_list(text)
    res = int_text[0]
    p = 1
    for i in range(1,len(int_text)):
        p = p * 26
        res = res + int_text[i]*p
    return res


def E_Rsa(text,public_key,n):
    m = text_to_int(text)
    e = text_to_int(public_key)
    return pow(m,e,n)


def D_Rsa(text,private_key,n):
    c = text_to_int(text)
    d = text_to_int(private_key)
    return pow(c,d,n)


def strong_prime(s,t):
    start = sympy.randprime(10,100)
    r = 2*start*t+1

    while not sympy.isprime(r):
        start = start + 1
        r = 2*start*t+1
        if sympy.isprime(r):
            x = ((2*pow(s,r-2,r))%r)*s-1
            if x%2 == 0:
                r = r + 1

    x = ((2*pow(s,r-2,r))%r)*s-1

    start = sympy.randprime(1,100)
    p = x + 2*r*s*start

    while not sympy.isprime(p):
        start = start + 1
        p = x + 2*r*s*start
    return p

a = sympy.nextprime(1030)

b = sympy.nextprime(a)
print(a,b)
print(strong_prime(a,b))
var = message(E_vigenere("cryptanalysis","code"))
print(var)
print(message(D_vigenere(var,"code")))
