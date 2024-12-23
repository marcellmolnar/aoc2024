def first(connMap):
    print("first")
    matchingCircles = []
    for i, iNodes in connMap.items():
        for j in iNodes:
            for k in connMap[j]:
                if i in connMap[k]:
                    if any(a.startswith('t') for a in (i,j,k)):
                        ni,nj,nk = sorted([i,j,k])
                        if (ni,nj,nk) not in matchingCircles:
                            matchingCircles.append((ni,nj,nk))
    print(len(matchingCircles))

def second(connections):
    print("second")
    allMembers = set(connections.keys())

    checkedSets = []
    biggest = [0]
    def dfs(rootNode, node, group, biggestGroup):
        for n in connections[node]:
            if n == rootNode and len(group) > 1:
                if len(group) > len(biggestGroup):
                    if len(biggestGroup) > biggest[0]:
                        print(f"found circle {len(group)} {','.join(sorted(biggestGroup))}")
                        biggest[0] = len(biggestGroup)
                    biggestGroup.clear()
                    biggestGroup.update(group)
                continue
            if n not in group and all(n in connections[m] for m in group):
                newGroup = group.copy()
                newGroup.add(n)
                newGroup = set(sorted(newGroup))
                if newGroup not in checkedSets:
                    biggestWithN = dfs(rootNode, n, newGroup, biggestGroup)
                    checkedSets.append(newGroup)
                    if len(biggestWithN) > len(biggestGroup):
                        biggestGroup.clear()
                        biggestGroup.update(biggestWithN)
        return biggestGroup

    biggestGroup = set()
    id = 0
    for i in allMembers:
        print(f"{id}/{len(allMembers)}")
        id += 1
        biggestGroupWithI = dfs(i, i, set([i]), set([i]))
        if len(biggestGroupWithI) > len(biggestGroup):
            biggestGroup.clear()
            biggestGroup.update(biggestGroupWithI)

    print(len(biggestGroup))
    print(",".join(sorted(biggestGroup)))
    return

def main(fname):
    with open(fname) as f:
        dat = f.readlines()

    connections = [line.strip().split('-') for line in dat]
    connMap = {}
    for conn in connections:
        a,b = conn
        connMap[a] = connMap.get(a, []) + [b]
        connMap[b] = connMap.get(b, []) + [a]
    
    first(connMap)
    second(connMap)

if __name__ == '__main__':
    isTest = False
    main('input_test.txt' if isTest else 'input.txt')