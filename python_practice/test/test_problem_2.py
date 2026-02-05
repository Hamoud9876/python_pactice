from src.problem_2 import revoming_dupes


def test_handles_wrong_input():
    response = revoming_dupes({})
    
    assert response == "wrong input type"

    response = revoming_dupes([])
    
    assert response == "no element in the list"

def test_return_list():
    response = revoming_dupes([
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 1, "name": "Alice"}
])
    
    assert isinstance(response, list)

def test_finds_one_dupe():
    response = revoming_dupes([
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 1, "name": "Alice"}
])
    
    assert len(response) == 2

def test_remove_all_dupes():
    response = revoming_dupes([
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 1, "name": "Alice"},
    {"id": 1, "name": "Alice"},
    {"id": 1, "name": "Alice"},
    {"id": 1, "name": "Alice"},
    {"id": 1, "name": "Alice"},
    {"id": 1, "name": "Alice"},
    {"id": 1, "name": "Alice"},
])
    
    assert len(response) == 2


def test_remove_any_dupe():
    response = revoming_dupes([
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 1, "name": "Alice"},
    {"id": 1, "name": "Alice"},
    {"id": 1, "name": "Alice"},
    {"id": 1, "name": "Alice"},
    {"id": 1, "name": "Alice"},
    {"id": 1, "name": "Alice"},
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 2, "name": "Bob"},
    {"id": 2, "name": "Bob"},
    {"id": 2, "name": "Bob"},
    {"id": 2, "name": "Bob"},
    {"id": 2, "name": "Bob"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Hamoud"},
    {"id": 3, "name": "Hamoud"},
    {"id": 3, "name": "Hamoud"},
    {"id": 3, "name": "Hamoud"},
    {"id": 3, "name": "Hamoud"}
])
    

    assert len(response) == 3

