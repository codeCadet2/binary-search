#This search goes through the ordered list one by one checking for the target

def naive_search(l, target):
    # example l = [1, 3, 10, 12]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


#Binary search divides and conquers the list search

def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) -1
    
    midpoint = (low + high) // 2
    
    if l[midpoint] == target: 
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint -1 )
    else: 
        #target > l(midpoint)
        return binary_search(l, target,midpoint +1, high)
    
if __name__ == '__main__':
    l = [1, 3, 5, 10, 12]
    target = 10 #this should print list item number 3
    print(binary_search(l, target))
    