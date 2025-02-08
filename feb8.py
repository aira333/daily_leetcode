class NumberContainers:

    def __init__(self):
        self.map = defaultdict(sortedcontainers.SortedSet)
        self.indexMap = {}

    def change(self, index: int, number: int) -> None:
        if index in self.indexMap:
            prevNumber = self.indexMap[index]
            self.map[prevNumber].discard(index)
            if not self.map[prevNumber]:
                del self.map[prevNumber]
        self.indexMap[index] = number
        self.map[number].add(index)

    def find(self, number: int) -> int:
        return next(iter(self.map[number]), -1) if number in self.map else -1