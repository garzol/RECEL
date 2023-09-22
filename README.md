# RECEL
binaries of the recel pinballs (internal ROM of A1761 and A1762)



2023-09-19 - phd@pps4.fr

Files recovered from original A1761-13 and A1762-13 RIOT spider chips
Chips lent: courtesy of Paulo Gordinho <gordon@outlook.pt>

Binary files were obtained by stripping header from serial log interface through my A17 reading material. 


To read bin files, use something like:
od -t x1 -A x BIN/A1761-13.bin

Each bin size is 2048 bytes even though the ROM size of an A176x is normally 1K. This is because size of pps4.com A17 clones is standard 2K. Thus, this explains why the second half of them is all 0s.

A1761-13 Config:
ROMSEL = 0
RAMSEL = 0
RAMAB8 = 0
IO ident is not yet determined (0x2 or 0x4)

A1762-13 Config:
ROMSEL = 1
RAMSEL = 0
RAMAB8 = 1
IO ident is not yet determined (0x4 or 0x2)


Recel.txt is a disassembly coming from an old disassembler
Recel2.txt is disassembled by a more recent app (available on https://rockwell.pps4.fr/dasm)

A1761-13 is also known as A2361
A1762-13 is also known as A2362
