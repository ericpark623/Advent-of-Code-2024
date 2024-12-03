import pandas as pd

df = pd.read_csv('/Users/ericpark/Downloads/day2.txt', header = None)
df2 = df[0].apply(lambda x: [int(ele) for ele in x.split()])

def rule1(lst):
    if lst == sorted(lst, reverse = False):
        return True
    elif lst == sorted(lst, reverse = True):
        return True
    else:
        return False

def rule2(lst):
    for i in range(len(lst)-1):
        if (abs(lst[i]-(lst[i+1]))>=1) and (abs(lst[i]-(lst[i+1]))<=3):
            continue
        else:
            return False
    return True

def day2_pt1(x):
    safe_count = 0

    for row in x:
        if rule1(row) and rule2(row):
            safe_count += 1
        else:
            continue
    return safe_count

day2_pt1(df2)

def day2_pt2(x):
    safe_count = 0
    for row in x:
        if rule1(row) and rule2(row):
            safe_count += 1
        else:
            for i in range(len(row)):
                new_r = row[:i]+row[i+1:]
                if rule1(new_r) and rule2(new_r):
                    safe_count +=1
                    break
    return safe_count

day2_pt2(df2)
