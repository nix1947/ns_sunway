from string import ascii_uppercase


keyword = 'RANDOMKEYWORD'

def encrypt(message):
    """Return xor of plain and message""" 
    return ''.join([chr(ord(plain) ^ ord(key)) for plain,key in zip(message, keyword[:len(message)])])
    

def decrypt(cipher):
    return encrypt(cipher)

