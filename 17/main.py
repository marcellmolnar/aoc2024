
def getOutputOfProgram(registerA, registerB, registerC, instructions):

    def getOperand(op):
        if op <= 3:
            return op
        elif op == 4:
            return registerA
        elif op == 5:
            return registerB
        elif op == 6:
            return registerC
        assert False

    outStr = ""
    ip = 0
    while 0 <= ip < len(instructions):
        if instructions[ip] == 0:
            assert ip+1 < len(instructions)
            registerA = int(registerA / pow(2,getOperand(instructions[ip+1])))
            ip += 2
        elif instructions[ip] == 1:
            assert ip+1 < len(instructions)
            registerB = registerB ^ instructions[ip+1]
            ip += 2
        elif instructions[ip] == 2:
            assert ip+1 < len(instructions)
            registerB = getOperand(instructions[ip+1]) % 8
            ip += 2
        elif instructions[ip] == 3:
            if registerA == 0:
                ip += 2
            else:
                assert ip+1 < len(instructions)
                ip = instructions[ip+1]
        elif instructions[ip] == 4:
            registerB = registerB ^ registerC
            ip += 2
        elif instructions[ip] == 5:
            assert ip+1 < len(instructions)
            if outStr != "":
                outStr += ","
            outStr += str(getOperand(instructions[ip+1]) % 8)
            ip += 2
        elif instructions[ip] == 6:
            assert ip+1 < len(instructions)
            registerB = int(registerA / pow(2,getOperand(instructions[ip+1])))
            ip += 2
        elif instructions[ip] == 7:
            assert ip+1 < len(instructions)
            registerC = int(registerA / pow(2,getOperand(instructions[ip+1])))
            ip += 2
        else:
            assert False
    return outStr

def main(fname):
    with open(fname) as f:
        dat = f.readlines()

    registerA = int(dat[0].split('Register A: ')[1].strip())
    registerB = int(dat[1].split('Register B: ')[1].strip())
    registerC = int(dat[2].split('Register C: ')[1].strip())
    print(registerA, registerB, registerC)

    instructions = list(map(lambda x: int(x), dat[4].split('Program: ')[1].split(',')))
    print(instructions)
    
    # first
    print(getOutputOfProgram(registerA, registerB, registerC, instructions))

    # second
    def solveFor(p, r):
        if p < 0:
            print(r)
            return True
        # try adding 3 bits to the right
        found = False
        for i in range(8):
            # reverse engineered instructions
            a = r << 3 | i
            b = a % 8
            b = b ^ 1
            c = int(a / pow(2, b))
            b = b ^ 5
            b = b ^ c
            o = b % 8
            # if the output is correct, try solving for the next instruction
            if o == instructions[p] and solveFor(p - 1, a):
                return True
        return found

    solveFor(len(instructions)-1, 0)

if __name__ == '__main__':
    main('input.txt')