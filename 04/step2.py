def get_candidate(x,y):
    if not x>=1 or not y>=1:
        return [],[]
    return ([lines[x-1][y-1],lines[x][y],lines[x+1][y+1]], 
            [lines[x-1][y+1],lines[x][y],lines[x+1][y-1]])

def validate_position(x,y):
    if lines[x][y]!='A':
        return 0
    try:
        candidate1, candidate2 = get_candidate(x,y)
    except (IndexError):
        return 0
    if candidate2 in TARGETS and candidate1 in TARGETS :
        return 1
    return 0

def main():
    count = 0
    n_lines = len(lines)
    for x in range(n_lines):
        lines[x] = lines[x].strip()
        for y in range(n_lines):
            count+= validate_position(x,y)
    print(count)

if __name__ == "__main__":

    with open("input.txt", 'r') as f:
        lines = (f.readlines())

    TARGETS = [["M","A","S"],["S","A","M"]]
    main()
