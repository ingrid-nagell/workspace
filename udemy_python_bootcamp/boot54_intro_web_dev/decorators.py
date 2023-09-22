import time

def delay_decorator(function):
    def wrapper():
        time.sleep(2)
        function()
    return wrapper

def hello():
    print("hello")

@delay_decorator
def bye():
    print("bye")

def adios():
    print("adios")


hello()
bye()

delayed_adios = delay_decorator(adios)
delayed_adios()