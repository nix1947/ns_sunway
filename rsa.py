#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Implement a RSA algorithm to encrypt and decrypt
message

choose two prime number 


p = 7 
q = 13 

n = p * q = 91

m = (p - 1 ) * (q - 1) 
    (7 - 1 ) * (13 - 1) = 72


Now it's time to find public key

public key = (e, n) 

To find public key we have an equation 

GCD(e, m) = 1 : 1 < e < m 

GCD(e, 72) = 1

lets choose e = 4
factors of 4
4 = 2 * 2 * 1

m = 72
factors of m 
2 * 3 * 2 * 3 *2 * 1

we cannot choose e as 4 because the 
GCD(greatest common divider) of 
4 and 72 is 2 not 1

let's choose e = 5

Factor of e = 5
5 = 5 * 1

factor of m = 7 2

2 * 3 * 2 * 3 *2 * 1

The greatest divisor factor of e=5 and
m=72 here is 1 
so we can  choose e as 5 

so public key (e, n) = (5, 91)

"""

from math import gcd 

def gen_random_prime_number():
    return 7, 19

p, q = gen_random_prime_number() 


def gen_n():
    return  p * q 

n = gen_n() 

def get_m():
    return  (p-1) * (q-1)

m = get_m() 

def gen_public_key():
    """
        Algorithm to generate public key is 
        GCD(e, m) = 1 :  1 < e < m
    """
    # Let's find e below 1000

    for e in range(2, 1000):
       check = gcd(e, m) 
       if check == 1: 
           return e 

e = gen_public_key() 

def gen_private_key():
    """
        Generate private key d 
        d = (1 + m * i) / e
        The value of d must be in whole number. 
    """

    m = get_m()
    e = gen_public_key()

    for i in range(2, 1000):
        d = (1 + m * i ) / 5
        if int(d) == d: 
            return int(d) 

d = gen_private_key() 

def encode(message=None):
    """
        Retun the ascii string of given string.
    """
    return ord(message) 

def decode(char=None):
    """
        Return the plain text from given ascii string.
    """
    return chr(char)


def encrypt(message=None):
    if message is None: 
        raise ValueError("Message shouldn't be None")

    cipher_char = []  
    for char in message:
        encoded_char = encode(char)
        cipher = encoded_char ** gen_public_key() % gen_n() 
        cipher_char.append(cipher) 

    return ','.join(list(map(lambda char: str(char), cipher_char)))




def decrypt(cipher=None):
    if cipher is None:
        raise ValueError("Cipher shouldn't be None")

    plain_char = []
    cipher_list = cipher.split(',')

    for cipher_char in cipher_list: 
        plain = decode(int(cipher_char) ** gen_private_key() % gen_n())
        plain_char.append(plain)
    return ''.join(plain_char)










