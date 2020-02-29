from helper import d_Rsa,d_vigenere,text_to_int,int_to_text,e_Rsa,message,divide_blocks


f = open("cipher.txt","r")
contents = f.read()
cipher_message_list = contents.split(" ")
f.close()

f = open("cipher_key.txt","r")
contents = f.read()
cipher_key_list = contents.split(" ")
f.close()
print(cipher_key_list,cipher_message_list)

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

print(list_of_keys[2*usernum-1],list_of_keys[2*usernum-2])

print(private_key_recp,list_of_keys[2*rusernum-1])
# private_key_recp = "zioxkaez"
# privatenum = text_to_int("fjfseaieb")
# public_key_recp = "lh"
# sprivatekey = "hiesxkhk"
# spublic_key = "pi"
# snum =  text_to_int("txdmxakm")
orignal_message = "shivamjadhavgmailcom"

key = "kerboros"

y = []
for i in range(0,len(cipher_message_list)-1):
    l = divide_blocks(cipher_message_list[i],privatenum)
    for j in l:
        y.append(int_to_text(j))

z = []
for i in range(0,len(cipher_key_list)-1):
    l = divide_blocks(cipher_key_list[i],privatenum)
    for j in l:
        z.append(int_to_text(j))
print(y,z,"marker#1")
c_m = []
c_k = []
for i in range(0,len(y)):
    c_m.append(int_to_text(d_Rsa(y[i],private_key_recp,privatenum)))

for i in range(0,len(z)):
    c_k.append(int_to_text(d_Rsa(z[i],private_key_recp,privatenum)))


y1 = []
for i in range(0,len(y)):
    l = divide_blocks(c_m[i],snum)
    for j in l:
        y1.append(int_to_text(j))

z1 = []
for i in range(0,len(z)):
    l = divide_blocks(c_k[i],snum)
    for j in l:
        z1.append(int_to_text(j))
print(y1,z1)
pre_cm = []
pre_ck = []
final_cipher = ""
final_key = ""
for i in range(0,len(y1)):
    pre_cm.append(int_to_text(e_Rsa(y1[i],spublic_key,snum)))
    # print(i,pre_cm[i])
    final_cipher = final_cipher + pre_cm[i]
for i in range(0,len(z1)):
    pre_ck.append(int_to_text(e_Rsa(z1[i],spublic_key,snum)))
    # print(i,pre_ck[i])
    final_key = final_key + pre_ck[i]
print(final_key,final_cipher)

t = message(d_vigenere(final_cipher,final_key))
print(t)
if t == orignal_message:
    print(t)
else:
    print("REJECTED")
