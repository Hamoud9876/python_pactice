from src.problem_1 import fidning_errors
import pytest
from random import randint, choice

@pytest.fixture(scope="function")
def create_data():
    rows = []
    for i in range(randint(1,50)):
        rows.append(f"2024-01-15 12:03:22,${choice(["ERROR","INFO","WARN"])},User not found")

    return rows

def test_handles_wrong_input():
    response = fidning_errors({})

    assert response == "wrong input type"

def test_return_dict():
    response = fidning_errors(["2024-01-15 12:03:22,ERROR,User not found"])

    assert isinstance(response, dict) 

def test_count_one_error():
    response = fidning_errors(["2024-01-15 12:03:22,ERROR,User not found"])

    assert response["ERROR"] == 1

    response = fidning_errors(["2024-01-15 12:03:22,INFO,User not found"])

    assert response["INFO"] == 1

def test_count_multiple_errors():
    response = fidning_errors(["2024-01-15 12:03:22,ERROR,User not found",
                               "2024-01-15 12:03:22,ERROR,User not found",
                               "2024-01-15 12:03:22,ERROR,User not found"])

    assert response["ERROR"] == 3

def test_count_multiple_errors():
    lst = ["2024-01-15 12:03:22,INFO,User not found",
            "2024-01-15 12:03:22,ERROR,User not found",
            "2024-01-15 12:03:22,INFO,User not found",
            "2024-01-15 12:03:22,ERROR,User not found",
            "2024-01-15 12:03:22,ERROR,User not found",
            "2024-01-15 12:03:22,WARN,User not found",
            "2024-01-15 12:03:22,WARN,User not found"]
    response =  fidning_errors(lst)

    assert response["ERROR"] == 3
    assert response["INFO"] == 2
    assert response["WARN"] == 2


    