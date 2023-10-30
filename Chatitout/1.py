def max_index_difference(n, arr):
    max_diff = -1
    min_so_far = arr[0]
    min_so_far_index = 0
    for i in range(1, n):
        if arr[i] < min_so_far:
            min_so_far = arr[i]
            min_so_far_index = i
        else:
            max_diff = max(max_diff, i - min_so_far_index)
    return max_diff if max_diff != 0 else -1

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
result = max_index_difference(n, arr)
print(result)
