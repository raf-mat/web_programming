# One thing made possible by functional programming is the idea of a decorator, which is a higher-order function that can modify another function. 
# For example, let’s write a decorator that announces when a function is about to begin, and when it ends. We can then apply this decorator using an @ symbol.
def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper

@announce
def hello():
    print("hello, world !")

hello()