import numpy as np

data = open("adventofcode2.txt", "r").read()

data1 = data.split("\n")

ay_list = []
bz_list = []
cx_list = []

ax_list = []
by_list = []
cz_list = []

for i in data1:
    if 'A Y' in i:
        ay_list.append(1)
    else:
        ay_list.append(0)
    if 'B Z' in i:
        bz_list.append(1)
    else:
        bz_list.append(0)
    if 'C X' in i:
        cx_list.append(1)
    else:
        cx_list.append(0)
    if 'A X' in i:
        ax_list.append(1)
    else:
        ax_list.append(0)
    if 'B Y' in i:
        by_list.append(1)
    else:
        by_list.append(0)
    if 'C Z' in i:
        cz_list.append(1)
    else:
        cz_list.append(0)
    


total_points = (sum(ay_list)*8 + sum(bz_list)*9 + sum(cx_list)*7 + sum(ax_list)*4 + sum(by_list)*5 + sum(cz_list)*6)


print(total_points)