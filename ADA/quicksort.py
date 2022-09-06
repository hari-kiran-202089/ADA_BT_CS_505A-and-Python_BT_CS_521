def partition(arr, start, end):
    # taking last element as pivot
    pivot = arr[end]
    i = start
    j = end-1
    while i <= j:
        # swapping elements accordingly
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]

    # inserting pivot element in the right position
    arr[i], arr[end] = arr[end], arr[i]
    return i


def quicksort(arr, start, end):
    if end - start <= 1:
        return

    # pivot index
    idx = partition(arr, start, end-1)

    # sorting left subarray
    quicksort(arr, start, idx)
    # sorting right subarray
    quicksort(arr, idx, end)


if __name__ == "__main__":
    arr = input("Enter space seperated values: ")
    arr = list(map(int, arr.split()))
    print("Unsorted array: ")
    print(arr)
    quicksort(arr, 0, len(arr))
    print("Sorted array: ")
    print(arr)