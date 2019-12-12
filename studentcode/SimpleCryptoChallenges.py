'''
# Crypto Challenges

## Challenge 1 – the Caesar cipher
Your challenge is to decipher this string: MYXQBKDEVKDSYXC
'''
import base64
import binascii
import string

def caesar_decrypt(p_string):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # str_in = input('Enter message, Like Hello: ').upper()
    # shift = 0
    # while shift == 0:
    #     try:
    #         shift = int(input('Shift value, like 13: '))
    #     except ValueError as e:
    #         print(e)
    #         shift = 0

    all_shifts = {}

    for n in range(len(alpha)):
        all_shifts[n] = ''.join([alpha[(alpha.index(c) + n) %26] for c in p_string])

    for k, v in all_shifts.items():
        print(f'{k:3}: {v}')

    best = int(input('Please enter the most readable return: '))
    return all_shifts[best]

# 16: CONGRATULATIONS


'''
## Challenge 2 – base64

Decode this: VGhpcyBpcyB0b28gZWFzeQ==

b'This is too easy'

Decode this: VWtkc2EwbEliSFprVTBjeFl6lZaMWxUUW5OaU1qbDNVSGM5UFFvPQo=

Hint: several rounds of Base64 were used.
'''

def b64_cont_decode(p_string):
    # this function continuosly runs a base64 decode on the passed bytes encoded string (b'string') until the user stops it
    # sentinel value to control runs
    cont = True
    # pull in the string to a reassignable value (preserves input) *could convert str to byte encoded str here
    encode_str = p_string
    decodes = 0
    # while loop to continuously iterate decodes, print, and user input
    while cont:
        # decode the string using base64.b64decode()
        try:
            encode_str = base64.b64decode(encode_str)
            decodes += 1
        except binascii.Error:
            # add or remove padding to the string if an error occurs
            if encode_str[-2:] == b'==':
                encode_str = encode_str[:-2]
            else:
                encode_str += b'='
        print(f'{decodes} : {encode_str!s}')
        user_input = input('Run Again? y/n (default yes): ')
        # if user input is some version of no
        if user_input == 'n' or user_input == 'no' or user_input == 'N' or user_input == 'NO' or user_input == 'nO' or user_input == 'No':
            # set continue to False
            cont = False
    
    return encode_str


'''
## Challenge 3 – XOR

### The first challenge is here:

Decipher this: kquht}
Key is a single digit

# 8 : SIMPLE

###  Here's a longer example that is in a hexadecimal format:

Decipher this: 70155d5c45415d5011585446424c
Key is two digits of ASCII
'''

def my_xor(p_string, key_len):
    # xors a string with integers with a number of x digits
    keys = [str(k) for k in range(10**(key_len - 1), 10**key_len)]
    all_xors = {}

    # convert the string from hex if necessary
    if p_string[:2] == b'0x':
        p_string = str(binascii.unhexlify(p_string[2:]))

    # build a dictionary of xors with the key
    for key in keys:
        out_str = ''
        for i, c in enumerate(p_string):
            k = key[i % len(key)]
            x = ord(k) ^ ord(c)
            # print(c, k, x, chr(x))
            if chr(x) in string.printable:
                out_str += chr(x)
        all_xors[key] = out_str

    for k, v in all_xors.items():
        print(f'{k} : {v}')


if __name__ == "__main__":
    # caesar_decrypt('MYXQBKDEVKDSYXC')
    # b64_cont_decode(b'VGhpcyBpcyB0b28gZWFzeQ==')
    # b64_cont_decode(b'VWtkc2EwbEliSFprVTBjeFl6lZaMWxUUW5OaU1qbDNVSGM5UFFvPQo=')
    # b64_cont_decode(b'VWtkc2EwbEliSFprVTBJeFl6SlZaMWxUUW5OaU1qbDNVSGM5UFE9PQ==')
    # my_xor('kquht}', 1)
    my_xor(b'0x70155d5c45415d5011585446424c', 2)