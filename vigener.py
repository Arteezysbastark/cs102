def encrypt_vigenere(plaintext: str, keyword: str) -> str:
 b=int
 c=("")
 i = int
 i=0
 base_keyword = keyword
 while(len(keyword) <  len(plaintext)):
    keyword = keyword + base_keyword
 while i < len(plaintext):
    b = ord(plaintext[i])
    k = keyword[i]
    if(ord(keyword[i]) > 96):
     number = ord(keyword[i]) - 97
    else:
     number = ord(keyword[i]) - 65
    if((b+number > 65 and b+number < 90) or (b+number>97 and b+number < 122)) :
     b=b+number
    elif (b+number>90 and b+number < 97) :
     b = b + number + 6
    elif (b+number > 122) :
     b = b + number - 57
    c=c+(chr(b))
    i=i+1
 print (c)      
 return c
def decrypt_vigenere(plaintext: str, keyword: str) -> str:
 b=int
 c=("")
 i=int
 i=0
 base_keyword = keyword
 while(len(keyword) <  len(plaintext)):
    keyword = keyword + base_keyword
 while i < len(plaintext):
    b = ord(plaintext[i])
    k = keyword[i]
    if(ord(keyword[i]) > 96):
     number = ord(keyword[i]) - 97
    else:
     number = ord(keyword[i]) - 65
    if((b-number > 64 and b-number < 91) or (b-number>96 and b-number < 123)) :
     b=b-number
    elif(b > 96 and b - number < 97):
     b = b - number - 6
    elif(b > 64 and b-number < 65): 
     b = b - number + 58
    c=c+(chr(b))
    i=i+1 
 print (c)
 return c
l=input("Введите строку")
s=(input("Введите шифр"))
ciphertext= encrypt_vigenere (l,s)
plaintext=decrypt_vigenere(l,s)