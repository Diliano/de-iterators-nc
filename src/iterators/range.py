class NCRangeIterator:
    def __init__(self, n):
        self.n = n
        self.current_value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_value == self.n:
            raise StopIteration
        value_to_return = self.current_value
        self.current_value += 1
        return value_to_return
    

class NCRange:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return NCRangeIterator(self.n)
    
    def __len__(self):
        return self.n