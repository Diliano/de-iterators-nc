from src.iterators.filter import NCFilter
import pytest

"""
Reusable test components
"""
def is_odd(num):
        return num % 2 != 0

@pytest.fixture
def test_iterator():
    return NCFilter(is_odd, [1, 2, 3])


"""
Test suite for NCFilter class
"""
def test_filter_is_an_iterator():
    assert hasattr(NCFilter, "__next__")

def test_stores_input_function_as_func_property(test_iterator):
    assert test_iterator.func is is_odd

def test_stores_input_collection_as_collection_iterator_property(test_iterator):
    assert hasattr(test_iterator.collection_iterator, "__next__")

def test_iter_method_returns_self(test_iterator):
    assert iter(test_iterator) is test_iterator

def test_next_method_applies_function_to_and_returns_next_element(test_iterator):
    assert next(test_iterator) == 1

def test_next_method_handles_multiple_invocations(test_iterator):
    assert next(test_iterator) == 1
    assert next(test_iterator) == 3

    """
    Extra test for multiple True and False evaluations
    """
    def is_odd(num):
        return num % 2 != 0
    collection = [1, 2, 3, 40, 22, 17, 20, 19]
    test_iterator = NCFilter(is_odd, collection)
    assert next(test_iterator) == 1
    assert next(test_iterator) == 3
    assert next(test_iterator) == 17
    assert next(test_iterator) == 19

def test_raises_stop_iteration_exception_if_out_of_elements(test_iterator):
    assert next(test_iterator) == 1
    assert next(test_iterator) == 3
    with pytest.raises(StopIteration):
        next(test_iterator)

def test_iterator_can_be_converted_to_a_list(test_iterator):
    assert list(test_iterator) == [1, 3]

def test_iterator_can_only_be_iterated_over_once(test_iterator):
    assert list(test_iterator) == [1, 3]
    assert list(test_iterator) == []