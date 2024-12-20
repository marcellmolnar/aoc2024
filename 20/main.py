from itertools import product

class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def asKey(self):
        return f'{self.x},{self.y}'
    
    def keyToCoords(key):
        x, y = key.split(',')
        return Coords(int(x), int(y))

def genScores(m, start):
    scores = [[None for _ in range(len(m[0]))] for _ in range(len(m))]
    scores[start.y][start.x] = 0
    toVisit = [start]
    while toVisit:
        c = toVisit.pop(0)
        currentScore = scores[c.y][c.x]
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx * dy != 0:
                    continue
                if 0 <= c.x + dx < len(m[0]) and 0 <= c.y + dy < len(m):
                    if m[c.y + dy][c.x + dx] in ['.', 'E']:
                        if (scores[c.y + dy][c.x + dx] is None or scores[c.y + dy][c.x + dx] > currentScore + 1):
                            scores[c.y + dy][c.x + dx] = currentScore + 1
                            toVisit.append(Coords(c.x + dx, c.y + dy))
    return scores

def genCheatPaths(m, jumps):
    cheatPaths = {}
    alreadyAdded = {}
    for y in range(len(m)):
        for x in range(len(m[y])):
            current = Coords(x, y)
            possibleEnds = {}
            if m[y][x] in ['.','S'] :
                for dx, dy in product(range(-jumps, jumps + 1), repeat=2):
                    if dx == dy == 0 or abs(dx) + abs(dy) > jumps:
                        continue
                    np = Coords(x + dx, y + dy)
                    if 0 <= np.x < len(m[0]) and 0 <= np.y < len(m) and m[np.y][np.x] in ['.', 'E']:
                        possibleEnds[np.asKey()] = abs(dx) + abs(dy)
            cheatPaths[current.asKey()] = []
            alreadyAdded[current.asKey()] = set()
            for endKey, score in possibleEnds.items():
                end = Coords.keyToCoords(endKey)
                if endKey not in alreadyAdded[current.asKey()]:
                    cheatPaths[current.asKey()].append((end,score))
                    alreadyAdded[current.asKey()].add(end.asKey())
    return cheatPaths

def solve(m, scores, jumps):
    cheatPaths = genCheatPaths(m, jumps)

    s = 0
    for cheatStartKey, ends in cheatPaths.items():
        cheatStart = Coords.keyToCoords(cheatStartKey)
        for cheatEnd, score in ends:
            endScore = scores[cheatEnd.y][cheatEnd.x]
            assert endScore is not None
            startScore = scores[cheatStart.y][cheatStart.x]
            assert startScore is not None

            diff = endScore - startScore - score
            if diff >= 100:
                s += 1
    print(s)
    assert (jumps == 20 and s == 1026446) or (jumps == 2 and s == 1438) or (jumps not in [2, 20])
            

def main(fname):
    with open(fname) as f:
        dat = f.readlines()

    m = [list(x.strip()) for x in dat]
    
    # first
    start = Coords(0, 0)
    end = Coords(0, 0)
    for y in range(len(m)):
        for x in range(len(m[y])):
            if m[y][x] == 'S':
                start.x, start.y = x, y
            if m[y][x] == 'E':
                end.x, end.y = x, y

    scores = genScores(m, start)

    # first
    solve(m, scores, 2)

    # second
    solve(m, scores, 20)


if __name__ == '__main__':
    isTest = False
    main('input_test.txt' if isTest else 'input.txt')