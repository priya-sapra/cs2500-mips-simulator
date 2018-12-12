'''
	p1.py - MIPS Pipelining Simulator
	Authors: Justin Gaskins, Bruno Kaufmann, Priya Sapra
	CSCI-2500 Computer Organization Final Group Project
'''

import sys
from instructiontest import Instruction

# Assign a numerical value to a register if needed
def assignRegisters(i, registers):
	split_i = i.mips.split(" ")
	split_i = split_i[1].split(",")
	target_reg = split_i[0]
	val = split_i[-1]
	if val.isdigit():
		registers[target_reg] = int(val)

# If a register in i1 matches the TARGET REGISTER in i2, then there is a dependency and
# we return a 1 to indicate that there is ONE NOP
# Note: i2 is the the instruction that is 2 BEFORE i1
def checkOneNOP(i1, i2):
	for r1 in i1.regs:
		if r1 == i2.regs[0]:
			return 1
	return 0

# If a register in i1 matches the TARGET REGISTER in i2, then there is a dependency and
# we return a 2 to indicate that there are TWO NOPs
# Note: i2 is the the instruction that is 1 BEFORE i1
def checkTwoNOP(i1, i2):
	for r1 in i1.regs:
		if r1 == i2.regs[0]:
			return 2
	return 0

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
	cycles_header = "{:<20}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{}"\
					.format("CPU Cycles ===>", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
	instructions = []
	registers = {'$s0': 0, '$s1': 0, '$s2': 0, '$s3': 0,
				 '$s4': 0, '$s5': 0, '$s6': 0, '$s7': 0,
				 '$t0': 0, '$t1': 0, '$t2': 0, '$t3': 0,
				 '$t4': 0, '$t5': 0, '$t6': 0, '$t7': 0,
				 '$t8': 0, '$t9': 0}

	nop_obj = Instruction("nop", 0, 0, 0, False)

	start_cycle = 0	# This is to know at one cycle the instruction has started

	for inst in contents:
		# If the "instruction" is actually a loop hook, remove it from the list
		if inst[-1] == ":":
			contents.remove(inst)

	for inst in contents:
		instructions.append(Instruction(inst, 0, 0, start_cycle, False))
		start_cycle += 1	# Each instruction will start at the cycle that is equal to the # instruction that it is in order
							# for example - first instruction will start at cycle 0, second instruction starts at cycle 1 ...

	# Assign the registers that are used in each instruction
	for i in instructions:
		i.setRegisters(registers.keys())

	# Print start
	print("START OF SIMULATION ", end = "")
	if (mode == "F"):
		print("(forwarding)")
	else:
		print("(no forwarding)")


	nop = 0	# This is the NOP INDICATOR - if it is =1, there is one NOP, if it is =2, there are two NOPs
	nop_line = 0 # THis is the line where the NOP goes


	# Go through the cycles (cc = clock cycle)
	for cc in range(0,16):

		# If the last instruction is done, we stop printing entirely
		if instructions[-1].complete:
			break
		print("-" * 82)
		print(cycles_header)

		i_idx = 0	# This is the index of the instruction that we're on (helps with checkNOP functions)
		for x in instructions:
			# Advance stage if needed (the check is done in the function)
			x.advanceStage(cc)

			# If we CAN check one instruction back and we haven't already checked for NOP
			if (i_idx - 1 >= 0) and (cc >= x.start+2) and (nop == 0):
				nop = checkTwoNOP(x, instructions[i_idx-1])
				nop_line = i_idx 	# Set NOP line to mark wherever the NOP should be printed
				nop_obj.start = nop_line
				nop_obj.advanceNop(instructions[i_idx], cc)

			# If we CAN check two instructions back and we haven't already checked for NOP
			if (i_idx - 2 >= 0) and (cc >= x.start+2) and (nop == 0):
				nop = checkOneNOP(x, instructions[i_idx-2])
				nop_line = i_idx 	# Set NOP line to mark wherever the NOP should be printed
				nop_obj.start = nop_line
				nop_obj.advanceNop(instructions[i_idx], cc)

			# If current instruction is complete (reach WB), then we want to update the registers
			if x.complete:
				assignRegisters(x, registers)

			# Only print instruction if instruction has started
			if (cc >= x.start):
				if (nop > 0):
					for j in range (0, nop):
						print(nop_obj)
					nop = 0
				print(x)

			# Increment i_idx
			i_idx += 1


		print()
		print("$s0 = {:<14}$s1 = {:<14}$s2 = {:<14}$s3 = {}".format(registers["$s0"], registers["$s1"], registers["$s2"], registers["$s3"]))
		print("$s4 = {:<14}$s5 = {:<14}$s6 = {:<14}$s7 = {}".format(registers["$s4"], registers["$s5"], registers["$s6"], registers["$s7"]))
		print("$t0 = {:<14}$t1 = {:<14}$t2 = {:<14}$t3 = {}".format(registers["$t0"], registers["$t1"], registers["$t2"], registers["$t3"]))
		print("$t4 = {:<14}$t5 = {:<14}$t6 = {:<14}$t7 = {}".format(registers["$t4"], registers["$t5"], registers["$t6"], registers["$t7"]))
		print("$t8 = {:<14}$t9 = {}".format(registers["$t8"], registers["$t9"]))


	# End of the simulation
	print("-" * 82)
	print("END OF SIMULATION")
