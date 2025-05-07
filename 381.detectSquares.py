from collections import defaultdict
from typing import List

class DetectSquares:

    def __init__(self):
        self.hashMap = defaultdict(int)  # point -> frequency
        self.pointSet = set()

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        self.hashMap[point] += 1
        self.pointSet.add(point)

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        total = 0

        for x2, y2 in self.pointSet:
            # Skip if not same row or column — we only care about vertical/horizontal square alignment
            if x1 == x2 and y1 != y2:
                side = abs(y2 - y1)
                # Horizontal square to the right
                p2 = (x1 + side, y1)
                p3 = (x2 + side, y2)
                total += (
                    self.hashMap[(x2, y2)] *
                    self.hashMap.get(p2, 0) *
                    self.hashMap.get(p3, 0)
                )
                # Horizontal square to the left
                p2 = (x1 - side, y1)
                p3 = (x2 - side, y2)
                total += (
                    self.hashMap[(x2, y2)] *
                    self.hashMap.get(p2, 0) *
                    self.hashMap.get(p3, 0)
                )

            elif y1 == y2 and x1 != x2:
                side = abs(x2 - x1)
                # Vertical square upward
                p2 = (x1, y1 + side)
                p3 = (x2, y2 + side)
                total += (
                    self.hashMap[(x2, y2)] *
                    self.hashMap.get(p2, 0) *
                    self.hashMap.get(p3, 0)
                )
                # Vertical square downward
                p2 = (x1, y1 - side)
                p3 = (x2, y2 - side)
                total += (
                    self.hashMap[(x2, y2)] *
                    self.hashMap.get(p2, 0) *
                    self.hashMap.get(p3, 0)
                )

        return total
