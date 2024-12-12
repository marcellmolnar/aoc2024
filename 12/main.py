
def main(fname):
    with open(fname) as f:
        dat = f.readlines()

    h = len(dat)
    w = len(dat[0]) - 1 # -1 to remove newline
    print(h, w)

    clusterSizes = {}
    clusterPerimeters = {}
    clusterIndex = 0
    posToClusterIndex = {}
    clusterToChar = {}
    for i in range(h):
        for j in range(w):
            if j == 0:
                print(i)
            if (i,j) not in posToClusterIndex.keys():
                print(f"starting @ {i},{j}")
                walkThrough = [(i,j)]
                clusterSizes[clusterIndex] = 0
                clusterToChar[clusterIndex] = dat[i][j]
                clusterPerimeters[clusterIndex] = 0
                while 0 < len(walkThrough):
                    y,x = walkThrough.pop(0)
                    #print(f"  walking through @ {y},{x}")
                    if (y,x) not in posToClusterIndex.keys():
                        posToClusterIndex[(y,x)] = clusterIndex
                        clusterSizes[clusterIndex] += 1

                    if y > 0 and dat[y-1][x] == dat[i][j] and (y-1,x) not in posToClusterIndex.keys() and (y-1,x) not in walkThrough:
                        walkThrough.append((y-1,x))
                    if y < h - 1 and dat[y+1][x] == dat[i][j] and (y+1,x) not in posToClusterIndex.keys() and (y+1,x) not in walkThrough:
                        walkThrough.append((y+1,x))
                    if x > 0 and dat[y][x-1] == dat[i][j] and (y,x-1) not in posToClusterIndex.keys() and (y,x-1) not in walkThrough:
                        walkThrough.append((y,x-1))
                    if x < w - 1 and dat[y][x+1] == dat[i][j] and (y,x+1) not in posToClusterIndex.keys() and (y,x+1) not in walkThrough:
                        walkThrough.append((y,x+1))
                clusterIndex += 1
                print("done")                    

            # add perimeters based on neighbors
            # horizontal
            #  top
            if i == 0:
                if j == 0 or dat[i][j-1] != dat[i][j]:
                    clusterPerimeters[posToClusterIndex[(i,j)]] += 1
            elif dat[i][j] != dat[i-1][j]:
                if j == 0 or dat[i][j-1] != dat[i][j] or dat[i-1][j-1] == dat[i][j]:
                    clusterPerimeters[posToClusterIndex[(i,j)]] += 1
            #  bottom
            if i == h - 1:
                if j == 0 or dat[i][j-1] != dat[i][j]:
                    clusterPerimeters[posToClusterIndex[(i,j)]] += 1
            elif dat[i][j] != dat[i+1][j]:
                if j == 0 or dat[i][j-1] != dat[i][j] or dat[i+1][j-1] == dat[i][j]:
                    clusterPerimeters[posToClusterIndex[(i,j)]] += 1

            # vertical
            #  left
            if j == 0:
                if i == 0 or dat[i-1][j] != dat[i][j]:
                    clusterPerimeters[posToClusterIndex[(i,j)]] += 1
            elif dat[i][j] != dat[i][j-1]:
                if i == 0 or dat[i-1][j] != dat[i][j] or dat[i-1][j-1] == dat[i][j]:
                    clusterPerimeters[posToClusterIndex[(i,j)]] += 1
            #  right
            if j == w - 1:
                if i == 0 or dat[i-1][j] != dat[i][j]:
                    clusterPerimeters[posToClusterIndex[(i,j)]] += 1
            elif dat[i][j] != dat[i][j+1]:
                if i == 0 or dat[i-1][j] != dat[i][j] or dat[i-1][j+1] == dat[i][j]:
                    clusterPerimeters[posToClusterIndex[(i,j)]] += 1
            # second

        
    print("s",clusterSizes)
    print("p",clusterPerimeters)
    print("c",clusterToChar)
    print(sum(p*clusterSizes[i] for i,p in clusterPerimeters.items()))
            


if __name__ == "__main__":
    main("input.txt")