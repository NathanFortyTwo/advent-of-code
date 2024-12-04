
import re

with open("input.txt", 'r') as f:
    str = f.read()

pattern = r"mul\(\d{1,3},\d{1,3}\)"
matches = re.findall(pattern, str)
s = 0
for match in matches:
    x,y = match.split("(")[1][:-1].split(",")
    x = int(x)
    y = int(y)
    s +=x*y

print(s)