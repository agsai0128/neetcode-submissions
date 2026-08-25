"""
Approach:
maintain a dictionary from key to a list of (timestamp, value) pairs
set() just appends because timestamp are stricktly increasing
get() perform binary search on that key's list
if no timestamp small enough, return ""

Time and space:
set: O(1)
get: O(log n)

space: O(total number of set calls)
"""

class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        arr = self.store[key]

        left, right = 0, len(arr) - 1
        res = ""

        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] <= timestamp:
                res = arr[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return res
