import math
line = ""
li = []

try:
    while True:
        line += input()+" "
except EOFError:
    li = line.split()
    ln=len(li)-1
    while ln >=0:
        number=math.sqrt(int(li[ln]))
        formatted_number = "{:.4f}".format(number)
        print(formatted_number)
        ln=ln-1;
    
