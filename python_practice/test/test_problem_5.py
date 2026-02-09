from src.problem_5 import validating_data


def test_handles_wrong_input():
    response = validating_data({})
    
    assert response == "you did not input a list"

    response = validating_data([])
    
    assert response == "no element in the provided list"

def test_returns_list():
    my_input = [ 
 {"id": 1, "email": "a@example.com", "age": 30}, 
 {"id": None, "email": "b@example.com", "age": -5} 
 ]
    response = validating_data(my_input)
    
    assert isinstance(response, list)
    assert isinstance(response[0], dict)

def test_fuct_immutability():
    my_input = [ 
 {"id": 1, "email": "a@example.com", "age": 30}, 
 {"id": None, "email": "b@example.com", "age": -5} 
 ]
    response = validating_data(my_input)

    assert my_input is not response

def test_removes_null_ids():
    my_input = [ 
 {"id": 1, "email": "a@example.com", "age": 30}, 
 {"id": None, "email": "b@example.com", "age": 2}, 
 {"id": 2, "email": "b@example.com", "age": 4}, 
 {"id": None, "email": "b@example.com", "age": 7}, 
 {"id": 3, "email": "b@example.com", "age": 9}, 
 ]
    response = validating_data(my_input)

    assert len(response) ==2

def test_removes_wrong_emails():
    my_input = [ 
 {"id": 1, "email": "a@example.com", "age": 30}, 
 {"id": 4, "email": "b@example.com", "age": 2}, 
 {"id": 2, "email": "c@example.com", "age": 2}, 
 {"id": 5, "email": "fexample.com", "age": 2}, 
 {"id": 3, "email": "eexample.com", "age": 2}, 
 ]
    
    response = validating_data(my_input)

    assert len(response) == 2


def test_remves_invalid_age():
    my_input = [ 
 {"id": 1, "email": "a@example.com", "age": 30}, 
 {"id": 4, "email": "b@example.com", "age": -9}, 
 {"id": 2, "email": "c@example.com", "age": -10}, 
 {"id": 5, "email": "f@example.com", "age": -2}, 
 {"id": 3, "email": "e@example.com", "age": 2}, 
 ]
    
    response = validating_data(my_input)

    assert len(response) == 3

def test_removes_all_invalid_rows():
    my_input = [ 
 {"id": 1, "email": "a@example.com", "age": 30}, 
 {"id": None, "email": "b@example.com", "age": 2}, 
 {"id": 2, "email": "c@example.com", "age": -10}, 
 {"id": 5, "email": "f@example.com", "age": 9}, 
 {"id": 3, "email": "eexample.com", "age": 2}, 
 ]
    
    response = validating_data(my_input)

    assert len(response) == 3
    