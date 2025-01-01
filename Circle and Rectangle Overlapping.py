class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        nearest_x = max(x1, min(x2, xCenter))
        nearest_y = max(y1, min(y2, yCenter))
        xdistance = nearest_x - xCenter
        ydistance = nearest_y - yCenter
        return xdistance ** 2 + ydistance **2 <= radius ** 2
