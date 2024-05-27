def fizz_buzz(param):
    if param % 3 == 0 and param % 5 == 0:
        return "fizzbuzz"
    elif param % 3 == 0:
        return "fizz"
    elif param % 5 == 0:
        return "buzz"
    else:
        return param