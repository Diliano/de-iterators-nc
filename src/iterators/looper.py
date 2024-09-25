class Looper:
    def __init__(self, collection):
        if not collection:
            raise ValueError("Provided argument must not be empty")
        if not hasattr(collection, "__iter__"):
            raise TypeError("Provided argument must be iterable")
        
        self.collection = collection
        self.collection_iterator = iter(self.collection)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                return next(self.collection_iterator)
            except StopIteration:
                self.collection_iterator = iter(self.collection)