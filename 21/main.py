from helper import buttonA, neededMove, neededMoveController, moveToChar
import random
"""
keypad layout (k, robot):
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+

controller layout (c2, robot):
    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+

controller layout (c1, robot):
    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+

controller layout (c0, us):
    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+
"""


def valueToStr(v):
    if v == buttonA:
        return 'A'
    s = ""
    if v.real > 0:
        s += '>' * int(v.real)
    elif v.real < 0:
        s += '<' * abs(int(v.real))
    if v.imag < 0:
        s += 'v' * abs(int(v.imag))
    elif v.imag > 0:
        s += '^' * int(v.imag)
    return s

def main(fname):
    with open(fname) as f:
        dat = f.readlines()

    btns = [x[:-1] if x[-1] == '\n' else x for x in dat]
    print(btns)

    # initially everything is on button 'A'
    controllers = 3
    controllerStates = [buttonA] * (controllers-1)
    
    def solveControllers(dirC, level, s):
        if level == controllers:
            #print(valueToStr(dir), sep='', end='')
            for dir in [int(dirC.imag)*1j, int(dirC.real)]:
                s += valueToStr(dir)
            return s

        
        dirs = [int(dirC.real), int(dirC.imag)*(1j)]
        #print(dirs)
        if dirC == buttonA:
            dirs = [buttonA]
        #"""
        else:
            levelState = controllerStates[level-1]
            if dirs[0] * dirs[1] != 0:
                poses = [(1 if dirs[0] > 0 else -1), (1j if dirs[1].imag > 0 else -1j)]
                if levelState != poses[0] and levelState != poses[1]:
                    ms = [neededMoveController[(levelState, poses[0])], neededMoveController[(levelState, poses[1])]]
                    if abs(ms[1].real) + abs(ms[1].imag) < abs(ms[0].real) + abs(ms[0].imag):
                        dirs = [dirs[1], dirs[0]]
                elif levelState == poses[1]:
                    dirs = [dirs[1], dirs[0]]
        #"""
            if random.random() < 0.5:
                dirs = [dirs[1], dirs[0]]

        for dir in dirs:
            if abs(dir) == 0:
                continue
            
            levelState = controllerStates[level-1]
            pos = buttonA if dir == buttonA else (1 if dir.real > 0 else (-1 if dir.real < 0 else (1j if dir.imag > 0 else -1j)))
            rep = 1 if dir == buttonA else int(abs(dir))
            #print(f"level: {level}, levelState: {levelState}, dir: {dir}")
            if levelState != pos:
                movement = neededMoveController[(levelState, pos)]
                #print(levelState, pos, movement)
                s = solveControllers(movement, level+1, s)
                """
                if movement.imag != 0:
                    s = solveControllers(movement.imag*1j, level+1, s)
                if movement.real != 0:
                    s = solveControllers(movement.real, level+1, s)
                #"""
            for _ in range(rep):
                s = solveControllers(buttonA, level+1, s)
            controllerStates[level-1] = pos
        return s

    cs = [100000]* len(btns)
    print(sum(cs))
    for _ in range(10000):
        i = 0
        for code in btns:
            solution = ""
            keyPadState = buttonA
            for k in code:
                btn = int(k) if k != 'A' else buttonA
                #print((keyPadState, btn))
                m = neededMove[(keyPadState, btn)]
                solution = solveControllers(m, 1, solution)
                """
                if m.imag != 0:
                    solution = solveControllers((m.imag)*1j, 1, solution)
                if m.real != 0:
                    solution = solveControllers(m.real, 1, solution)
                #"""
                solution = solveControllers(buttonA, 1, solution)
                keyPadState = btn
            thisScore = len(solution)*int(code[:-1])
            cs[i] = min(cs[i], thisScore)
            #print(len(solution), thisScore, solution)
            i += 1
    print(sum(cs))
    # 125328 high
    # 106736 low
    # 117736 not

if __name__ == '__main__':
    isTest = False
    main('input_test.txt' if isTest else 'input.txt')