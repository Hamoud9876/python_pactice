from src.problem_4 import totals

def test_handles_wrong_input():
    response = totals({})
    
    assert response == "you did not input a list"

    response = totals([])
    
    assert response == "no element in the inputed list"


def test_return_dict():
    response = totals([
    ("US", 100),
    ("CA", 200),
    ("US", 50),
    ("CA", 300)
])
    
    assert isinstance(response, dict)


def test_calculate_one_total():
    response = totals([
    ("US", 100),
    ("CA", 200),
    ("US", 50),
    ("CA", 300)
])
    
    assert response["US"] == 150


def test_return_all_totals():
    response = totals([
    ("US", 100),
    ("CA", 200),
    ("US", 50),
    ("CA", 300)
])
    
    assert response["US"] == 150
    assert response["CA"] == 500
