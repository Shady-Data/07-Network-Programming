# A-Z: 0-25
# a-z: 26-51
# 0-9: 52-61
# +/ : 62-63

# For python 3, import base64
from base64 import b64encode, b64decode

# encode/decode in the base64 module require bytes string (b'some string here')
c = b64encode(b'ABC')

print(c)

print(b64decode(c))