from PIL import Image

class Robot:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def __str__(self):
        return f"({self.x}, {self.y}) -> ({self.vx}, {self.vy})"
    
    def step(self, h, w):
        self.x += self.vx
        self.x %= w
        self.y += self.vy
        self.y %= h

def main(fname, h, w):
    assert h % 2 == 1
    assert w % 2 == 1
    with open(fname) as f:
        dat = f.readlines()

    robots = []
    for l in dat:
        posStr, veloStr = l.split(' ')
        posX, posY = int(posStr[2:].split(',')[0]), int(posStr.split(',')[1])
        veloX, veloY = int(veloStr[2:].split(',')[0]), int(veloStr.split(',')[1])
        robots.append(Robot(posX, posY, veloX, veloY))

    s = 0
    for i in range(100):
        for r in robots:
            r.step(h, w)
        s += 1

    q = [0,0,0,0]
    for r in robots:
        if r.x == w//2 or r.y == h//2:
            continue
        idx = 2*int((r.y)/(int(h/2)+1))+int((r.x)/(int(w/2)+1))
        q[idx] += 1
    print(q[0]*q[1]*q[2]*q[3])

    for i in range(10000):
        for r in robots:
            r.step(h, w)

        # these numbers come from manually checking the output
        # since periodically weird horizontal and vertical lines appear
        if ((s-114) % w == 0 or (s - 178) % h == 0):
            im = Image.new('L', (w, h))
            pix = im.load()
            for y in range(h):
                for x in range(w):
                    pix[x, y] = 0
            for r in robots:
                pix[r.x, r.y] = 255
            im = im.resize((w * 10, h * 10), resample=Image.NEAREST)
            im.save(f"outs/output_{s}.png")
        s += 1


if __name__ == "__main__":
    useTest = False
    main("input_test.txt" if useTest else "input.txt", 7 if useTest else 103, 11 if useTest else 101)