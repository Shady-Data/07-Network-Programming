# plain text  ABCDEFGHIJKLMNOPQRSTUVWXYZ
# cipher text DEFGHIJKLMNOPQRSTUVWXYZABC

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

str_in = input('Enter message, Like Hello: ').upper()
shift = 0
while shift == 0:
    try:
        shift = int(input('Shift value, like 13: '))
    except ValueError as e:
        print(e)
        shift = 0

str_out = ''.join([alpha[(alpha.index(c) + shift) %26] for c in str_in])

print('Obfuscated version:', str_out)