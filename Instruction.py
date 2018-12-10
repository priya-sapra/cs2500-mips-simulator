class Instruction(object):
    cycles = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']

    def __init__( self, mips="", stage=0, stalls=0, start=0, complete=False):
        self.mips = mips            # actual MIPS instruction
        self.stage = stage          # current stage (0-5 for -, ID, IF, EX, MEM, WB)
        self.stalls = stalls        # number of times the instruction needs to stall
        self.complete = complete    # finished all 5 stages
        self.start = start          # cycle when the instruction starts

    def __str__(self):
    	return ("{:<20}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}").format(
    			self.mips, self.cycles[0], self.cycles[1], self.cycles[2], self.cycles[3],
    			self.cycles[4], self.cycles[5], self.cycles[6], self.cycles[7],
                self.cycles[8], self.cycles[9], self.cycles[10], self.cycles[11],
                self.cycles[12], self.cycles[13], self.cycles[14], self.cycles[15])
    
    # add to the current stage
    def advanceStage(self, cycle): 
        # If the instruction should be started or has been started, add 1 to the stage
        if (cycle >= self.start) and (self.complete == False):
            self.stage += 1
        # If the cycle finished in the last cycle, the stage should be reset to 0
        elif self.complete:
            self.stage = 0
        # If we have reached a WB stage, the instruction is DONE
        if self.stage == 5:
            self.complete = True
        # set the clock cycle stage
        self.cycles[cycle] = self.stage

