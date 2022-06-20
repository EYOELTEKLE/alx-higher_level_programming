def safe_print_division(a, b):
    try:
        answer = a / b
    except (ArithmeticError, TypeError):
        answer = None
    finally:
        print("Inside result: {}".format(answer))
    return answer
