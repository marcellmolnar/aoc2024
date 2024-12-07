import re

def main():
    fname = "input.txt"
    # read file line by line
    
    with open(fname) as f:
        dat = f.readlines()

    # first
    s = 0
    enabled = True
    for l in dat:
        a = re.findall("(mul\([0-9]{1,3},[0-9]{1,3}\))|(do\(\))|(don't\(\))", l)
        for aa in a:
            if aa[1] == "do()":
                print("enabled")
                enabled = True
            elif aa[2] == "don't()":
                enabled = False
                print("disabled")
            elif enabled:
                print(aa[0])
                aaa = re.findall("[0-9]{1,3}", aa[0])
                s += int(aaa[0])*int(aaa[1])
    print(s)

if __name__ == "__main__":
    main()