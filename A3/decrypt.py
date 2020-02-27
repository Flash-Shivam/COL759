from helper import d_Rsa,d_vigenere,text_to_int,int_to_text,e_Rsa,message

cipher_message_list = ["bvjerobb", "fzipftyv", "vruunohs"]

cipher_key_list = ["tojzqujr", "wogaxsqb"]

private_key_recp = "zioxkaez"
privatenum = text_to_int("fjfseaieb")
public_key_recp = "lh"
sprivatekey = "hiesxkhk"
spublic_key = "pi"
snum =  text_to_int("txdmxakm")
orignal_message = "shivamjadhavgmailcom"

key = "kerboros"
c_m = []
c_k = []
for i in range(0,len(cipher_message_list)):
    c_m.append(int_to_text(d_Rsa(cipher_message_list[i],private_key_recp,privatenum)))

for i in range(0,len(cipher_key_list)):
    c_k.append(int_to_text(d_Rsa(cipher_key_list[i],private_key_recp,privatenum)))

pre_cm = []
pre_ck = []
final_cipher = ""
final_key = ""
for i in range(0,len(cipher_message_list)):
    pre_cm.append(int_to_text(e_Rsa(c_m[i],spublic_key,snum)))
    final_cipher = final_cipher + pre_cm[i]
for i in range(0,len(cipher_key_list)):
    pre_ck.append(int_to_text(e_Rsa(c_k[i],spublic_key,snum)))
    final_key = final_key + pre_ck[i]


t = message(d_vigenere(final_cipher,final_key))
if t == orignal_message:
    print(t)
else:
    print("REJECTED")
