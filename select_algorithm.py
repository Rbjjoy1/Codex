def partition(arr, low, high, pivot_index):
    pivot_value = arr[pivot_index]
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Move pivot to end
    store_index = low

    for i in range(low, high):
        if arr[i] < pivot_value:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1
    arr[store_index], arr[high] = arr[high], arr[store_index]  # Move pivot to its final place
    return store_index


def median_of_medians(arr, low, high, group_size=5):
    if high - low < group_size:
        return sorted(arr[low:high + 1])[len(arr[low:high + 1]) // 2]

    for i in range(low, high + 1, group_size):
        sub_high = min(i + group_size - 1, high)
        median = sorted(arr[i:sub_high + 1])[len(arr[i:sub_high + 1]) // 2]
        arr[low + (i // group_size)] = median

    return median_of_medians(arr, low, low + (high - low) // group_size)


def select(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot_index = median_of_medians(arr, 0, len(arr) - 1)
    pivot_index = partition(arr, 0, len(arr) - 1, pivot_index)

    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return select(arr[:pivot_index], k)
    else:
        return select(arr[pivot_index + 1:], k - pivot_index - 1)

# Example usage:
# arr = [3, 6, 2, 7, 5]
# k = 2  # Find the 3rd smallest element
# print(select(arr, k))