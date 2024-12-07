import numpy as np

def main():
    fname = "input.txt"
    # read file line by line
    
    with open(fname) as f:
        dat = f.readlines()
    
    def checkIfSafe(diff):
        return (all(d > 0 for d in diff) or all(d < 0 for d in diff)) and all(abs(d) <= 3 for d in diff)

    # first
    safe = 0
    for l in range(len(dat)):
        d = dat[l].split()
        diff = [int(a)-int(b) for (a,b) in zip(d[0:len(d)-1], d[1:len(d)])]
        if checkIfSafe(diff):
            safe += 1
        else: # second
            for toRem in range(len(d)):
                newD = d.copy()
                del newD[toRem]
                diff = [int(a)-int(b) for (a,b) in zip(newD[0:len(d)-1], newD[1:len(d)])]
                if checkIfSafe(diff):
                    print(newD)
                    safe += 1
                    break

    print(safe)

if __name__ == "__main__":
    main()