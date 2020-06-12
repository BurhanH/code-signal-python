# https://app.codesignal.com/arcade/intro/level-1/jwr339Kq6e3LQTsfa
# Write a function that returns the sum of two numbers.

def add(param1:int = 0 , param2: int = 0) -> int:
    if -1000 <= param1 and param1 <= 1000:
        if -1000 <= param2 and param2 <= 1000:
            return param1 + param2
    return 0
