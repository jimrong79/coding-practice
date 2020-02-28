
def binary_search(arr, target):
    l, r = 0, len(arr)
    
    while l <= r:
        m = (l + r) >> 1
        
        if arr[m] == target:
            return m
        
        elif arr[m] < target:
            l = m + 1
        
        else:
            r = m - 1
    
    return -1
        
    
    
arr = [1,2,3,4,5,6,10,13,23,24,33,45,56,67]

print (binary_search(arr, 67))