
def showMap(map):
    mapStr = ""
    for l in map:
        mapStr += "".join(l) + "\n"
    print(mapStr)

def getScoreToBottomRight(mOrig, scoresOrig, r):
    scores = []
    for l in scoresOrig:
        scores.append(l.copy())
    m = []
    for l in mOrig:
        m.append(l.copy())
    toVisit = [(0,0)]
    while len(toVisit) > 0:
        x, y = toVisit.pop(0)
        m[y][x] = 'x'
        currentScore = scores[y][x]
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx*dy != 0: continue
                if 0 <= x+dx < r and 0 <= y+dy < r and m[y+dy][x+dx] == '.' and (scores[y+dy][x+dx] == -1 or scores[y+dy][x+dx] > currentScore + 1):
                    scores[y+dy][x+dx] = currentScore + 1
                    toVisit.append((x+dx, y+dy))
    return scores[r-1][r-1]

def main(fname, isTest):
    with open(fname) as f:
        dat = f.readlines()

    corrupted = []
    for l in dat:
        corrupted.append([int(a) for a in l.split(',')])
    #print(corrupted)

    m = []
    scores = []
    r = 7 if isTest else 71
    for y in range(r):
        m.append(['.']*r)
        scores.append([-1]*r)
    scores[0][0] = 0

    addCorruptedUntil = (12 if isTest else 1024)
    for i,c in enumerate(corrupted):
        if i < addCorruptedUntil:
            print(i,c)
            m[c[1]][c[0]] = '#'
    showMap(m)

    # first
    print(getScoreToBottomRight(m, scores, r))
    
    # second
    while getScoreToBottomRight(m, scores, r) != -1:
        c = corrupted[addCorruptedUntil]
        m[c[1]][c[0]] = '#'
        addCorruptedUntil += 1
    showMap(m)
    print(addCorruptedUntil)
    print(f"{c[0]},{c[1]}")
        



if __name__ == '__main__':
    isTest = False
    main('input_test.txt' if isTest else 'input.txt', isTest)