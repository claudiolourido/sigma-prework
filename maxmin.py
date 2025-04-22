def maxmin(arr):
    """
    Given a list of numbers, return the maximum and minimum values.
    """
    smallest = float('inf')
    largest = float('-inf')
    for num in arr:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    return [smallest, largest]



test = [54, -4343, 0, 999, -213]
print(maxmin(test))