#!/usr/bin/env python3
## display file to the screen - .read()
configfile = open("vlanconfig.cfg", "r")

## make a list of file lines - .readlines()

configlist = configfile.readlines()
print(configlist)

i=0
## Iterate through configlist

for x in configlist:
    i = i + 1
    if i%2 == 1:
        print(x.strip(),end=" ")
    else:
        print(x.strip())





