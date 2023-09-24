'''
Created on 23 sept. 2023

@author: a030466

This utility for reversing a binary file and inverting every byte

This is because eprom in RECEL pinballs is read through BIC interface and schematic of the master board shows that BICs are selected when A12 is 1. 
Then, we can say that the eprom addresses are in 0x800..0x8FF (just above the ROM space (0..7FF)

Note that the logic in PPS4 is inverted, thus: 1=-12V, 0=+5V.
BICs don't invert the D and A signals, which means that +5V stays +5V and -12V becomes 0V on the eprom tel side.

Since the Ttl side is positive logic, there is an implicit inversion of logic between data, both on address and data bus.

This is why we need to invert everything to retrieve the code of the eprom.

We are confident that our analysis is correct because for example 1C is always followed by a relevant byte in the file. 1C is IOL and must be followed by the identifier of a PPS4 device, which on recel can be 2, 4, D or F. Cqfd
'''

import sys
import os.path as path

def usage(progname):
    progshort = path.basename(progname)
    #print(f"usage : python {progshort} input_bin_file start_addr offset_addr")
    print(f"usage : {progshort} input_bin_file ")


    
if __name__ == '__main__':   
    #print ("Start...")
    try:
        inputfilename=sys.argv[1]
    except:
        usage(sys.argv[0])
        print("...Abort")
        sys.exit()
    
    if not path.isfile(inputfilename):
        print ( inputfilename + " not found... Abort")    
        sys.exit()
    
    with open(inputfilename, "rb") as fb:
        bn = fb.read()
    
    # print(type(bn))
    # print(bn)
    # print([b for b in bn])
    bnr = bytes([(255-b) for b in reversed(bn) ])
    #sys.stdout.buffer.write(bytes(reversed(bn)))
    sys.stdout.buffer.write(bnr)