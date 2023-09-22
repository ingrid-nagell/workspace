
def logger(function):
    def wrapper(*args):
        print("Function name: ", function.__name__)
        for arg in args:
            print(arg)
        print(function(*args))
    return wrapper

@logger
def print_world(planet, solarsystem):
    return f"{planet} is in solarsystem {solarsystem}"

result = print_world("Earth", "Milkeyway")
print(result)