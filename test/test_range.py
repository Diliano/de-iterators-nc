from src.iterators.range import NCRangeIterator, NCRange
import pytest

@pytest.fixture
def test_iterator():
    return NCRangeIterator(5)

@pytest.fixture
def test_iterable():
    return NCRange(5)

class TestNCRangeIterator:
    def test_is_an_iterator(self):
        assert hasattr(NCRangeIterator, "__next__")

    def test_stores_given_n_as_n_property(self, test_iterator):
        assert test_iterator.n == 5

    def test_iter_method_returns_self(self, test_iterator):
        assert iter(test_iterator) is test_iterator

    def test_next_method_returns_next_element(self, test_iterator):
        assert next(test_iterator) == 0

    def test_next_method_handles_multiple_invocations(self, test_iterator):
        assert next(test_iterator) == 0
        assert next(test_iterator) == 1
        assert next(test_iterator) == 2

    def test_next_method_raises_stop_iteration_exception_if_range_reached(self, test_iterator):
        assert next(test_iterator) == 0
        assert next(test_iterator) == 1
        assert next(test_iterator) == 2
        assert next(test_iterator) == 3
        assert next(test_iterator) == 4
        with pytest.raises(StopIteration):
            next(test_iterator)

    def test_can_be_converted_to_list(self, test_iterator):
        assert list(test_iterator) == [0, 1, 2, 3, 4]
    
    def test_can_only_be_iterated_over_once(self, test_iterator):
        assert list(test_iterator) == [0, 1, 2, 3, 4]
        assert list(test_iterator) == []


class TestNCRange:
    def test_stores_given_n_as_n_property(self, test_iterable):
        assert test_iterable.n == 5

    def test_iter_method_returns_an_iterator(self, test_iterable):
        assert hasattr(iter(test_iterable), "__next__")

    def test_can_be_converted_to_a_list(self, test_iterable):
        assert list(test_iterable) == [0, 1, 2, 3, 4]

    def test_can_be_iterated_over_multiple_times(self, test_iterable):
        assert list(test_iterable) == [0, 1, 2, 3, 4]
        assert list(test_iterable) == [0, 1, 2, 3, 4]
        assert list(test_iterable) == [0, 1, 2, 3, 4]
        assert list(test_iterable) == [0, 1, 2, 3, 4]

    def test_len_method_returns_length(self, test_iterable):
        assert len(test_iterable) == 5