import numpy as np

def main():
    fname = "input.txt"
    # read file line by line
    
    with open(fname) as f:
        dat = f.readlines()
    
    # first
    mustBeAfter = {}
    secondPart = False
    m = 0
    okC = 0
    nokC = 0
    mWrongs = 0
    stillWrong = 0
    for l in range(len(dat)):
        if dat[l] == "\n":
            secondPart = True
            continue
        if not secondPart:
            d = dat[l][:-1].split("|")
            if int(d[1]) not in mustBeAfter.keys():
                mustBeAfter[int(d[1])] = []
            mustBeAfter[int(d[1])].append(int(d[0]))
        else:
            d = dat[l][:-1].split(",")
            seen = []
            nok = False
            for i in range(len(d)):
                n = int(d[i])
                if any([n in mustBeAfter[s] for s in seen]):
                    nok = True
                    nokC += 1
                    break
                seen.append(n)
                if i == (len(d))//2:
                    mid = n
            if not nok:
                okC += 1
                m += mid
            # second
            else:
                print(l, d)
                newL = [int(d[0])]
                for i in range(1,len(d)):
                    n = int(d[i])
                    shouldBeAfterThese = [x for x in newL if x in mustBeAfter[n]] if n in mustBeAfter.keys() else []
                    shouldBeAfterTheseIndex = [newL.index(x) for x in shouldBeAfterThese if x in newL]
                    shouldBeAfter = max(shouldBeAfterTheseIndex) if len(shouldBeAfterTheseIndex) > 0 else -1
                    newL.insert(shouldBeAfter+1, n)
                print(newL, newL[len(d)//2])
                mWrongs += newL[len(d)//2]
                seen = []
                nok = False
                for i in range(len(newL)):
                    n = int(newL[i])
                    if any([n in mustBeAfter[s] for s in seen]):
                        stillWrong += 1
                        break
                    seen.append(n)

    print(m)
    print(mWrongs)
    print(stillWrong)
                    

if __name__ == "__main__":
    main()