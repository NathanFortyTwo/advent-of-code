with open("input.txt") as f:
    lines = f.readlines()

def is_safe(numbers):

    if len(numbers) <=1:
        return 1
    if numbers[0]==numbers[1]:
        return 0
    order = "ASC" if numbers[1] > numbers[0] else "DESC" 
    for index,val in enumerate(numbers[:-1]):
        nextval = numbers[index+1]
        diff = nextval-val
        if (order == "ASC" and not (1 <=diff<=3)) or (order == "DESC" and  not (-3<=diff<=-1)):
            #try again here
            return 0
    return 1

def try_remove(numbers):
    c = is_safe(numbers)
    if c:
        return 1
    
    for k in range(len(numbers)):
        new_numbers = numbers[:k] + numbers[k+1:]    
        if is_safe(new_numbers):
            return 1
    return 0

    
s= 0 
for line in lines:
    numbers = [int(elt) for elt in line.split(" ")]
    s+= try_remove(numbers)

print(s)


