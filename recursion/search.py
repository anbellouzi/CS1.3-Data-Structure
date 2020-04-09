#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    if  array[index] == item:
        return index
    # check if item is found
    elif index == len(array)-1: #reached end of array without finding item 
        return None
    
    # call function recursively
    return linear_search_recursive(array, item, index+1)
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    left = 0
    right = len(array)-1
    while left <= right: 
        mid = left + (right - left)//2; 
        # Check if item is present at mid 
        if array[mid] == item: 
            return mid  
        # If item is greater
        elif array[mid] < item: 
            left = mid + 1
        # If item is smaller
        else: 
            right = mid - 1
       
    return "Not found"
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests

def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    if left == None: left = 0
    if right == None: right = len(array)-1

    # get middle 
    mid = ((right - left ) // 2) + left
    curr_item = array[mid]  # curr item 

    if item ==  curr_item:  # item found 
        return mid          # return found 
    elif right == left:     # reached end
        return None         # not found 

    
    if curr_item > item:
        return binary_search_recursive(array, item, left, mid-1)
    else:
        return binary_search_recursive(array, item, mid+1, right)

    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests


if __name__ == '__main__':
    print(binary_search(['a', 'b', 'c', 'd'], 'ds'))
