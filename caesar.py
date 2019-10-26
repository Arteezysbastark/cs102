def encrypt_caesar(plaintext: str, number: int) -> str:
    b = int
    c = ("")
    i = int
    i = 0
    while i < len(plaintext):
        b = ord(plaintext[i])
        if((b+number > 65 and b+number < 90) or (b+number > 97 and b+number < 122)):
            b = b+number
        elif (b+number > 90 and b+number < 97):
            b = b + number + 6
        elif (b+number > 122):
            b = b + number - 57
        c = c+(chr(b))
        i = i+1
    return c


def decrypt_caesar(plaintext: str, number: int) -> str:
    b = int
    c = ("")
    i = int
    i = 0
    while i < len(plaintext):
        b = ord(plaintext[i])
        if((b-number > 64 and b-number < 91) or (b-number > 96 and b-number < 123)):
            b = b-number
        elif(b > 96 and b - number < 97):
            b = b - number - 6
        elif(b > 64 and b-number < 65):
            b = b - number + 58
        c = c+(chr(b))
        i = i+1
    return c

