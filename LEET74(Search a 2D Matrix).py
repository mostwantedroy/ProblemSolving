class Solution:
    def binarySearch(self, list, target):
        start = 0
        end = len(list)

        found = False

        while start < end:
            mid = (start + end) // 2
            if list[mid] < target:
                start = mid + 1
            elif list[mid] > target:
                end = mid - 1
            else:
                found = True
                break

        return found

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        temp = []

        for item in matrix:
            temp.extend(item)

        return self.binarySearch(temp, target)