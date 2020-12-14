def my_decorator(func):

    def wrap_func():
        import time
        text = time.time()
        ret = func()
        text2 =time.time()
        A = text2-text
        print(A)
        return ret

    return wrap_func

@my_decorator
def my_func():
    print("Hello World! Do my Job!")


if __name__ == "__main__":
    my_func()

