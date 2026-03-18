class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        a = list()
        for i in arr:
            if i == 0:
                a.append(i)
            a.append(i)
        while len(a) > len(arr):
            a.pop()
        for i in range(len(arr)):
            arr[i] = a[i]
