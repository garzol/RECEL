# RECEL Binaries
binaries of the recel pinballs (internal ROM of A1761 and A1762)  
+  
binary from the eprom of the screech (magia) game variant  


## Origin of the chips
### "13" variants
Files recovered from original A1761-13 and A1762-13 RIOT spider chips and from eprom (256Bytes)  
Chips lent: courtesy of Paulo Gordinho <gordon@outlook.pt>  
Binary files were obtained from my A17 reading material. 

2023-09-19 - phd@pps4.fr

### "14" variants
Files recovered from original A1761-14 and A1762-14 RIOT spider chips  
Chips lent: [Recreativas.org](https://www.recreativas.org)  
Binary files were obtained from my A17 reading material.   
There was no creation of bin files for -14 chips because they appear to be exactly identical to their -13 counterparts. 

Therefore, while we did not test it actually, mixing a -13 with a -14 fitted on the same board should be working.  

2023-12-19 - phd@pps4.fr

| :zap:    A176x-13 and A176x-14 are strictly identical                  |
|-----------------------------------------|  


## Generalities  
To read bin files, use something like:  
`od -t x1 -A x BIN/A1761-13.bin`

The size of an A17xx ROM is 2KB (A1..A11=>2KB + RRSEL as a chip select). Hence, Each bin size is 2048 bytes even though the actual significant ROM size of an A176x is only 1K. If you look at the System 3 schematic, you will see that A11 is tied to "ground" permanently. Then, accessing the second half of the ROM is not possible on the CPU board.  However, with our specific A17 reader, this is not the case. All addresses in the range (A1..A11 + RRSEL) are scrutinized. Reading an A176x chip shows that the second half of its ROM is all 0 (not programmed). 0 in PPS-4 logic means VSS, or +5V. 

| :exclamation:  A176x ROM has a size of 2KB, but the second half of it is all 0 (not programmed) | 
|-----------------------------------------|  
  


| :zap:    RECEL Hardware does not make use of A11, which is tied to VSS                  |
|-----------------------------------------|  



| :zap:    The ROM mapping of the board just lets appear ranges of 1KB for each RRIOT                  |
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

This is why we need to invert everything from the initial binary to retrieve the code of the game prom.
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


A1761-13 or A1761-14 are also known as A2361  
A1762-13 or A1762-14 are also known as A2362

## PIO 11696 commands
`IOL	XY`  
`X is the device ID, OxD on the sys3`  
`Y is the command` 

### Command codes
#### Read/Write IO  

| Group#        |  Read=>(A)    | Write<=(A) |
| ------------- | ------------- | ---------- |
|            A  | 0             | 8          | 
|            B  | 1             | 9          | 
|            C  | 2             | A          | 
|            D  | 3             | F          | 
|            E  | 4             | C          | 
|            F  | 5             | D          |

#### Set/Reset specific bit
SET: Command is `IOL X6 with Acc as in the table below`   
RESET: Command is `IOL XB with Acc as in the table below` 


| Group#-bit#   | (A) [6=set B=reset] |
| ------------- | ------------------- | 
|       A-1     | F                   | 
|       A-2     | E                   | 
|       A-4     | D                   | 
|       A-8     | C                   | 
|       B-1     | B                   | 
|       B-2     | A                   | 
|       B-4     | 9                   | 
|       B-8     | 8                   | 
|       C-1     | 7                   | 
|       C-2     | 6                   | 
|       C-4     | 5                   | 
|       C-8     | 4                   | 
|       D-1     | 3                   | 
|       D-2     | 2                   | 
|       D-4     | 1                   | 
|       D-8     | 0                   | 
|
