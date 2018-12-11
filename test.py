'''
	p1.py - MIPS Pipelining Simulator
	Authors: Justin Gaskins, Bruno Kaufmann, Priya Sapra
	CSCI-2500 Computer Organization Final Group Project
'''

import sys
from Instruction import Instruction

def assignRegisters(i, registers):
	split_i = i.mips.split(" ")
	split_i = split_i[1].split(",")
	target_reg = split_i[0]
	val = split_i[-1]
	if val.isdigit():
		registers[target_reg] = int(val)

if __name__ == "__main__":
	if len(sys.argv) == 3:
		# assign mode - F for Forwarding and N for Non-forwarding
		mode = sys.argv[1]

		# open and parse file
		file = open(sys.argv[2])
		raw_file = file.read().strip()
		contents = raw_file.split("\n")
		file.close()
	else:
		print("ERROR: Usage p1.py [mode] [input]")
		sys.exit();

	# initialize variables
	cycles_header = "{:<20}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}"\
	cycles_header = "{:<20}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{}"\
					.format("CPU Cycles ===>", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
	instructions = []
	registers = {'$s0': 0, '$s1': 0, '$s2': 0, '$s3': 0,
				 '$s4': 0, '$s5': 0, '$s6': 0, '$s7': 0,
				 '$t0': 0, '$t1': 0, '$t2': 0, '$t3': 0,
				 '$t4': 0, '$t5': 0, '$t6': 0, '$t7': 0,
				 '$t8': 0, '$t9': 0}
	# s0 = s1 = s2 = s3 = s4 = s5 = s6 = s7 = 0
	# t0 = t1 = t2 = t3 = t4 = t5 = t6 = t7 = t8 = t9 = 0
	start_cycle = 0	# This is to know at one cycle the instruction has started

	for inst in contents:
		instructions.append(Instruction(inst, 0, 0, start_cycle, False))
		start_cycle = start_cycle + 1	# Each instruction will start at the cycle that is equal to the # instruction that it is in order
										# for example - first instruction will start at cycle 0, second instruction starts at cycle 1 ...

	# Print start
	print("START OF SIMULATION ", end = "")
	if (mode == "F"):
		print("(forwarding)")
	else:
		print("(no forwarding)")

	# Go through the cycles (cc = clock cycle)
	for cc in range(0,16):

      	# If the last instruction is done, we stop printing entirely
		if instructions[-1].complete:
			break

		print("-" * 82)
		print(cycles_header)

		for x in instructions:
			# Advance stage if needed (the check is done in the function)
			x.advanceStage(cc)

			if x.complete:
				assignRegisters(x, registers)

			# Only print instruction if instruction has started
			if (cc >= x.start):
				print(x)


		print()
		print("$s0 = {:<14}$s1 = {:<14}$s2 = {:<14}$s3 = {:<14}".format(registers["$s0"], registers["$s1"], registers["$s2"], registers["$s3"]))
		print("$s4 = {:<14}$s5 = {:<14}$s6 = {:<14}$s7 = {:<14}".format(registers["$s4"], registers["$s5"], registers["$s6"], registers["$s7"]))
		print("$t0 = {:<14}$t1 = {:<14}$t2 = {:<14}$t3 = {:<14}".format(registers["$t0"], registers["$t1"], registers["$t2"], registers["$t3"]))
		print("$t4 = {:<14}$t5 = {:<14}$t6 = {:<14}$t7 = {:<14}".format(registers["$t4"], registers["$t5"], registers["$t6"], registers["$t7"]))
		print("$t8 = {:<14}$t9 = {:<14}".format(registers["$t8"], registers["$t9"]))
		print("$s0 = {:<14}$s1 = {:<14}$s2 = {:<14}$s3 = {}".format(registers["$s0"], registers["$s1"], registers["$s2"], registers["$s3"]))
		print("$s4 = {:<14}$s5 = {:<14}$s6 = {:<14}$s7 = {}".format(registers["$s4"], registers["$s5"], registers["$s6"], registers["$s7"]))
		print("$t0 = {:<14}$t1 = {:<14}$t2 = {:<14}$t3 = {}".format(registers["$t0"], registers["$t1"], registers["$t2"], registers["$t3"]))
		print("$t4 = {:<14}$t5 = {:<14}$t6 = {:<14}$t7 = {}".format(registers["$t4"], registers["$t5"], registers["$t6"], registers["$t7"]))
		print("$t8 = {:<14}$t9 = {}".format(registers["$t8"], registers["$t9"]))


	# End of the simulation
	print("-" * 82)
	print("END OF SIMULATION")
