import itertools

def main(fname):
    # read file line by line
    
    with open(fname) as f:
        dat = f.readlines()

    # first
    eqs = len(dat)
    s = 0
    for i in range(eqs):
        eq = dat[i]
        desiredValue = eq.split(':')[0]
        values = eq.split(':')[1][1:-1].split(' ') # [1:-1] to remove the space at the beginning and new line at the end
        for ops in itertools.product(['+','*','||'], repeat=len(values)-1):
            v = int(values[0])
            eqS = values[0]
            for j in range(len(ops)):
                eqS += ops[j] + values[j+1]
                if ops[j] == '+':
                    v += int(values[j+1])
                elif ops[j] == '*':
                    v *= int(values[j+1])
                # second
                else:
                    v = eval(str(v) + values[j+1])
            if v == int(desiredValue):
                s += v
                break
    print(s)

if __name__ == "__main__":
    main("input.txt")