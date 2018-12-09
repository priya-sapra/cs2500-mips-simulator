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
		raw_file = file.read().strip()
		contents = raw_file.split("\n")
		# print(*contents, sep = ", ")
		file.close()
	else:
		print("ERROR: Usage p1.py [mode] [input]")
		sys.exit();

	# initialize variables
	cycles_header = "{:<20}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}".format("CPU Cycles ===>", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
	instructions = []
	s0 = s1 = s2 = s3 = s4 = s5 = s6 = s7 = 0
	t0 = t1 = t2 = t3 = t4 = t5 = t6 = t7 = t8 = t9 = 0

	for inst in contents:
		instructions.append(Instruction(inst, 0, 0, False))

	# Print start
	print("START OF SIMULATION ", end = "")
	if (mode == "F"):
		print("(forwarding)")
	else:
		print("(no forwarding)")

	# Go through the cycles
	for i in range(0,16):
		print("-" * 82)
		print(cycles_header)
		for x in instructions:
			print(x)
		print()
		print("$s0 = {:<14}$s1 = {:<14}$s2 = {:<14}$s3 = {:<14}".format(s0, s1, s2, s3))
		print("$s4 = {:<14}$s5 = {:<14}$s6 = {:<14}$s7 = {:<14}".format(s4, s5, s6, s7))
		print("$t0 = {:<14}$t1 = {:<14}$t2 = {:<14}$t3 = {:<14}".format(t0, t1, t2, t3))
		print("$t4 = {:<14}$t5 = {:<14}$t6 = {:<14}$t7 = {:<14}".format(t4, t5, t6, t7))
		print("$t8 = {:<14}$t9 = {:<14}".format(t8, t9))


	# End of the simulation
	print("-" * 82)
	print("END OF SIMULATION")

	# print("Contents: ", contents)
