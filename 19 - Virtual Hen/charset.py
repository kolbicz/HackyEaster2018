import itertools
import string

charset=""

for x in string.printable:
    charset+= chr(ord(x) & 0xDF | 0x40)
print ''.join(sorted(set(charset), key=charset.index))