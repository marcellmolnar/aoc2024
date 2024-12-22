def mixInto(secret, value):
    return secret ^ value

def prune(secret):
    return secret % 16777216

def eveolve(secret):
    secret = mixInto(secret, secret*64)
    secret = prune(secret)
    secret = mixInto(secret, int(secret/32))
    secret = prune(secret)
    secret = mixInto(secret, secret*2048)
    return prune(secret)

def main(fname):
    with open(fname) as f:
        secrets = [int(x) for x in f.readlines()]

    lastDiffs = [[] for _ in range(len(secrets))]
    firstOccurence = [{} for _ in range(len(secrets))]
    s = {}
    alreadyAdded = {}
    for _ in range(2000):
        for i in range(len(secrets)):
            secret = secrets[i]
            newSecret = eveolve(secret)
            diff = newSecret % 10 - secret % 10
            lastDiffs[i].append(diff)
            if len(lastDiffs[i]) > 4:
                lastDiffs[i].pop(0)
            if len(lastDiffs[i]) == 4 and tuple(lastDiffs[i]) not in firstOccurence[i]:
                firstOccurence[i][tuple(lastDiffs[i])] = newSecret % 10
            if tuple(lastDiffs[i]) not in s:
                s[tuple(lastDiffs[i])] = 0
                alreadyAdded[tuple(lastDiffs[i])] = []
            if i not in alreadyAdded[tuple(lastDiffs[i])]:
                s[tuple(lastDiffs[i])] += newSecret % 10
                alreadyAdded[tuple(lastDiffs[i])].append(i)

            secrets[i] = newSecret

    # first
    print(sum(secrets))
    # second
    print(max(s.items(), key=lambda x: x[1]))

if __name__ == '__main__':
    isTest = False
    main('input_test_2.txt' if isTest else 'input.txt')