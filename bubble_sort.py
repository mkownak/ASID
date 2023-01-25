def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr
  
  
l1=[1,3,5,6,7,7,4,3]

bubble_sort(l1)
print(l1)
