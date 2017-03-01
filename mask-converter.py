#!/usr/bin/python
###MAC Address conversion script ###

import sys, getopt # Required for argv

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
        src_format = str(arg)
    elif opt in ("-d", "--dest-format"):
        dst_format = str(arg)
    elif opt in ("-m", "--src-mask"):
        src_mask = str(arg)

#########################################################################

#########################################################################
### Convert Subnet mask (255.255.255.255) into CIDR prefix (/32) ###
#########################################################################
def subnetTocidr(src_mask):
    new_cidr = sum([bin(int(x)).count("1") for x in src_mask.split(".")])
    return new_cidr

#########################################################################
### Convert CIDR prefix (/32) into subnetmask (255.255.255.255) ###
#########################################################################
def cidrTosubnet(src_mask):
    #new_subnet = 0xffffffff ^ (1 << 32 - int(src_mask)) - 1
    new_subnet = '.'.join([str((0xffffffff << (32 - int(src_mask)) >> i) & 0xff) for i in [24, 16, 8, 0]])
    return new_subnet

#########################################################################
### Run the script and all its routines ###
#########################################################################
def main():
    if dst_format == "cidr":
	    new_cidr = subnetTocidr(src_mask)
	    print src_mask + " --> " + str(new_cidr)

    if dst_format == "subnet":
        new_subnet = cidrTosubnet(src_mask)
        print src_mask + " --> " + str(new_subnet)

if __name__ == '__main__':
    main()
