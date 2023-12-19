# RECEL Binaries
binaries of the recel pinballs (internal ROM of A1761 and A1762)  
+  
binary from the eprom of the screech (magia) game variant  




2023-09-19 - phd@pps4.fr

## Generalities  
Files recovered from original A1761-13 and A1762-13 RIOT spider chips and from eprom (256Bytes)  
Chips lent: courtesy of Paulo Gordinho <gordon@outlook.pt>  
Binary files were obtained from my A17 reading material. 

To read bin files, use something like:  
`od -t x1 -A x BIN/A1761-13.bin`

The size of an A17xx ROM is 2KB (A1..A11 + RRSEL). Hence, Each bin size is 2048 bytes even though the ROM size of an A176x is normally 1K. Reading an A176x chip shows that the second half of its ROM is all 0 (not programmed). 0 in PPS-4 logic means VSS, or +5V. 

| :exclamation:  A176x ROM has a size of 2KB, but  the second half is all 0 (not programmed) | 
|-----------------------------------------|  
  


| :zap:    RECEL Hardware does not use A11, which is directly connected to VSS                  |
|-----------------------------------------|  





## Config of A17 chips  
- A1761-13 internal Config:  
  - ROM access:  
    - ROMSEL = 0  
  - RAM access:       
    - RAMSEL = 0  
    - RAMAB8 = 0      
  - IO chip Id:   
    - 0x4  
- A1762-13 Config:  
  - ROM access:  
    - ROMSEL = 1  
  - RAM access:    
    - RAMSEL = 0  
    - RAMAB8 = 1  
  - IO chip Id:  
    - 0x2

## ROM mapping  
The analysis of the recel master board schematic shows that the rom mapping is as follows:   
`0x000..0x3FF : A1761-13`   
`0x400..0x7FF : A1762-13`   
`0x800..0x8FF : game eprom 1702`   

## Considerations about signal polarity.
Note that the logic in PPS4 is inverted, thus: 1=-12V, 0=+5V.
BICs don't invert the D and Addr signals, which means that +5V stays +5V and -12V becomes 0V on the eprom ttl side.

Since the Ttl side is positive logic, there is an implicit inversion of logic between data, both on address and data bus.

This is why we need to invert everything from the initial binary to retrieve the code of the eprom.
you can use pdtac.py for this purpose.
1702_screech_invA_invD.bin is the exact inversion both on data and addresses of 1702.bin.  
1702_screech_invA_invD shall be used for disassembly (start address 0x800)

## Disassembly  
Recel_screech.txt is a disassembly coming from an old disassembler
To be up to date use the most recent app (available on line on https://rockwell.pps4.fr/dasm) or on github if you want to be offline:
https://github.com/garzol/pps4Emul.git   

commented disassembly here:   
https://spider.pps4.fr/static/coegen/recel_screech.txt  
(regular updates, as I make progress in this decompilation)  


A1761-13 is also known as A2361  
A1762-13 is also known as A2362
