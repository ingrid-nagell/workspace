import time


def speed_calc_decorator(function):
    def wrapper():
        start_time = time.time()
        function()
        end_time = time.time()
        run_time = end_time - start_time
        print(f"{function.__name__} run time: ", run_time)
    return wrapper

@speed_calc_decorator
def slow_function():
    time.sleep(2)
    print("slooooow")

@speed_calc_decorator
def fast_function():
    time.sleep(1)
    print("fast!")

slow_function()
fast_function()