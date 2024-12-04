import re

with open("input.txt", 'r') as f:
    str = f.read()

pattern = r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))"
matches = re.findall(pattern, str)
s = 0
on = True
for match in matches:
    if match=="do()":
        on = True
        continue
    if match=="don't()":
        on = False
        continue
    if on:
        x,y = match.split("(")[1][:-1].split(",")
        x = int(x)
        y = int(y)
        s +=x*y

print(s)