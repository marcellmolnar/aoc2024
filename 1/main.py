import numpy as np

def main():
    fname = "input.txt"
    # read file line by line
    
    d = np.loadtxt(fname, delimiter=' ', dtype=np.int32)
    
    d1= d[:,0].copy()
    d2= d[:,1].copy()

    # first
    d1 = np.sort(d1)
    d2 = np.sort(d2)

    print(np.sum(np.abs(d2-d1)))
    print(d1.min(), d2.min(), d1.max(), d2.max())

    # second
    sim = 0
    for n in d1:
        sim += np.sum((n-d2)==0)*n
    print(sim)

    # new list
    

if __name__ == "__main__":
    main()