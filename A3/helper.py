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


def e_vigenere(text,key):
    m = len(key)
    index = 0
    int_key = int_list(key)
    int_text = int_list(text)
    for i in range(0,len(int_text)):
        int_text[i] = (int_text[i] + int_key[index%m])%26
        index = index + 1
    return int_text


def d_vigenere(text,key):
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


def int_to_text(num):
    res = ""
    if num == 0:
        res = '0' + res
        return res
    while num > 0:
        res = res + chr(97+num%26)
        num = num / 26
    return res


def e_Rsa(text,public_key,n):
    m = text_to_int(text)
    e = text_to_int(public_key)
    return pow(m,e,n)


def d_Rsa(text,private_key,n):
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



def divide_blocks(text,num):
    int_list1 = int_list(text)
    r = []
    res = int_list1[0]
    p = 1
    for i in range(1,len(int_list1)):
        p = 26*p
        add = int_list1[i]*p
        if res + add > num:
            r.append(res)
            res = int_list1[i]
            p = 1
        else:
            res = res + add
    r.append(res)
    return r
