from src.generators.fibonacci import fib

def test_fibonacci_function_returns_first_item():
    fib_gen = fib(1)
    assert next(fib_gen) == 1
