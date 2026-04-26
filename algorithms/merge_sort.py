def merge_sort(arr, left, right):
    if left >= right:
        return

    mid = (left + right) // 2

    yield from merge_sort(arr, left, mid)
    yield from merge_sort(arr, mid + 1, right)

    yield from merge(arr, left, mid, right)


def merge(arr, left, mid, right):
    left_part = arr[left:mid+1]
    right_part = arr[mid+1:right+1]

    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        yield ("compare", k, None)

        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1

        yield ("overwrite", k, arr[k])
        k += 1

    while i < len(left_part):
        arr[k] = left_part[i]
        yield ("overwrite", k, arr[k])
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        yield ("overwrite", k, arr[k])
        j += 1
        k += 1