import pytest

car_type = input("Mini\nSedan\nPrime\nEnter your Choice: ")
car_type = car_type.upper()

def test_car_type():
    if car_type == 'MINI':
        assert True
    elif car_type == 'SEDAN':
        assert True
    elif car_type == 'PRIME':
        assert True
    else:
        assert False