numbers = [2,4,5,6,4,4,2,34,31,32,14,6]

def bubble_sort(arr):
    for i in range(1,len(arr)):
        for j in range(len(arr)-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

print(bubble_sort(numbers))
