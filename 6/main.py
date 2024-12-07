from enum import Enum
import numpy as np

class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4
    INVALID = 5

def testMap(m, h, w, pos, face):
    directions = []
    for yy in range(h):
        directions.append([])
        for _ in range(w):
            directions[yy].append([])
    while 0 <= pos[0] and pos[0] < h and 0 <= pos[1] and pos[1] < w:
        y,x = pos
        if m[y][x] == 'X' and (face in directions[y][x]):
            return True
        m[y][x] = 'X'
        directions[y][x].append(face)
        if face == Direction.UP:
            if 0 < y and m[y-1][x] == '#':
                face = Direction.RIGHT
            else:
                pos[0] -= 1
        elif face == Direction.RIGHT:
            if x < w - 1 and m[y][x+1] == '#':
                face = Direction.DOWN
            else:
                pos[1] += 1
        elif face == Direction.DOWN:
            if y < h - 1 and m[y+1][x] == '#':
                face = Direction.LEFT
            else:
                pos[0] += 1
        elif face == Direction.LEFT:
            if 0 < x and m[y][x-1] == '#':
                face = Direction.UP
            else:
                pos[1] -= 1
    return False

def main():
    fname = "input.txt"
    # read file line by line
    
    with open(fname) as f:
        dat = f.readlines()

    h = len(dat)
    w = len(dat[0])-1 # breakline character

    # first
    mOrig = []
    posOrig = [0,0]
    faceOrig = Direction.UP
    for y in range(h):
        mOrig.append([])
        for x in range(w):
            if dat[y][x] == '^':
                posOrig = [y,x]
            mOrig[y].append(dat[y][x])
    print(posOrig)
    m = []
    for y in range(h):
        m.append(mOrig[y].copy())
    pos = posOrig.copy()
    face = faceOrig
    testMap(m, h, w, pos, face)
    print(np.sum(np.array(m)=='X'))

    # second
    posToTry = []
    for y in range(h):
        for x in range(w):
            if m[y][x] == 'X' and (y != posOrig[0] or x != posOrig[1]):
                posToTry.append([y,x])
    s = 0
    
    for i in range(len(posToTry)):
        y,x=posToTry[i]
        m = []
        for yy in range(h):
            m.append(mOrig[yy].copy())
        m[y][x] = '#'
        pos = [45,47]
        face = Direction.UP
        
        if i % 500 == 0:
            print(f"{i}/{len(posToTry)}")
        
        inField = testMap(m, h, w, pos, face)
        if inField:
            s += 1

    print(s)

if __name__ == "__main__":
    main()