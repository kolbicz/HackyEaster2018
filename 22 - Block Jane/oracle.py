from pwn import *  # NOQA
import socket
from Crypto.Cipher import AES

from paddingoracle import BadPaddingException, PaddingOracle

HOST = "whale.hacking-lab.com"
PORT = 5555

encdata = [0xe3, 0x43, 0xf4, 0x26, 0x04, 0xca, 0x58, 0xa7, 0x31, 0xad, 0xbf, 0x10, 0xb3, 0x76, 0xee, 0x33, 
  	   0xaa, 0x94, 0x49, 0x26, 0xcd, 0xf9, 0x54, 0x40, 0x0d, 0x86, 0xee, 0x4f, 0x6e, 0x35, 0x77, 0x4e, 
  	   0xc5, 0x10, 0xfe, 0x57, 0x67, 0xba, 0xba, 0x99, 0xa3, 0xed, 0x28, 0xfa, 0x26, 0xdc, 0x99, 0xb6,
  	   0xc1, 0xda, 0xdd, 0x08, 0x7e, 0x4c, 0xee, 0x27, 0xe4, 0x55, 0x07, 0x00, 0x52, 0x76, 0xc1, 0x0f, 
  	   0xd9, 0xc1, 0x5f, 0x27, 0xd3, 0x48, 0x1a, 0x92, 0xf3, 0x4d, 0xd4, 0x64, 0x77, 0xf7, 0xbe, 0x3c]

log.info("%d blocks of AES", len(encdata) // AES.block_size)
# split the blocks
bs = AES.block_size
iv = encdata[:bs]
blocks = [encdata[bs:2 * bs],
          encdata[2 * bs:3 * bs],
          encdata[3 * bs:]]

encdata_s = ""
for b in blocks:
    for c in b:
        encdata_s += chr(c)

class PadBuster(PaddingOracle):
    def __init__(self, **kwargs):
        super(PadBuster, self).__init__(**kwargs)

    def oracle(self, data, **kwargs):
        log.info(hexdump(data))
        #rem = remote(HOST, PORT)
        rem = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        rem.connect((HOST, PORT))
        rem.sendall("".join(chr(x) for x in data))
        line = rem.recv(5)
        #self.history.append(line)
        log.debug(line)
        if "error" in line:
            raise BadPaddingException()
        rem.close()
        del rem

padbuster = PadBuster()
data = padbuster.decrypt(encdata_s, block_size=AES.block_size, iv=iv)
log.info(data)
