"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        pass
        # assign the memory allocation - 256 zeros
        self.ram = [0] * 0xFF * 256
        # Program Counter >> where calculations/current instructions are executed
        self.PC = 0
        # Instruction Register >> where a copy of the current instructions are kept
        self.IR = None
        # This register holds value between 0-255 (total of 256) for 8bites/registers
        self.register = [0] * 8

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        pass

        # Load Immediate - 3 bites
        LDI = 0b10000010
        # Instruction Register - 2 bites
        IR = self.ram[self.PC]	
        # exit programm - 1 bite     
        HLT = 0b00000001
        # print 
        PRN = 0b01000111

        running_cmd = True

        while running_cmd:
            # assing the the Instruction Register the memory address read that is stored in Program Counter
            IR = self.ram[self.PC]
            # assign first & second operand to ram allocation to perform instructions
            operand_a = self.ram[self.PC + 1]
            operand_b = self.ram[self.PC + 2]
            if IR == LDI:
                self.register[operand_a] = operand_b
                self.PC += 3
            # if Instruction Register = equals Print
            elif IR == PRN:
                # prints the numeric value stored in register
                print(self.register[operand_a])
                self.PC += 2
            # if Instruction Register = exit emulator
            elif IR == HLT:
                running_cmd = False
                self.PC += 1
            else:
                print(f"Error! Command not found >> {self.ram[self.PC]}")
                sys.exit(1)
