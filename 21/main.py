from helper import buttonA, neededMove, neededMoveController

def solveSteps(movements, controllerCount, doPrint=False):
    for _ in range(controllerCount):
        if doPrint:
            print(movements)
        newMovements = {}
        for m,c in movements.items():
            state = buttonA
            movement_list = []
            newElements = {}
            for k in m:
                if state == k:
                    movement_list.append([buttonA])
                    continue
                mC = neededMoveController[(state, k)]
                movement = []
                if (state == 1j and mC.real == -1) or (state == buttonA and mC.real == -2):
                    dirs = [int(mC.imag)*(1j), int(mC.real)]
                elif (state == -1 and mC.imag == 1):
                    dirs = [int(mC.real), int(mC.imag)*(1j)]
                else:
                    dirs = [int(mC.real), int(mC.imag)*(1j)]
                    if mC.real > 0:
                        dirs = [int(mC.imag)*(1j), int(mC.real)]
                for d in dirs:
                    pos = buttonA if d == buttonA else (1 if d.real > 0 else (-1 if d.real < 0 else (1j if d.imag > 0 else -1j)))
                    rep = 1 if d == buttonA else int(abs(d))
                    movement += [pos]*rep
                movement += [buttonA]
                movement_list.append(movement)
                state = k
            for m in movement_list:
                if tuple(m) not in newElements:
                    newElements[tuple(m)] = 1
                else:
                    newElements[tuple(m)] += 1
            for m in movement_list:
                newElements[tuple(m)] *= c
            for k,v in newElements.items():
                if k not in newMovements:
                    newMovements[k] = v
                else:
                    newMovements[k] += v
        movements = newMovements

    return sum(len(k)*v for k,v in movements.items())

def second(btns, controllerCount):
    minSteps = [None] * len(btns)
    for _ in range(1):
        for i, code in enumerate(btns):
            keyPadState = buttonA
            movements = {}
            movement = []
            for k in code:
                btn = int(k) if k != 'A' else buttonA
                mC = neededMove[(keyPadState, btn)]
                if (keyPadState == 1 and mC.imag == -1) or (keyPadState == 4 and mC.imag == -2) or (keyPadState == 7 and mC.imag == -3):
                    ms = [mC.real, mC.imag*1j]
                elif (keyPadState == 0 and mC.real == -1) or (keyPadState == buttonA and mC.real == -2):            
                    ms = [mC.imag*1j, mC.real]
                else:
                    ms = [mC.real, mC.imag*1j]
                    if mC.real > 0:
                        ms = [mC.imag*1j, mC.real]
                for m in ms:
                    pos = buttonA if m == buttonA else (1 if m.real > 0 else (-1 if m.real < 0 else (1j if m.imag > 0 else -1j)))
                    rep = 1 if m == buttonA else int(abs(m))
                    movement += [pos]*rep
                movement += [buttonA]
                keyPadState = btn
            movements[tuple(movement)] = 1
            v = solveSteps(movements, controllerCount)
            if minSteps[i] is None:
                minSteps[i] = v
            minSteps[i] = min(minSteps[i], v)

    print(sum(minSteps[i]*int(code[:-1]) for i, code in enumerate(btns)))

def main(fname):
    with open(fname) as f:
        dat = f.readlines()

    btns = [x[:-1] if x[-1] == '\n' else x for x in dat]
    print(btns)
    #first
    second(btns, 2)
    # second
    second(btns, 25)

if __name__ == '__main__':
    isTest = False
    main('input_test.txt' if isTest else 'input.txt')