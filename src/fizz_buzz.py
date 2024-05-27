def fizz_buzz(param):
    if param % 3 == 0 and param % 5 != 0:
        return "Fizz"
    elif param % 3 != 0 and param % 5 == 0:
        return "Buzz"
    elif param % 3 == 0 and param % 5 == 0:
        return "FizzBuzz"
    else:
        return str(param)