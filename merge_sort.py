numbers = [2,4,5,6,4,4,2,34,31,32,14,6]

def merge_sort(arr):
    if len(arr)<2:
        return arr

    mid = len(arr)//2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    l = r = 0
    merged_arr = []

    while l<len(left_arr) and r<len(right_arr):
        if left_arr[l] < right_arr[r]:
            merged_arr.append(left_arr[l])
            l+=1
        else:
            merged_arr.append((right_arr[r]))
            r+=1
    merged_arr += left_arr[l:]
    merged_arr += right_arr[r:]
    return merged_arr

print(merge_sort(numbers))
