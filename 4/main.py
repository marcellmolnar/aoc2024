import numpy as np

def main():
    fname = "input.txt"
    # read file line by line
    
    with open(fname) as f:
        dat = f.readlines()
    
    h = len(dat)
    w = len(dat[0])-1 # breakline character

    # first
    mask = np.zeros(h*w).reshape(h,w)
    s = 0
    for y in range(h):
        for x in range(w):
            if dat[y][x] == 'X':
                # horizontal forward
                if x + 3 < w:
                    if dat[y][x+1] == 'M' and dat[y][x+2] == 'A' and dat[y][x+3] == 'S':
                        mask[y,x:x+4] += 1
                        s += 1
                # horizontal backward
                if 0 <= x - 3:
                    if dat[y][x-1] == 'M' and dat[y][x-2] == 'A' and dat[y][x-3] == 'S':
                        mask[y,x-3:x+1] += 1
                        s += 1
                # vertical forward
                if y + 3 < h:
                    if dat[y+1][x] == 'M' and dat[y+2][x] == 'A' and dat[y+3][x] == 'S':
                        mask[y:y+4,x] += 1
                        s += 1
                # vertical backward
                if 0 <= y - 3:
                    if dat[y-1][x] == 'M' and dat[y-2][x] == 'A' and dat[y-3][x] == 'S':
                        mask[y-3:y+1,x] += 1
                        s += 1
                # diagonal upforward
                if  x + 3 < w and 0 <= y - 3:
                    if dat[y-1][x+1] == 'M' and dat[y-2][x+2] == 'A' and dat[y-3][x+3] == 'S':
                        mask[y,x] += 1
                        mask[y-1,x+1] += 1
                        mask[y-2,x+2] += 1
                        mask[y-3,x+3] += 1
                        s += 1
                # diagonal downforward
                if  x + 3 < w and y + 3 < h:
                    if dat[y+1][x+1] == 'M' and dat[y+2][x+2] == 'A' and dat[y+3][x+3] == 'S':
                        mask[y,x] += 1
                        mask[y+1,x+1] += 1
                        mask[y+2,x+2] += 1
                        mask[y+3,x+3] += 1
                        s += 1
                # diagonal upbackward
                if 0 <= x - 3 and 0 <= y - 3:
                    if dat[y-1][x-1] == 'M' and dat[y-2][x-2] == 'A' and dat[y-3][x-3] == 'S':
                        mask[y,x] += 1
                        mask[y-1,x-1] += 1
                        mask[y-2,x-2] += 1
                        mask[y-3,x-3] += 1
                        s += 1
                # diagonal downbackward
                if 0 <= x - 3 and y + 3 < h:
                    if dat[y+1][x-1] == 'M' and dat[y+2][x-2] == 'A' and dat[y+3][x-3] == 'S':
                        mask[y,x] += 1
                        mask[y+1,x-1] += 1
                        mask[y+2,x-2] += 1
                        mask[y+3,x-3] += 1
                        s += 1
    print(s, np.sum(mask)/4)


    # second
    s = 0
    for y in range(1,h-1,1):
        for x in range(1,w-1,1):
            if dat[y][x] == 'A':
                # top M
                if dat[y-1][x-1] == 'M' and dat[y-1][x+1] == 'M' and \
                    dat[y+1][x-1] == 'S' and dat[y+1][x+1] == 'S':
                    s += 1
                # bottom M
                if dat[y+1][x-1] == 'M' and dat[y+1][x+1] == 'M' and \
                    dat[y-1][x-1] == 'S' and dat[y-1][x+1] == 'S':
                    s += 1
                # left M
                if dat[y-1][x-1] == 'M' and dat[y+1][x-1] == 'M' and \
                    dat[y-1][x+1] == 'S' and dat[y+1][x+1] == 'S':
                    s += 1
                # right M
                if dat[y-1][x+1] == 'M' and dat[y+1][x+1] == 'M' and \
                    dat[y-1][x-1] == 'S' and dat[y+1][x-1] == 'S':
                    s += 1
    print(s)


if __name__ == "__main__":
    main()