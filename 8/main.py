import itertools

def main(fname):
    # read file line by line
    
    with open(fname) as f:
        dat = f.readlines()
    
    #first
    h = len(dat)
    w = len(dat[0])-1 # breakline character
    s = 0
    print(h,w)
    m = {}
    emptyPoses = set()
    for i in range(h):
        for j in range(w):
            c = dat[i][j]
            if c == '.':
                emptyPoses.add((i,j))
                continue
            if c not in m.keys():
                m[c] = []
            m[c].append([i,j])
    antinodes = set()
    for c, positions in m.items():
        # take each pair of positions
        it = 0
        for p1, p2 in itertools.combinations(positions, 2):
            it += 1
            dy = p2[0] - p1[0]
            dx = p2[1] - p1[1]
            # second
            for multiplier in range(max(w,h)):
                if 0 <= p2[0] + multiplier * dy < h and 0 <= p2[1] + multiplier * dx < w:
                    antinodes.add((p2[0] + multiplier * dy, p2[1] + multiplier * dx))
                if 0 <= p1[0] - multiplier * dy < h and 0 <= p1[1] - multiplier * dx < w:
                    antinodes.add((p1[0] - multiplier * dy, p1[1] - multiplier * dx))
    print(len(antinodes))

if __name__ == "__main__":
    main("input.txt")