import math

def main(fname):
    with open(fname) as f:
        dat = f.readlines()

    h = len(dat)
    tokens = 0
    for i in range(0, h, 4):
        buttonAstr = dat[i][:-1]
        buttonBstr = dat[i+1][:-1]
        prizePosStr = dat[i+2][:-1]

        bax, bay = int(buttonAstr.split(', ')[0][11:]), int(buttonAstr.split(', ')[1][1:])
        bbx, bby = int(buttonBstr.split(', ')[0][11:]), int(buttonBstr.split(', ')[1][1:])
        
        # second with additional value
        px, py = int(prizePosStr.split(', ')[0][9:]) + 10000000000000, int(prizePosStr.split(', ')[1][2:]) + 10000000000000

        # solution for x and y:
        # x = (px - y*bbx) / bax
        # y = (py*bax - px*bay) / (bax*bby - bbx*bay)
        y = (py*bax - px*bay) / (bax*bby - bbx*bay)
        x = (px - y*bbx) / bax
        
        eps = 0.0000001
        if math.fabs(math.floor(x)-x) < eps and math.fabs(math.floor(y)-y) < eps:
            tokens += 3*x + y

    print(int(tokens))


if __name__ == "__main__":
    main("input.txt")