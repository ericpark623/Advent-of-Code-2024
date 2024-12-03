import pandas as pd
df = pd.read_csv('/Users/ericpark/Downloads/day1.txt', delim_whitespace = True, header = None)

def day1_pt1(x):
    overall_dist = 0
    lst1 = x[0].to_list()
    lst2 = x[1].to_list()
    
    while len(lst1) > 0:
        
        min_lst1 = min(lst1)
        min_lst2 = min(lst2)
        overall_dist += abs(min_lst1 - min_lst2)
        lst1.remove(min_lst1)
        lst2.remove(min_lst2)
    return overall_dist  

day1_pt1(df)

def day1_pt2(x):
    new_df = x[[0]].merge(pd.DataFrame(x[1].value_counts().reset_index()),left_on = 0, right_on = 1, how = 'left').fillna(0)
    return sum(new_df[0]*new_df['count'])

day1_pt2(df)

