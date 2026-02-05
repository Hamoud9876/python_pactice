"""
Problem 4: Group By + Aggregate

Given a list of (key, value) tuples, sum values by key.

sales = [
    ("US", 100),
    ("CA", 200),
    ("US", 50),
    ("CA", 300)
]

Result:
{"US": 150, "CA": 500}
"""

def totals(lst: list)-> dict:
    if not isinstance(lst, list):
        return "you did not input a list"
    if len(lst)==0:
        return "no element in the inputed list"
    total_dict = {}

    for i in lst:
        total_dict[i[0]] = total_dict.get(i[0],0) + i[1]

    return total_dict