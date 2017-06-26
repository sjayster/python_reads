def find(arr, n):
    s = 0
    while s < len(arr):
        if arr[s] == n:
            return s
        s += abs(arr[s] - n)

arr = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8]
n = 5
print find(arr, n)
