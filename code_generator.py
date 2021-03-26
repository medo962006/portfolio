import string
from random import choice
import sys
from pyperclip import copy
try:
    strength = int(input('how strong do you want your encrypted code(enter an integer)?\n:'))
except:
    print('wrong Input, closing program...')
    sys.exit(-1)
all_char ='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-./:;?@[]^_`{|}~'
all_char_list = [_ for _ in all_char]
code = {}
for x in string.ascii_letters:
    codee = ''
    for i in range(strength):
        codee += choice(all_char_list)
    code[x] = codee
print(code)
copy(str(code))
print('encrypted code copied to clipboard')
