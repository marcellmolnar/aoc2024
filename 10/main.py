
def countTracks(dat, h, w, y, x):
    canMove = True
    assert int(dat[y][x]) == 0
    # first with set, second with list
    #achievableNodes = {0: set()}
    #achievableNodes[0].add((y,x))
    achievableNodes = {0: [(y,x)]}
    searchFor = 1
    while searchFor <= 9:
        achievableNodes[searchFor] = [] #set()
        for pos in achievableNodes[searchFor-1]:
            # can move up
            if 0 < pos[0] and int(dat[pos[0]-1][pos[1]]) == searchFor:
                achievableNodes[searchFor].append((pos[0]-1,pos[1]))
            # can move down
            if pos[0] < h - 1 and int(dat[pos[0]+1][pos[1]]) == searchFor:
                achievableNodes[searchFor].append((pos[0]+1,pos[1]))
            # can move left
            if 0 < pos[1] and int(dat[pos[0]][pos[1]-1]) == searchFor:
                achievableNodes[searchFor].append((pos[0],pos[1]-1))
            # can move right
            if pos[1] < w - 1 and int(dat[pos[0]][pos[1]+1]) == searchFor:
                achievableNodes[searchFor].append((pos[0],pos[1]+1))
        searchFor += 1
    print(len(achievableNodes[9]))
    return len(achievableNodes[9])


def main(fname):
    # read file line by line
    
    with open(fname) as f:
        dat = f.readlines()

    # first
    m = {}
    h = len(dat)
    w = len(dat[0])-1 # breakline character
    # search zeros
    for i in range(h):
        for j in range(w):
            if dat[i][j] == '0':
                m[(i,j)] = 0

    s = 0
    for pos in m.keys():
        s += countTracks(dat, h, w, pos[0], pos[1])
    print(s)

if __name__ == "__main__":
    main("input.txt")