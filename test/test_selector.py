from src.iterators.selector import Selector
import pytest

def test_selector_is_an_iterator():
    assert hasattr(Selector, "__next__")

def test_selector_stores_given_collections_as_collection_iterator_properties():
    sel = Selector([1, 2, 3], [True, True, True])
    assert hasattr(sel.collection1_iterator, "__next__")
    assert hasattr(sel.collection2_iterator, "__next__")

def test_iter_method_returns_self():
    sel = Selector([1, 2, 3], [True, True, True])
    assert iter(sel) is sel

def test_next_method_returns_next_element_that_has_a_truthy_corresponding_element():
    sel = Selector([1, 2, 3], [True, True, True])
    assert next(sel) == 1

def test_next_method_handles_multiple_invocations():
    sel = Selector([1, 2, 3], [True, False, True])
    assert next(sel) == 1
    assert next(sel) == 3

"""
Handling arguments of different lengths

As we are selecting elements from collection1, if collection2 is shorter
in length, all of the missing 'corresponding elements' will be deemed True

If collection2 is longer in length, collection1 will naturally raise a
StopIteration exception once iterated over
"""
def test_handles_collection1_longer_than_collection2():
    sel = Selector([1, 2, 3, 4], [True, False, True])
    assert next(sel) == 1
    assert next(sel) == 3
    assert next(sel) == 4

    sel = Selector([1, 2, 3, 4, 5, 6], [True, False, True])
    assert next(sel) == 1
    assert next(sel) == 3
    assert next(sel) == 4
    assert next(sel) == 5
    assert next(sel) == 6

def test_handles_collection2_longer_than_collection1():
    sel = Selector([1, 2, 3], [True, False, True, True, False])
    assert next(sel) == 1
    assert next(sel) == 3
    with pytest.raises(StopIteration):
        next(sel)