"""
Problem 3: Rolling Average

Given a list of integers and a window size k,
return a list of rolling averages.

nums = [1, 3, 5, 7, 9]
k = 3
Result: [3.0, 5.0, 7.0]

Do not use NumPy.
"""


def rolling_average(lst:list, key: int) -> list:
    if not isinstance(lst, list):
        return "you did not input a list"
    if len(lst)==0:
        return "no element in the inputed list"
    if not isinstance(key, int):
        return "invalid input for a key"
    
    avg_lst = []
    temp_lst = []
    for i in range(len(lst)):
        if i+key <= len(lst):
            temp_lst = lst[i:i+key]
            avg_lst.append(sum(temp_lst)/len(temp_lst))

    
    return avg_lst