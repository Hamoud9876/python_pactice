"""
Problem 1: Log Line Parser

You’re given log lines like:
"2024-01-15 12:03:22,ERROR,User not found"

Write a function that:
- Takes a list of log lines
- Returns a dictionary counting how many times each log level appears

Example output:
{"ERROR": 5, "INFO": 12, "WARN": 3}
"""

def fidning_errors(lst: list)-> dict:
    if not isinstance(lst, list):
        return "wrong input type"
    if len(lst)==0:
        return "no element in the list"
    
    my_dict = {}

    my_input_cp = lst
    for i in range(len(my_input_cp)):
        split_string = my_input_cp[i].split(",")
    
        error_type = split_string[1]
        my_dict[error_type] = my_dict.get(error_type, 0) +1

    return my_dict


