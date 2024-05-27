def calculate_fuel(distance):
    # Якщо мінімальна кількість палива повинна бути 100
    return max(distance * 10, 100)