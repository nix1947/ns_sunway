from string import printable as letters



def encrypt(message, key):
    cipher = [] # List equivelent to array
    for c in message:
        position = letters.find(c)
        new_position = position + key % len(letters) 
        encrypted_char = letters[new_position]
        cipher.append(encrypted_char)

    return ''.join(cipher)


def decrypt(cipher, key):
    plain_text = []
    for c in cipher:
        position = letters.find(c)
        position = (position - key) % len(letters)
        plain_text.append(letters[position])
    return ''.join(plain_text)


message = 'hello'
# Call the encrypt function

cipher = encrypt(message, 3) # 3 is the key, each letter shifted by 3 postion.
print(cipher) # This is the encrypted message. 

# Decryption
# Call decrypt function
plain_message =  decrypt(cipher, 3) # This print the original messaage. 


