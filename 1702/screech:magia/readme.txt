2024-11_18

I compared the obtained 1702 binary and sc4.bin from recel_games.zip
==>They are identical.




2023-09-22

I got 3 eproms from Paulo Gordinho.

The 3 were dedicated to screech/magia variant.

Paulo identified its eproms with colour post-its (red, violet, yellow)

I built a home made 1702 reader and tried each eprom twice. Hence 6 files (2 per colour)

The 6 files are identical, proving that we successfully read the eprom.

I left all of them here for describing the methodology used. Since they are all identical, you can pick whichever you want, it does not matter.


Infos: I did my best to fetch data in right address order (from 0 to 255, 0 being 0V, 1 being 5V)
and in correct logic for data (0 being 0V, 1 being 5V)

Nevertheless, it is quite a pain in the back to ensure a correct polarity all across the acquisition chain...

Moreover, there was no means to verify against a reference, since there was no reference available.

So, I was unsure. To add up in the potential mess, I thought that the 256 bits of the 1702 were pure configuration, making it impossible to check the contents since its could be anything.

But... looking at the schematic, it appears that the 1702 is actually PPS4 code in the rom space between 0x800 and 0x8FF. It also appears that the 1702 is accessed through 2 BICs for which data and addresses are not inverted during the operation. But, since PPS4 work on a negative logic, there is actually an inversion.

Therefore, by inverting both addresses and data values, we normally should see meaningful code, and this is the case. We are sure of that, because, for example, every 1C code in the eprom (IOL) is effectively followed by one of the possible 2nd parameter (2, 4, D, F).


phd@pps4.fr
https://rockwell.pps4.fr/recelsys3/
https://rockwell.pps4.fr
