#!/usr/bin/python
###IP Address conversion script ###

import sys, getopt # Required for argv
#from netaddr import IPAddress # Required for mask conversion

#########################################################################
###  CONSTANTS  ###
#########################################################################

VERSION = 1

#########################################################################

#########################################################################
### Take input variables for use later ###
#########################################################################
argv = sys.argv[1:]
outputfile = ''
try:
    opts, args = getopt.getopt(argv,"hs:d:a:m:",["src-format=","dst-format=","src-mask"])
except getopt.GetoptError:
    print 'mask-converter.py -s <Source Format> -d <Destination Format> -m <Source Mask>'
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print 'mask-converter.py -s <Source Format> -d <Destination Format> -m <Source Mask>'
        sys.exit()
    elif opt in ("-s", "--src-format"):
        src_format = arg
    elif opt in ("-d", "--dest-format"):
        dst_format = arg
    elif opt in ("-m", "--src-mask"):
        src_mask = arg

#########################################################################

#########################################################################
### Convert Subnet mask (255.255.255.255) into CIDR prefix (/32) ###
#########################################################################
def subnetTocidr(src_mask):
    new_cidr = sum([bin(int(x)).count("1") for x in src_mask.split(".")])
    return new_cidr

#########################################################################
### Run the script and all its routines ###
#########################################################################
def main():
    if dst_format == "cidr":
	    new_cidr = subnetTocidr(src_mask)
	    print src_mask + " --> " + str(new_cidr)

if __name__ == '__main__':
    main()