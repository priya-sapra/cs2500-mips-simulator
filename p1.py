'''
	p1.py - MIPS Pipelining Simulator
	Authors: Justin Gaskins, Bruno Kaufmann, Priya Sapra
	CSCI-2500 Computer Organization Final Group Project
'''

import sys

# I think I'm missing something like name == "__main__" or something
# I can't find it at the moment, but if you know it just add it in...

# assign mode - F for Forwarding and N for Non-forwarding
mode = sys.argv[1]

# open and parse file
file = open(sys.argv[2])
raw_file = file.read()
contents = raw_file.split("\n")

# initialize variables
cycles_header = "CPU Cycles ===> 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16"

# Print start
print("START OF SIMULATION ", end = "")
if (mode == "F"):
	print("(forwarding)")
else:
	print("(no forwarding)")

# Go through the cycles
for i in range(0,16):
	print(cycles_header)


# End of the simulation
print("END OF SIMULATION")

# print("Contents: ", contents)