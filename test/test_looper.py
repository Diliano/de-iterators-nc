from src.iterators.looper import Looper
import pytest

def test_looper_is_an_iterator():
    assert hasattr(Looper, "__next__")

def test_stores_given_iterable_as_a_collection_iterator_property():
    loop = Looper([1, 2, 3])
    assert hasattr(loop.collection_iterator, "__next__")

def test_raises_value_error_exception_if_given_empty_iterable():
    with pytest.raises(ValueError) as excinfo:
        Looper([])
    assert str(excinfo.value) == "Provided argument must not be empty"

def test_raises_type_error_exception_if_given_non_iterable():
    with pytest.raises(TypeError) as excinfo:
        Looper(2)
    assert str(excinfo.value) == "Provided argument must be iterable"

def test_iter_method_returns_self():
    loop = Looper([1, 2, 3])
    assert iter(loop) is loop

def test_next_method_returns_next_element():
    loop = Looper([1, 2, 3])
    assert next(loop) == 1

def test_next_method_handles_multiple_invocations():
    loop = Looper([1, 2, 3])
    assert next(loop) == 1
    assert next(loop) == 2
    assert next(loop) == 3

def test_next_method_loops_back_to_start_once_collection_has_been_iterated_through():
    loop = Looper([1, 2, 3])
    assert next(loop) == 1
    assert next(loop) == 2
    assert next(loop) == 3
    assert next(loop) == 1
    assert next(loop) == 2
    assert next(loop) == 3
    assert next(loop) == 1
    assert next(loop) == 2
    assert next(loop) == 3