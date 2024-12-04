
def validate_position(x,y):
    count = 0
    if lines[x][y]=='X':
        candidates = get_all_possibilities(x,y)
        for candidate in candidates:
            if "".join(candidate)=="XMAS":
                count+=1
    return count

def get_all_possibilities(x,y):
    res = []
    if lines[x][y] !="X":
        return res
    for direction in DIRECTIONS:
        try :
            res.append(get_candidate(direction,x,y))
        except (AssertionError, IndexError):
            continue
    return res

def get_candidate(direction,x,y):
    match direction:
        case "N": 
            assert x>2
            return [lines[x][y],lines[x-1][y],lines[x-2][y],lines[x-3][y]]

        case "S": 
            return [lines[x][y],lines[x+1][y],lines[x+2][y],lines[x+3][y]]

        case "E": 
            return [lines[x][y],lines[x][y+1],lines[x][y+2],lines[x][y+3]]

        case "W": 
            assert y>2
            return [lines[x][y],lines[x][y-1],lines[x][y-2],lines[x][y-3]]

        case "SE": 
            return [lines[x][y],lines[x+1][y+1],lines[x+2][y+2],lines[x+3][y+3]]

        case "SW": 
            assert y>2
            return [lines[x][y],lines[x+1][y-1],lines[x+2][y-2],lines[x+3][y-3]]

        case "NE":
            assert x>2
            return [lines[x][y],lines[x-1][y+1],lines[x-2][y+2],lines[x-3][y+3]]

        case "NW": 
            assert x>2
            assert y>2
            return [lines[x][y],lines[x-1][y-1],lines[x-2][y-2],lines[x-3][y-3]]



def main():
    count=0
    n_lines = len(lines) # square
    for x in range(n_lines):
        lines[x] = lines[x].strip()
        for y in range(n_lines):
            count+=validate_position(x,y)
    print(count)

if __name__=="__main__":
    
    with open("input.txt", 'r') as f:
        lines = (f.readlines())
    DIRECTIONS = "N,S,E,W,NE,NW,SE,SW".split(",")

    main()