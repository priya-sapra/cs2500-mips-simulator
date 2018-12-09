class Instruction(object):
    cycles = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']

    def __init__( self, mips="", stage=0, stalls=0, complete=False):
        self.mips = mips
        self.stage = stage
        self.stalls = stalls
        self.complete = complete

    def __str__(self):
    	return ("{:<20} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4}").format(
    			self.mips, self.cycles[0], self.cycles[1], self.cycles[2], self.cycles[3],
    			self.cycles[4], self.cycles[5], self.cycles[6], self.cycles[7],
                self.cycles[8], self.cycles[9], self.cycles[10], self.cycles[11],
                self.cycles[12], self.cycles[13], self.cycles[14], self.cycles[15])
