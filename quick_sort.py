numbers = [2,4,5,6,4,4,2,34,31,32,14,6]

def quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[len(arr)//2]
    left_arr = []
    right_arr = []
    equal_arr = []

    for i in arr:
        if i < pivot:
            left_arr.append(i)
        elif i> pivot:
            right_arr.append(i)
        else:
            equal_arr.append(i)
    return quick_sort(left_arr) + equal_arr + quick_sort(right_arr)

print(quick_sort(numbers))
