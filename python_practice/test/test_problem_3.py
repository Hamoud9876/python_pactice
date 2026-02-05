from src.problem_3 import rolling_average

def test_handles_wrong_input():
    response = rolling_average({},1)
    
    assert response == "you did not input a list"

    response = rolling_average([],1)
    
    assert response == "no element in the inputed list"
    
    response = rolling_average([1, 3, 5, 7, 9],"int")

    assert response == "invalid input for a key"





def test_return_list():
    response = rolling_average([1, 3, 5, 7, 9],3)
    
    assert isinstance(response, list)


def test_return_one_average():
    response = rolling_average([1, 3, 5, 7, 9],3)

    assert response[0] == 3.0

def test_does_not_exceed_range():
    response = rolling_average([1, 3, 5, 7, 9],6)

    assert len(response) == 0

def test_calculate_all_avg():
    response = rolling_average([1, 3, 5, 7, 9],3)

    assert response[0] == 3.0
    assert response[1] == 5.0
    assert response[2] == 7.0
