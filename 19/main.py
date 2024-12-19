
def main(fname):
    with open(fname) as f:
        dat = f.readlines()

    patterns = dat[0].split(', ')
    patterns[-1] = patterns[-1][:-1]
    print(patterns)

    designs = []
    for i in range(2, len(dat)):
        designs.append(dat[i][:-1])
    print(designs)

    def solveWithPatterns(design, solutionCount, s):
        if design == '':
            return 1
        # soluionCount keeps track of already solved length, thus reducing the computation demand
        if len(design) in solutionCount:
            return solutionCount[len(design)]
        solutionsFromHere = 0
        for p in patterns:
            if design.startswith(p):
                solutionsFromHere += (1 if s==0 else s) * solveWithPatterns(design[len(p):], solutionCount, s)                    
        solutionCount[len(design)] = solutionsFromHere

        return solutionsFromHere
    
    s = 0
    for d in designs:
        solutions = solveWithPatterns(d, {}, 0)
        # first task is to only count solvable designs, second is to count all possible solutions
        s+= solutions
    print(s)

if __name__ == '__main__':
    isTest = False
    main('input_test.txt' if isTest else 'input.txt')