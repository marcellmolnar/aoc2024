def parseFullValue(values, n):
    result = 0
    bits = 0
    for key, val in values.items():
        if key.startswith(n):
            position = int(key[1:])
            bits = max(bits, position+1)
            result += val << position
    return result, bits

def getOutput(dat, remainingEqs, values):
    while len(remainingEqs) > 0:
        j = remainingEqs.pop(0)
        line = dat[j]
        equation, resultName = line.split(' -> ')
        resultName = resultName[:-1]
        inA, operation, inB = equation.split(' ')
        if inA not in values or inB not in values:
            remainingEqs.append(j)
            continue
        inA = values[inA]
        inB = values[inB]
        values[resultName] = (inA | inB) if operation == 'OR' else ((inA & inB) if operation == 'AND' else (inA ^ inB))
    return values

def searchForOperands(dat, remainingEqs, values, targetOperation, targetOperands):
    for j in remainingEqs:
        line = dat[j]
        equation, resultName = line.split(' -> ')
        resultName = resultName[:-1]
        inA, operation, inB = equation.split(' ')
        if inA in targetOperands and inB in targetOperands and inA != inB:
            if operation == targetOperation:
                return j, resultName
    return None

def second(dat, remainingEqs, values, inputBits):
    remainingEqsOrig = remainingEqs.copy()

    # first collect operations that are involved in the production of each bit
    addsTo = [-1] * inputBits
    carriesTo = [-1] * inputBits
    targets = [-1] * inputBits
    for i in range(inputBits):
        targetOperands = [f'x{i:02}', f'y{i:02}']
        targetZ = f'z{i:02}'
        for op in ['AND', 'XOR']:
            r = searchForOperands(dat, remainingEqs, values, op, targetOperands)
            assert r is not None
            j, resultName = r
            if op == 'AND':
                carriesTo[i] = resultName
            elif op == 'XOR':
                addsTo[i] = resultName

        for j in remainingEqsOrig:
            line = dat[j]
            _, resultName = line.split(' -> ')
            resultName = resultName[:-1]
            if resultName == targetZ:
                targets[i] = j

    # running the scipt one-by-one, it will break at the first error, which can be corrected manually
    lastCarry = carriesTo[0]
    for i in range(1, inputBits):
        z = searchForOperands(dat, remainingEqs, values, 'XOR', [lastCarry, addsTo[i]])
        if z is None or z[1] != f'z{i:02}':
            print(f"{i}: {lastCarry} xor {addsTo[i]} -> {z[1] if z is not None else 'not found'}")
            break
        f = searchForOperands(dat, remainingEqs, values, 'AND', [lastCarry, addsTo[i]])
        if f is None:
            print(f"{i}: {lastCarry} and {addsTo[i]} -> {f[1] if f is not None else 'not found'}")
            break
        currentCarry = searchForOperands(dat, remainingEqs, values, 'OR', [carriesTo[i], f[1]])
        if currentCarry is None:
            print(f"{i}: {carriesTo[i]} or {addsTo[i]} -> {currentCarry[1] if currentCarry is not None else 'not found'}")
            break
        lastCarry = currentCarry[1]        

def main(fname):
    with open(fname) as f:
        dat = f.readlines()

    values = {}
    i = 0
    for i in range(len(dat)):
        line = dat[i]
        if line == '\n':
            break
        name, val = line.split(': ')
        values[name] = int(val)
    x, xbits = parseFullValue(values, 'x')
    y, ybits = parseFullValue(values, 'y')
    assert xbits == ybits
    target = x + y

    remainingEqs = [i for i in range(i+1, len(dat))]
    remainingEqsOrig = remainingEqs.copy()

    # first
    values = getOutput(dat, remainingEqs, values)
    z,_ = parseFullValue(values, 'z')
    print(z)

    # second
    second(dat, remainingEqsOrig, values, xbits)

    # from manual corrections
    toCorrect = ["kwb","z12","qkf","z16","tgr","z24","cph","jqn"]
    print(",".join(sorted(toCorrect)))
    assert z == target

if __name__ == '__main__':
    isTest = False
    main('input_test_2.txt' if isTest else 'input.txt')