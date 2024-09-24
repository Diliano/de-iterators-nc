from src.iterators.enumerator import NCEnumerate
import pytest

def test_enumerator_is_an_iterator():
    assert hasattr(NCEnumerate, "__next__")

def test_stores_input_collection_as_collection_iterator_property():
    test_iterator = NCEnumerate([1, 2, 3])
    assert hasattr(test_iterator.collection_iterator, "__next__")

def test_iter_method_returns_self():
    test_iterator = NCEnumerate([1, 2, 3])
    assert iter(test_iterator) is test_iterator

def test_next_method_returns_index_and_value_of_next_element():
    test_iterator = NCEnumerate([1, 2, 3])
    assert next(test_iterator) ==  (0, 1)

def test_next_method_handles_multiple_invocations():
    test_iterator = NCEnumerate([1, 2, 3])
    assert next(test_iterator) ==  (0, 1)
    assert next(test_iterator) ==  (1, 2)
    assert next(test_iterator) ==  (2, 3)

def test_raises_stop_iteration_exception_if_out_of_elements():
    test_iterator = NCEnumerate([1, 2, 3])
    assert next(test_iterator) ==  (0, 1)
    assert next(test_iterator) ==  (1, 2)
    assert next(test_iterator) ==  (2, 3)
    with pytest.raises(StopIteration):
        next(test_iterator)

def test_iterator_can_be_converted_to_a_list():
    test_iterator = NCEnumerate([1, 2, 3])
    assert list(test_iterator) == [(0, 1), (1, 2), (2, 3)]

def test_iterator_can_only_be_iterated_over_once():
    test_iterator = NCEnumerate([1, 2, 3])
    assert list(test_iterator) == [(0, 1), (1, 2), (2, 3)]
    assert list(test_iterator) == []