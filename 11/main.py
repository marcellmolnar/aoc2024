import math

def blinkFor(dat, n):
    for nn in range(n):
        newDat = {}
        for i in dat.keys():
            a = math.floor(math.log10(i)) if i > 9 else 0
            if i == 0:
                if 1 not in newDat.keys():
                    newDat[1] = 0
                newDat[1] += dat[i]
            elif i > 9 and a % 2 == 1:
                x = int(i % math.pow(10, (a+1)/2))
                if x not in newDat.keys():
                    newDat[x] = 0
                newDat[x] += dat[i]

                y = math.floor(i / math.pow(10, (a+1)/2))
                if y not in newDat.keys():
                    newDat[y] = 0
                newDat[y] += dat[i]
            else:
                newDat[i* 2024] = dat[i]
        dat = newDat
        print(dat)
        print(nn,sum(dat.values()))

def main(fname):
    with open(fname) as f:
        dat = {int(a):1 for a in f.read().split()}

    print(dat)
    # first with 25, second with 75
    blinkFor(dat, 75)


if __name__ == "__main__":
    main("input.txt")