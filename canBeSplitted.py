import numpy as np

'''
    If the two slices of the array divided by the index are equal 
    this function will return true otherwise it will return False.
'''
def equalSplits(array,index):
    left_array = array[:index]
    right_array = array[index:]
    
    sum_left = 0
    sum_right = 0
    
    for num in left_array:
        sum_left += num
    
    for num in right_array:
        sum_right += num
    
    return sum_right == sum_left

def canBeSplitted(array):
    if len(array) <= 0:
        return 0
    
    flag = -1
    for index in range(len(array)):
        if(equalSplits(array,index)):
            flag = 1
    return flag

print(canBeSplitted(np.array([1,3,3,8,4,3,2,3,3])))