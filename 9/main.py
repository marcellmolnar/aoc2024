import copy
from enum import Enum

class TYPE(Enum):
    FILE = 0
    FREE = 1
    INVALID = 2

class Block:
    def __init__(self, type, size, id):
        self.type = type
        self.size = size
        self.id = id

    def __str__(self):
        return f"{self.type} {self.size} {self.id}"
    
    def __repr__(self):
        return f"{self.type} {self.size} {self.id}"

def printBlocks(blocks):
    s = ""
    for b in blocks:
        for i in range(b.size):
            s += str(b.id) if b.type == TYPE.FILE else "."
    print(s)

def checkSum(blocks):
    s = 0
    p = 0
    for b in blocks:
        if b.type == TYPE.FILE:
            for i in range(b.size):
                s += (p+i) * b.id
        p += b.size
    return s

def getInput(dat):
    blocksLen = len(dat)
    blocks =  []
    isFile = True
    fId = 0
    for i in range(blocksLen):
        block = int(dat[i])
        blocks.append(Block(TYPE.FILE if isFile else TYPE.FREE, block, fId if isFile else -1))
        isFile = not isFile
        if isFile:
            fId += 1
    return blocks

def main(fname):
    # read file line by line
    
    with open(fname) as f:
        dat = f.read()

    # first
    blocks = getInput(dat)
    print(blocks)

    printBlocks(blocks)
    # reverse walkthrough
    firstFreeSpace = 1
    i = len(blocks)-1
    while firstFreeSpace < i:
        i = len(blocks)-1
        # search right most file
        while blocks[i].type == TYPE.FREE or blocks[i].size == 0:
            i -= 1

        b = blocks[i]
        if b.type == TYPE.FREE:
            continue
        # search first free space
        while blocks[firstFreeSpace].type == TYPE.FILE or blocks[firstFreeSpace].size == 0:
            firstFreeSpace += 1
        
        toMoveSize = min(b.size, blocks[firstFreeSpace].size)
        b.size -= toMoveSize
        blocks[firstFreeSpace].size -= toMoveSize
        blocks.insert(firstFreeSpace, Block(TYPE.FILE, toMoveSize, b.id))
        #print(f"Inserted {toMoveSize} from {b.id} to {firstFreeSpace}")

    printBlocks(blocks)
    print(checkSum(blocks))

    # second
    blocks = getInput(dat)
    print("orig")
    printBlocks(blocks)
    maxFileId = 0
    for b in blocks:
        if b.type == TYPE.FILE:
            maxFileId = max(maxFileId, b.id)
    for i in range(maxFileId, -1, -1):
        # search for file
        fileBlockId = -1
        #print(f"searching for {i}")
        for j in range(len(blocks)-1, -1, -1):
            if blocks[j].type == TYPE.FILE and blocks[j].id == i:
                fileBlockId = j
                break
        # search for free space
        freeSpaceId = -1
        sizeToMove = blocks[fileBlockId].size
        for j in range(len(blocks)):
            if blocks[j].type == TYPE.FREE and blocks[j].size >= sizeToMove:
                freeSpaceId = j
                #print(f"found for {fileBlockId} ({sizeToMove}) at {j} (free size: {blocks[j].size})")
                break
        if freeSpaceId != -1 and freeSpaceId < fileBlockId:
            #print(f"Inserted {sizeToMove} from {blocks[fileBlockId].id} to {freeSpaceId}")
            #blocks[fileBlockId].size = 0
            blocks[fileBlockId].type = TYPE.FREE
            blocks[freeSpaceId].size -= sizeToMove
            blocks.insert(freeSpaceId, Block(TYPE.FILE, sizeToMove, i))
        #printBlocks(blocks)
    printBlocks(blocks)
    print(checkSum(blocks))


if __name__ == "__main__":
    main("input.txt")