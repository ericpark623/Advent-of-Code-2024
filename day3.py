import pandas as pd
import re

with open('/Users/ericpark/Downloads/day3.txt', 'r') as file:
    exp = file.read()

def day3_pt1(exp):
    lst = re.findall(r"mul\(\d+\,\d+\)",exp)
    overall_sum = 0
    new_lst = [list(map(int,i[4:-1].split(','))) for i in lst]
    return sum([j[0]*j[1] for j in new_lst])

day3_pt1(exp)

def day3_pt2(exp):
    lst = re.findall(r"mul\(\d+\,\d+\)|do\(\)|don't\(\)",exp)
    do = True
    enabled_m = []
    for i in lst:
        if i == "don't()":
            do = False
        elif i == "do()":
            do = True
        else:
            if do == True:
                enabled_m.append(i)
    new_lst = [list(map(int,i[4:-1].split(','))) for i in enabled_m]
    return sum([j[0]*j[1] for j in new_lst])

day3_pt2(exp)
