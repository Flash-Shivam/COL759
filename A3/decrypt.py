from helper import d_Rsa,d_vigenere,text_to_int,int_to_text,e_Rsa,message,divide_blocks


f = open("cipher.txt","r")
contents = f.read()
cipher_message_list = contents.split(" ")
f.close()

f = open("cipher_key.txt","r")
contents = f.read()
cipher_key_list = contents.split(" ")
f.close()
# print(cipher_key_list,cipher_message_list)

usernum = 1
rusernum = 2
f = open("user_publickey.txt","r")
contents = f.read()
f.close()
list_of_keys = contents.split(" ")

privatenum = text_to_int(list_of_keys[2*rusernum-1])
name = "user"+str(rusernum)+ "priv"+".txt"
f = open(name,"r")
contents = f.read()
l = contents.split(" ")
f.close()
private_key_recp = l[0]
spublic_key = list_of_keys[2*usernum-2]
snum = text_to_int(list_of_keys[2*usernum-1])

# print(list_of_keys[2*usernum-1],list_of_keys[2*usernum-2])

# print(private_key_recp,list_of_keys[2*rusernum-1])
num = min(snum,privatenum)
# private_key_recp = "zioxkaez"
# privatenum = text_to_int("fjfseaieb")
# public_key_recp = "lh"
# sprivatekey = "hiesxkhk"
# spublic_key = "pi"
# snum =  text_to_int("txdmxakm")
orignal_message = "shivamjadhavisahandsomeman"
# print("--------")
key = "kerboros"
c_m = []
c_k = []
for i in range(0,len(cipher_message_list)-1):
    c_m.append(int_to_text(d_Rsa(cipher_message_list[i],private_key_recp,privatenum)))
    # print(cipher_message_list[i],int_to_text(e_Rsa(c_m[i],"fd",privatenum)))

for i in range(0,len(cipher_key_list)-1):
    c_k.append(int_to_text(d_Rsa(cipher_key_list[i],private_key_recp,privatenum)))
    # print(cipher_key_list[i],int_to_text(e_Rsa(c_k[i],"fd",privatenum)))

m_prime = ""
for i in c_m:
    m_prime = m_prime + i
k_prime = ""
for i in c_k:
    k_prime = k_prime + i
cipher1 =  divide_blocks(m_prime,num)
key_cipher1 = divide_blocks(k_prime,num)

pre_cm = []
pre_ck = []
final_cipher = ""
final_key = ""
for i in range(0,len(cipher1)):
    pre_cm.append(int_to_text(e_Rsa(int_to_text(cipher1[i]),spublic_key,snum)))
    # print(i,pre_cm[i])
    final_cipher = final_cipher + pre_cm[i]
    # print(int_to_text(cipher1[i]),int_to_text(d_Rsa(pre_cm[i],"xbrgadq",snum)))
for i in range(0,len(key_cipher1)):
    pre_ck.append(int_to_text(e_Rsa(int_to_text(key_cipher1[i]),spublic_key,snum)))
    # print(i,pre_ck[i])
    # print(int_to_text(key_cipher1[i]),int_to_text(d_Rsa(pre_ck[i],"xbrgadq",snum)))
    final_key = final_key + pre_ck[i]

# print(final_key)

t = message(d_vigenere(final_cipher,final_key))
# print(t)
if t == orignal_message:
    print(t)
else:
    print("REJECTED")
