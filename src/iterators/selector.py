class Selector:
    def __init__(self, collection1, collection2):
        self.collection1_iterator = iter(collection1)
        self.collection2_iterator = iter(collection2)

    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            val1 = next(self.collection1_iterator)
            try:
                val2 = next(self.collection2_iterator)
            except StopIteration:
                val2 = True
            if val2:
                return val1