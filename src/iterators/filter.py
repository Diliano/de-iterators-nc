class NCFilter:
    def __init__(self, func, collection):
        self.func = func
        self.collection_iterator = iter(collection)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            value = next(self.collection_iterator)
            if self.func(value):
                return value            