import numpy as np

'''
    If the two slices of the array divided by the index are equal 
    this function will return true otherwise it will return False.
'''
def equalSplits(array,index):
    sum_left = 0
    sum_right = 0
    
    for num in array[:index]:
        sum_left += num
    
    for num in array[index:]:
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

array = list()
num = input("Enter how many elements you want: ")
print ('Enter elements in array: ')
for i in range(int(num)):
    n = input("num : ")
    array.append(int(n))
print ('ARRAY: ',array)

print("Can be splitted: ",canBeSplitted(np.array(array)))