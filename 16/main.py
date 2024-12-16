from enum import Enum

class DIRERCTION(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Reindeer:
    def __init__(self, pos, direction):
        self.pos = pos
        self.direction = direction

    def __str__(self):
        return f"Reindeer at {self.pos} facing {self.direction}"
    
    def asKey(self):
        return (self.pos[0], self.pos[1], self.direction)

def showMap(map):
    mapStr = ""
    for l in map:
        mapStr += "".join(l) + "\n"
    print(mapStr)

def main(fname):
    with open(fname) as f:
        dat = f.readlines()

    map = []
    for l in dat:
        map.append(list(l.strip()))
    showMap(map)
    
    # first
    scores = {}
    startPos = (0, 0)
    endPos = (0, 0)
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == 'S':
                startPos = Reindeer((x,y), DIRERCTION.EAST)
                scores[startPos.asKey()] = 0
            if map[y][x] == 'E':
                endPos = (x, y)

    # some kind of Dijkstra's algorithm
    toProc = [startPos]
    while len(toProc) > 0:
        n = toProc.pop(0)
        currentScore = scores[n.asKey()]
        
        # add next position
        dx, dy = {DIRERCTION.NORTH: (0, -1), DIRERCTION.SOUTH: (0, 1), DIRERCTION.WEST: (-1, 0), DIRERCTION.EAST: (1, 0)}.get(n.direction, (0, 0))
        nextPos = Reindeer((n.pos[0] + dx, n.pos[1] + dy), n.direction)
        if 0 <= n.pos[0] + dx < len(map[0]) and 0 <= n.pos[1] + dy < len(map) \
            and map[n.pos[1] + dy][n.pos[0] + dx] in ['.', 'E'] and (nextPos.asKey() not in scores or scores[nextPos.asKey()] > currentScore + 1):
            toProc.append(nextPos)
            scores[nextPos.asKey()] = currentScore + 1
        
        # add current position with different directions
        for d in [DIRERCTION.NORTH, DIRERCTION.EAST, DIRERCTION.SOUTH, DIRERCTION.WEST]:
            nextPos = Reindeer(n.pos, d)
            if n.direction != d and (nextPos.asKey() not in scores or scores[nextPos.asKey()] > currentScore + 1000):
                toProc.append(nextPos)
                scores[nextPos.asKey()] = currentScore + 1000

    # get the min score with direction
    minScore = None
    endReindeerPos = None
    for d in [DIRERCTION.NORTH, DIRERCTION.EAST, DIRERCTION.SOUTH, DIRERCTION.WEST]:
        endReindeerPos = Reindeer(endPos, d)
        if endReindeerPos.asKey() in scores:
            if minScore is None or scores[endReindeerPos.asKey()] < minScore:
                minScore = scores[endReindeerPos.asKey()]
                endReindeerPos = Reindeer(endPos, d)
    print(minScore)

    # second

    # starting from the end position, step back to the start position
    areOnBestPath = set()
    toVisit = [endReindeerPos]
    while len(toVisit) > 0:
        n = toVisit.pop(0)
        areOnBestPath.add(n.pos)
        currentScore = scores[n.asKey()]

        # best path is when taking a step back, will modify the score to the neighbor's best score
        dx, dy = {DIRERCTION.NORTH: (0, -1), DIRERCTION.SOUTH: (0, 1), DIRERCTION.WEST: (-1, 0), DIRERCTION.EAST: (1, 0)}.get(n.direction, (0, 0))
        nextPos = Reindeer((n.pos[0] - dx, n.pos[1] - dy), n.direction)
        if 0 <= n.pos[0] - dx < len(map[0]) and 0 <= n.pos[1] - dy < len(map) \
            and map[n.pos[1] - dy][n.pos[0] - dx] in ['.', 'S'] and nextPos.asKey() in scores and scores[nextPos.asKey()] == currentScore - 1:
            toVisit.append(nextPos)

        for d in [DIRERCTION.NORTH, DIRERCTION.EAST, DIRERCTION.SOUTH, DIRERCTION.WEST]:
            nextPos = Reindeer(n.pos, d)
            if d != n.direction and nextPos.asKey() in scores and scores[nextPos.asKey()] == currentScore - 1000:
                toVisit.append(nextPos)
    print(len(areOnBestPath))

if __name__ == '__main__':
    main('input.txt')