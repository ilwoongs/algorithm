numbers = [2,4,5,6,4,4,2,34,31,32,14,6]

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        temp = arr[min_index]
        arr[min_index] = arr[i]
        arr[i] = temp
    return arr

print(selection_sort(numbers))
