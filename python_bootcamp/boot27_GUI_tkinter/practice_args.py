# *args

def add(*args):
    print(args[3]) # Args collect all arguments in a tuple, thus we can access arguments provided by index.
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(2,3,5,7,1,2))

def calculate(n, **kwargs): # Create a dictionary
    print(kwargs)
    n += kwargs.get("add")
    n *= kwargs.get("multiply") # .get() -> if key does not exist, it returns None
    return n

calculate(2, add = 3)