def decorator(func):
    def wrapper():
        print('Allo m8!')
        func()
        print("G'bye m8!")
    return wrapper

@decorator
def stand_alone_function():
    print('This function is UNTOUCHABLE.')   

@decorator
def do_something(theNumberEight = '8'):
    print(theNumberEight)
    

do_something()
stand_alone_function()