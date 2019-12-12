text = input('Enter text: ')
key = input('Enter key: ')
# n = len(text)

# for i in range(n):
#     t = text[i]
#     k = key[i%len(key)]
#     x = ord(k) ^ ord(t)
#     print(t, k, x, chr(x))

out_str = ''

for i, c in enumerate(text):
    k = key[i % len(key)]
    x = ord(k) ^ ord(c)
    print(c, k, x, chr(x))
    out_str += chr(x)

print(out_str)


