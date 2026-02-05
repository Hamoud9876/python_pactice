
"""
Problem 2: Deduplicate Records by Key

Given a list of dictionaries representing records,
remove duplicates based on 'id', keeping the first occurrence.

records = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 1, "name": "Alice"}
]
"""
from copy import deepcopy


def revoming_dupes(lst: list)->list:
    if not isinstance(lst, list):
        return "wrong input type"
    if len(lst)==0:
        return "no element in the list"
    
    seen = []
    clean_lst = []
    my_list = deepcopy(lst)

    for row in my_list:
        if row["id"] not in seen:
            clean_lst.append(row)
            seen.append(row["id"])



    return clean_lst