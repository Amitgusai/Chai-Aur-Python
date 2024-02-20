# ...................................................               API handling            ................................................






def main(func):
    def wrapper():
        return func()
    return wrapper


def func():
    pass

demo = func()


























