def merge_sort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else: 
                arr[k] = right_half[j]
                j += 1
            k += 1
        arr[k:] = left_half[i:]+right_half[j:]
if __name__ == "__main__":
    try:
        input_list = list(map(int,input("Enter a list of numbers separated by space ").split()))
        merge_sort(input_list)
        print("Sorted List: ",input_list)
    except ValueError:
        print("Invalid Input")
