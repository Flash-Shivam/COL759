from helper import e_vigenere,int_to_text,text_to_int,e_Rsa,d_Rsa,message,divide_blocks

message1 = "shivamjadhavgmailcom"

key = "kerboros"

encrypted_message1 = message(e_vigenere(message1,key))

user_publickey = "pi"
user_num = text_to_int("txdmxakm")
user_privatekey = "hiesxkhk"
rpublic_key = "lh"
rnum = text_to_int("fjfseaieb")


num = min(user_num,rnum)
cipher = []
key_cipher = []
encrypted_message_list = divide_blocks(encrypted_message1,num)
key_list = divide_blocks(key,num)
for i in range(0,len(encrypted_message_list)):
    m = int_to_text(encrypted_message_list[i])
    cipher.append(int_to_text(d_Rsa(m,user_privatekey,user_num)))

for i in range(0,len(key_list)):
    k = int_to_text(key_list[i])
    key_cipher.append(int_to_text(d_Rsa(k,user_privatekey,user_num)))

final_cipher = []
final_key_cipher = []

for i in range(0,len(encrypted_message_list)):
    m = (cipher[i])
    final_cipher.append(int_to_text(e_Rsa(m,rpublic_key,rnum)))

for i in range(0,len(key_list)):
    k = (key_cipher[i])
    final_key_cipher.append(int_to_text(e_Rsa(k,rpublic_key,rnum)))


print(final_cipher,final_key_cipher)
