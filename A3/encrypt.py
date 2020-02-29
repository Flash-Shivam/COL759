from helper import e_vigenere,int_to_text,text_to_int,e_Rsa,d_Rsa,message,divide_blocks

message1 = "ilikeprogramming"

key = "cpp"

encrypted_message1 = message(e_vigenere(message1,key))
print("Encrypted Message - " + encrypted_message1)
# user_publickey = "pi"
usernum = 1
rusername = 2
f = open("user_publickey.txt","r")
contents = f.read()
f.close()
list_of_keys = contents.split(" ")

user_num = text_to_int(list_of_keys[2*usernum-1])
name = "user"+str(usernum)+ "priv"+".txt"
f = open(name,"r")
contents = f.read()
l = contents.split(" ")
f.close()
user_privatekey = l[0]
rpublic_key = list_of_keys[2*rusername-2]
rnum = text_to_int(list_of_keys[2*rusername-1])

print(user_privatekey,list_of_keys[2*usernum-1])
print(rpublic_key,list_of_keys[2*rusername-1])
num1 = min(rnum,user_num)

cipher = []
key_cipher = []
encrypted_message_list = divide_blocks(encrypted_message1,num1)
key_list = divide_blocks(key,num1)

print(encrypted_message_list,key_list)

var = "jo"

for i in range(0,len(encrypted_message_list)):
    m = int_to_text(encrypted_message_list[i])
    temp = int_to_text(d_Rsa(m,user_privatekey,user_num))
    cipher.append(temp)
    mtemp= int_to_text(e_Rsa(temp,var,user_num))
    print(m,mtemp)
print("----------")
for i in range(0,len(key_list)):
    k = int_to_text(key_list[i])
    temp = int_to_text(d_Rsa(k,user_privatekey,user_num))
    key_cipher.append(temp)
    temp1 = int_to_text(e_Rsa(temp,var,user_num))
    print(k,temp1)
print("----------")
final_cipher = []
final_key_cipher = []
f = open("cipher.txt","w")


y = []
for i in range(0,len(encrypted_message_list)):
    l = divide_blocks(cipher[i],num1)
    for j in l:
        y.append(int_to_text(j))
z = []
for i in range(0,len(key_list)):
    l = divide_blocks(key_cipher[i],num1)
    for j in l:
        z.append(int_to_text(j))



for i in range(0,len(y)):
    m = (y[i])
    temp = int_to_text(e_Rsa(m,rpublic_key,rnum))
    temp1 = int_to_text(d_Rsa(temp,"rdcajlzu",rnum))
    print(m,temp1,text_to_int(temp1),text_to_int(m))
    # print(temp)
    final_cipher.append(temp)
    f.write(temp + " ")
f.close()
print("----------")
f = open("cipher_key.txt","w")
for i in range(0,len(z)):
    k = (z[i])
    temp = int_to_text(e_Rsa(k,rpublic_key,rnum))
    temp1 = int_to_text(d_Rsa(temp,"rdcajlzu",rnum))
    print(k,temp1)
    final_key_cipher.append(temp)
    f.write(temp + " ")
f.close()
print("----------")
print(final_cipher,final_key_cipher)
