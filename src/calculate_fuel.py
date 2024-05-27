def calculate_fuel(distance):
    # Припустимо, що витрати палива становлять 10 одиниць палива на 1 одиницю відстані.
    fuel_needed = distance * 10
    return fuel_needed

def test_calculate_fuel1():
    assert calculate_fuel(15) == 150

def test_calculate_fuel2():
    assert calculate_fuel(0) == 0

def test_calculate_fuel3():
    assert calculate_fuel(5) == 50