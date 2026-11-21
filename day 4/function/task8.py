def require_positive(func):
    def wrapper(a, b):

        if a <= 0 or b <= 0:
            print("Error: Numbers must be positive")
        else:
            return func(a, b)

    return wrapper


@require_positive
def divide(a, b):
    return a / b


print(divide(10, 2))
divide(-10, 2)