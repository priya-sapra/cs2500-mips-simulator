'''
	p1.py - MIPS Pipelining Simulator
	Authors: Justin Gaskins, Bruno Kaufmann, Priya Sapra
	CSCI-2500 Computer Organization Final Group Project
'''

import sys
from Instruction import Instruction

# I think I'm missing something like name == "__main__" or something
# I can't find it at the moment, but if you know it just add it in...
# Gotcha
if __name__ == "__main__":
	if len(sys.argv) == 3:
		# assign mode - F for Forwarding and N for Non-forwarding
		mode = sys.argv[1]

		# open and parse file
		file = open(sys.argv[2])
		raw_file = file.read()
		contents = raw_file.split("\n")
		file.close()
	else:
		print("ERROR: Usage p1.py [mode] [input]")
		sys.exit();

	# initialize variables
	cycles_header = "{:<20} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4}".format("CPU Cycles ===>", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
	inst = Instruction()

	# Print start
	print("START OF SIMULATION ", end = "")
	if (mode == "F"):
		print("(forwarding)")
	else:
		print("(no forwarding)")

	# Go through the cycles
	for i in range(0,16):
		print("-" * 98)
		print(cycles_header)
		print(inst)
		print()


	# End of the simulation
	print("-" * 98)
	print("END OF SIMULATION")

	# print("Contents: ", contents)
