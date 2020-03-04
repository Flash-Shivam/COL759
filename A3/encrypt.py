from helper import e_vigenere,int_to_text,text_to_int,e_Rsa,d_Rsa,message,divide_blocks

message1 = "shivamjadhavisahandsomeman"

key = "kerboros"

encrypted_message1 = message(e_vigenere(message1,key))

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

#print(list_of_keys[2*usernum-1],user_privatekey)
#print(rpublic_key,list_of_keys[2*rusername-1])
num = min(user_num,rnum)
cipher = []
key_cipher = []
encrypted_message_list = divide_blocks(encrypted_message1,num)
key_list = divide_blocks(key,num)
# print(encrypted_message_list,key_list)
# print(num,user_num-rnum,rnum)
for i in range(0,len(encrypted_message_list)):
    m = int_to_text(encrypted_message_list[i])
    cipher.append(int_to_text(d_Rsa(m,user_privatekey,user_num)))
    # print(m,int_to_text(e_Rsa(cipher[i],"rg",user_num)))

for i in range(0,len(key_list)):
    k = int_to_text(key_list[i])
    key_cipher.append(int_to_text(d_Rsa(k,user_privatekey,user_num)))
    # print(k,int_to_text(e_Rsa(key_cipher[i],"rg",user_num)))

m_prime = ""
for i in cipher:
    m_prime = m_prime + i
k_prime = ""
for i in key_cipher:
    k_prime = k_prime + i

cipher1 =  divide_blocks(m_prime,num)
key_cipher1 = divide_blocks(k_prime,num)
# print(cipher1)
# print(key_cipher1)

final_cipher = []
final_key_cipher = []
f = open("cipher.txt","w")
for i in range(0,len(cipher1)):
    m = int_to_text(cipher1[i])
    temp = int_to_text(e_Rsa(m,rpublic_key,rnum))
    final_cipher.append(temp)
    # print(m,int_to_text(d_Rsa(temp,"bzwlzn",rnum)))
    f.write(temp + " ")
f.close()


f = open("cipher_key.txt","w")
for i in range(0,len(key_cipher1)):
    k = int_to_text(key_cipher1[i])
    temp = int_to_text(e_Rsa(k,rpublic_key,rnum))
    # print(k,int_to_text(d_Rsa(temp,"bzwlzn",rnum)))
    final_key_cipher.append(temp)
    f.write(temp + " ")
f.close()

print(final_cipher,final_key_cipher)
