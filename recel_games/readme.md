2024-08-01

## Origin of this zip file  
In the following, what we call *this file* is recel_games.zip that we have decompressed to build the present directory.  

This file contains all games of the recel system 3 series.  

This file comes from recreativas.org, and was likely originally made by or for Mame project.  

Apart from the comments below, all these binaries are validated and can be considered good  


## Purpose of such files.  
This binary files (extension .c5) are destinated to make eproms (mainly 2716) for recel sys3 MPUs.
There are 2 HW versions of such MPU:  
1. Original version : There is a game prom (either a 1702A or 2716, or even whatever...) which contains specific game variant for a given game (15 different games exist). This game prom contains short subroutines that are called by the main program, which is common to all games, and resides in the ROM sections of B1 and B2. (2KB of code). B1 (A1761) from 0x000..0x3FF contains the startup boot address (at 0x000). B2 (A1762), prolonges the code from 0x400..0x7FF. Speifics for a particular game for example is how much points for hitting which target, this sort of things...  

2. Version 2 : In this version, B1 is still used just the same way as in V1. But B2 is disabled (ROM subsection only) and its equivalent 0x400..0x7FF is remapped in the game prom (locally from 0x400..0x7FF, in the eprom, this time), while the game variant is located in 0x000..0x3FF of the eprom, which is seen as from 0x800 from the cpu point of view.). Instead of 256B available as in V1, there are now 1KB available of game variant in V2.  

All this binary data (In B1, B2, or eprom) are PPS4 assembly code.  
Since, the eprom is accessed through BIC interface, and also because PPS4 logic is **negative**, you won't read pps4 assembly code directly from a .c5 file. If you want to disassemble this binary you need to invert both addresses and data first. Then you'll get PPS4  mnemonics.  

Since game proms are read by the MPU through PPS4 BIC chips, that use negative logic, you have to invert both addresses and data to make a bin image from a '.c5' file. 

> [!IMPORTANT]  
> In summary, to make game prom, use .c5 files. To disassemble or use directly the code with, for example, an emulator, you'll have to make the double 


### Example
from fa.c5 (from internet) is derived by double inversion (data+addresses) fa.bin.  
command for double inversion is something like:  

```
python3 ../pdtac.py sc.c5  > sc4.bin
```



fa.bin is pps4 instruction code.
 
fa.bin is fair fight game prom 256 bytes to be mapped at 800..8FF

cr.bin is 2KB 4x256b being game prom at 800 + 2KB of slightly modified A1762 (located at 0x400..0x7FF)

from cr.bin are derived:
crgame.bin is crazy race game prom 256 bytes to be mapped  at 800..8FF
crA1762.bin is crazy race A1762 1KB to be mapped at 0x400..0x7FF

diferences between original A1762 bin and crA1762...  

```
cmp -x  crA1762.bin A1762-13_1K.bin
```

> 0000004e 59 50  
> 0000004f 80 0b    
> 000002fe 34 00  

44E	50	0B	TL	00B				; Transfer Long
in the cr version its a TL 980


6FD	57	00	TL	700				; Transfer Long

in the cr version its a TL 734 => don't execute pio selftest (?)


## Specificities  
### screech:  
There are 2 versions:
sc_1_1702.bin (obtained from r_screech1.zip, and after inversion) is a 256b standard game prom

sc4_256.bin is built from r_screech4.zip. After inversion one can see that this file is 8 times a standard 256 bytes game prom. For now, we assume it is a standard game prom, so we created only a 256 bytes prom insttead of the original 8x version.

r_screech4.zip gives sc.c5 which gives sc4.bin which gives sc4_256.bin through something like:
head -c 256 sc4.bin > sc4_256.bin  

In the original delivery it was assumed that one file was for screech 1Player and the other for screech 4Player. But screech 1P never existed, then...  

### black magic
b4 is like fl : 1K game + 1K A1762 rom mod 
N.B. an interesting way to compare bin files:
xxd -c 1 A1762-13_1K.bin|cut -d ' ' -f 2 >A1762-13_1K.hex
xxd -c 1 flA1762.bin|cut -d ' ' -f 2 >flA1762.hex        
Then
diff flA1762.hex A1762-13_1K.hex                         



### pokerplus  
The version cointained in the original recel_games.zip is wrong, for some reasons we are not aware of.  

The good one was given by EdC later at our demand. It is pokerplus_BA65_EdC.BIN (before double inversion)
Then the good binary file is pokerplus_BA65.BIN (double inversion of pokerplus_BA65_EdC.BIN)
can also be found on [Ralf' site](https://lisy.dev/swrep/RecelFA/game_roms/).



