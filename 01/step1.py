

def prepare_lists():
    L1, L2 = [], []
    for line in lines:
        x, y=line.split(DELIMITER)
        L1.append(int(x))
        L2.append(int(y))
    L1.sort()
    L2.sort()
    return L1,L2
    
def compare_lists(L1,L2):
    count = 0
    for k in range(len(L1)):
        count+= abs(L1[k] -  L2[k])
    return count

def main():
    print(compare_lists(prepare_lists()))

if __name__=="__main__":
    with open("input.txt", 'r') as f:
        lines = f.readlines()

    DELIMITER = "   "
    main()