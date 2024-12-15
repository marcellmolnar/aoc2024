def showMap(map):
    mapStr = ""
    for l in map:
        mapStr += "".join(l) + "\n"
    print(mapStr)

def getStartingPos(map):
    for l in map:
        for s in l:
            if s == '@':
                return (l.index(s), map.index(l))
    return (0,0)
    
def calcScore(map, c):
    score = 0
    for y,l in enumerate(map):
        for x,s in enumerate(l):
            if s == c:
                score += y*100 + x
    return score

def first(dat):
    isMap = True
    map = []
    movements = []
    i=0
    for line in dat:
        if isMap:
            if line == '\n':
                isMap = False
            else:
                map.append(list(line.strip()))
        else:
            movements.append(line)
    print("map", len(map), len(map[0]))
    print("movements", len(movements))

    # first
    pos = getStartingPos(map)
    print(pos)

    for ms in movements:
        for m in ms:
            dx, dy = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}.get(m, (0, 0))
            boxesInFront = 0
            toCheckX = pos[0] + (boxesInFront + 1) * dx
            toCheckY = pos[1] + (boxesInFront + 1) * dy
            while 0 <= toCheckY < len(map) and 0 <= toCheckX < len(map[0]) and map[toCheckY][toCheckX] == 'O':
                boxesInFront += 1
                toCheckX = pos[0] + (boxesInFront + 1) * dx
                toCheckY = pos[1] + (boxesInFront + 1) * dy
            if 0 <= toCheckY < len(map) and 0 <= toCheckX < len(map[0]) and map[toCheckY][toCheckX] == '.':
                map[toCheckY][toCheckX] = 'O'
                map[pos[1]][pos[0]] = '.'
                pos = (pos[0] + dx, pos[1] + dy)
                map[pos[1]][pos[0]] = '@'
            #showMap(map)

    score = calcScore(map, 'O')
    print(score)

def second(dat):
    isMap = True
    map = []
    movements = []
    i=0
    for line in dat:
        if isMap:
            if line == '\n':
                isMap = False
            else:
                map.append(list("".join(list([{"@": "@.", ".": "..", "O": "[]", "#": "##"}[s] for s in line.strip()])).strip()))
        else:
            movements.append(line)
    print("map", len(map), len(map[0]))
    print("movements", len(movements))
    showMap(map)

    pos = getStartingPos(map)
    for ms in movements:
        for m in ms:
            dx, dy = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}.get(m, (0, 0))
            boxesInFront = 0
            # horizontal movement is easy
            if dy == 0:
                toCheckX = pos[0] + (boxesInFront + 1) * dx
                while 0 <= toCheckX < len(map[0]) and map[pos[1]][toCheckX] in ['[', ']']:
                    boxesInFront += 1
                    toCheckX = pos[0] + (boxesInFront + 1) * dx
                if 0 <= toCheckX < len(map[0]) and map[pos[1]][toCheckX] == '.':
                    while toCheckX != pos[0]:
                        map[pos[1]][toCheckX] = map[pos[1]][toCheckX-dx]
                        toCheckX -= dx
                    map[pos[1]][pos[0]] = '.'
                    pos = (pos[0] + dx, pos[1])
                    map[pos[1]][pos[0]] = '@'
            else:
                toCheckInRow = {}
                toCheckInRow[pos[1]] = [pos[0]]
                canPush = True
                checkRow = pos[1]
                while canPush and len(toCheckInRow[checkRow]) > 0:
                    toCheckInRow[checkRow+dy] = set()
                    for b in toCheckInRow[checkRow]:
                        if 0 <= checkRow+dy < len(map):
                            if map[checkRow+dy][b] in ['[', ']']:
                                toCheckInRow[checkRow+dy].add(b)
                                toCheckInRow[checkRow+dy].add(b+(1 if map[checkRow+dy][b] == '[' else -1))
                            if map[checkRow+dy][b] == '#':
                                canPush = False
                    checkRow += dy

                if canPush:
                    for r in range(checkRow-dy, pos[1]-dy, -dy): # if canPush, then checkRow is empty
                        for b in toCheckInRow[r]:
                            map[r+dy][b] = map[r][b]
                            map[r][b] = '.'
                    map[pos[1]][pos[0]] = '.'
                    map[pos[1]+dy][pos[0]+dx] = '@'
                    pos = (pos[0], pos[1] + dy)
            #showMap(map)

    score = calcScore(map, '[')
    print(score)

def main(fname):
    with open(fname) as f:
        dat = f.readlines()

    #first(dat)
    second(dat)

if __name__ == '__main__':
    main('input.txt')