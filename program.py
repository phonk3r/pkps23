def is_alternating(arr):

    n = len(arr)
    if n == 1:
        return False
    for i in range(1, n):
        if arr[i] * arr[i-1] >= 0:
            return False
    return True


arr1 = [1, -2, 3, -4, 5]
arr2 = [1, -2, 3, -4, -5]
arr3 = [1, 2, 3, 4, 5]
arr4 = [-1, 2, -3, 4, -5]
arr5 = [0, 1, -2, 3, -4]

for i, arr in enumerate([arr1, arr2, arr3, arr4, arr5]):
    if is_alternating(arr):
        print(f"Массив {i+1} является знакочередующейся последовательностью")
    else:
        print(f"Массив {i+1} не является знакочередующейся последовательностью")
