from src.iterators1.fibonacci import fib

def test_fibonacci_function_returns_first_item():
    fib_gen = fib()
    assert next(fib_gen) == 1
