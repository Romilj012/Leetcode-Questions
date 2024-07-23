class DetectSquares:
    def __init__(self):
        self.dict = defaultdict(int)
        self.arr = []

    def add(self, point: List[int]) -> None:
        self.arr.append(point)
        self.dict[tuple(point)] +=1 

    def count(self, point: List[int]) -> int:
        result = 0
        px, py = point
        for x, y in self.arr:
            if (abs(px-x) != abs(py-y)) or px == x or py == y:
                continue
            result += self.dict[(x,py)] * self.dict[(px,y)]
        return result



# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)