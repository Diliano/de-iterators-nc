class NCEnumerate:
    def __init__(self, collection):
        self.collection_iterator = iter(collection)
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            result = (self.index, next(self.collection_iterator))
            self.index += 1
            return result
        except StopIteration:
            raise StopIteration
            