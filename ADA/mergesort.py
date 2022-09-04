# helper function
def merge_two_sorted_array(arr1, arr2):
    result = []  # to store result
    len_arr1 = len(arr1)
    len_arr2 = len(arr2)
    i = 0
    j = 0

    # moving i and j pointer based on the low value
    while i < len_arr1 and j < len_arr2:
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # adding remaining elements
    while i < len_arr1:
        result.append(arr1[i])
        i += 1
    while j < len_arr2:
        result.append(arr2[j])
        j += 1
    return result


def mergesort(arr):
    if len(arr) <= 1:  # if single element it is already sorted
        return arr
    mid = len(arr)//2  # take mid element

    left = arr[:mid]
    right = arr[mid:]

    left = mergesort(left)  # sort left sub array
    right = mergesort(right)  # sort right sub array

    arr = merge_two_sorted_array(left, right)

    return arr


if __name__ == "__main__":
    arr = list(
        map(int, input("Enter space seperated values for the array: ").split()))
    print("Sorted Array: ")
    print(mergesort(arr))
