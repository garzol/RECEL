2024-08-01

from fa.c5 (from internet) is derived by double inversion (data+addresses) fa.bin
command for double inversion is something like:
python3 ../pdtac.py sc.c5  > sc4.bin



fa.bin is pps4 instruction code.
 
fa.bin is fair fight game prom 256 bytes to be mapped at 800..8FF

cr.bin is 2KB 4x256b being game prom at 800 + 2KB of slightly modified A1762 (located at 0x400..0x7FF)

from cr.bin are derived:
crgame.bin is crazy race game prom 256 bytes to be mapped  at 800..8FF
crA1762.bin is crazy race A1762 1KB to be mapped at 0x400..0x7FF

differnces between original A1762 bin and crA1762...
cmp -x  crA1762.bin A1762-13_1K.bin
0000004e 59 50
0000004f 80 0b 
000002fe 34 00

44E	50	0B	TL	00B				; Transfer Long
in the cr version its a TL 980


6FD	57	00	TL	700				; Transfer Long

in the cr version its a TL 734 => don't execute pio selftest (?)


===
screech:
There are 2 versions:
sc_1_1702.bin (obtained from r_screech1.zip, and after inversion) is a 256b standard game prom

sc4_256.bin is built from r_screech4.zip. After inversion one can see that this file is 8 times a standard 256 bytes game prom. For now, we assume it is a standard game prom, so we created only a 256 bytes prom insttead of the original 8x version.

r_screech4.zip gives sc.c5 which gives sc4.bin which gives sc4_256.bin through something like:
head -c 256 sc4.bin > sc4_256.bin

 
b4 is like fl : 1K game + 1K A1762 rom mod 
N.B. an interesting way to compare bin files:
xxd -c 1 A1762-13_1K.bin|cut -d ' ' -f 2 >A1762-13_1K.hex
xxd -c 1 flA1762.bin|cut -d ' ' -f 2 >flA1762.hex        
Then
diff flA1762.hex A1762-13_1K.hex                         



===
pokerplus
The version cointained in the original recel_games.zip is wrong, for some reasons we are not aware of
The good one was given by EdC later at our demand. It is pokerplus_BA65_EdC.BIN (before double inversion)
Then the good binary file is pokerplus_BA65.BIN (double inversion of pokerplus_BA65_EdC.BIN)
can also be found on ralf site:
https://lisy.dev/swrep/RecelFA/game_roms/



