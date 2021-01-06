numbers = [2,4,5,6,4,4,2,34,31,32,14,6]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i-1
        target = arr[i]
        while j>=0 and target < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = target
    return arr

print(insertion_sort(numbers))
