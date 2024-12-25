from itertools import combinations

maxHeight = 5
class PinDevice():
    def __init__(self, isKey):
        self.lines = []
        self.isKey = isKey

    def addLine(self, line):
        if len(self.lines) == 5:
            return
        self.lines.append(line)
        
    def toHeights(self):
        heights = [sum([line[i]=='#' for line in self.lines]) for i in range(len(self.lines[0]))]
        assert all([h <= maxHeight for h in heights]), f"Invalid heights: {heights}"
        return heights

def main(fname):
    with open(fname) as f:
        dat = f.readlines()

    isKey = None
    devicesOrig = []
    for line in dat:
        l = line.strip()
        if line == '\n':
            isKey = None
        elif isKey is None:
            assert all([c == '#' for c in l]) or all([c == '.' for c in l]), f"Invalid line: {l}"
            isKey = all([c == '.' for c in l])
            devicesOrig.append(PinDevice(isKey))
        else:
            devicesOrig[-1].addLine(l)

    # remove duplicates
    alreadyAdded = []
    devices = []
    for d in devicesOrig:
        if all(not all([x==y for x,y in zip((d.isKey, *d.toHeights()), a)]) for a in alreadyAdded):
            devices.append(d)
            alreadyAdded.append((d.isKey, *d.toHeights()))

    # first
    s = 0
    for pair in combinations(devices, 2):
        if pair[0].isKey != pair[1].isKey:
            sums = [a + b for a, b in zip(pair[0].toHeights(), pair[1].toHeights())]
            if all([s <= maxHeight for s in sums]):
                s += 1
    print(s)


if __name__ == '__main__':
    isTest = False
    main('input_test.txt' if isTest else 'input.txt')