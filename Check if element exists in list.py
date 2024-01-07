##Input: test_list = [1, 6, 3, 5, 3, 4]
##            3  # Check if 3 exist or not.
##Output: True
##Explanation: The output is True because the element we are looking is exist in the list.

lst=[ 1, 6, 3, 5, 3, 4 ] 
#checking if element 7 is present
# in the given list or not
i=7
# if element present then return
# exist otherwise not exist
if i in lst: 
	print("exist") 
else: 
	print("not exist")
