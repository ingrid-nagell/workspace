# decorators basics
# src: https://www.datacamp.com/tutorial/decorators-python

# writing decorators:
def split_string(function): # takes a function as arg
    def wrapper(): # keep modifying code inside wrapper
        func = function() # wrapper func inherit arg-param from parent
        splitted_string = func.split()
        return splitted_string # wrapper must do something? why?

    return wrapper # return the wrapper function

def uppercase_decorator(function):
    def wrapper(arg1):
        func = function(arg1)
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


@split_string
@uppercase_decorator
def say_hi():
    return 'hello world'

print(say_hi)

# decorator with arguments:
# if function we want to wrap takes args, the decorator must also
def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2): # args are kept within the wrapper func
        print("My arguments are: {0}, {1}".format(arg1,arg2))
        function(arg1, arg2) # instead of return, call function with args
    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities I love are {0} and {1}".format(city_one, city_two))

cities("Nairobi", "Accra")

# Change the uppercase decorator to handle arg:
def uppercase_decorator2(function):
    def wrapper(arg1):
        func = function(arg1)
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

@uppercase_decorator2
def say_hi2(w):
    return 'hello world' + w

print(say_hi2(" Yooo"))


# Defining General Purpose Decorators
# if function we want to wrap takes args, the decorator must also -> to be able to handle any args: *args, **kwargs
def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args,**kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function_to_decorate(*args)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("No arguments here.")

@a_decorator_passing_arbitrary_arguments
def function_with_two_argument(x, y):
    print(x + " " + y)

function_with_no_argument()

function_with_two_argument("hello", "world")