

def merge_sort(arr):
       
    n = len(arr)
    
    if n <= 1:
        return arr
    
    m = n // 2
    
    left = merge_sort(arr[:m])
    right = merge_sort(arr[m:])
    
    res = merge(left, right)
    
    return res

def merge(left, right):
    
    l = 0
    r = 0
    res = []
    
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
            
    while l < len(left):
        res.append(left[l])
        l += 1
        
    while r < len(right):
        res.append(right[r])
        r += 1
        
    return res
    
    
    
test = [1]

print (merge_sort(test))

