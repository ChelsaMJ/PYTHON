##Input: list = [4, 5, 6, 7, 8, 9]
##Output: [9, 8, 7, 6, 5, 4] 
##Explanation: The list we are having in the output is reversed to the list we have in the input.

# Reversing a list using slicing technique
def Reverse(lst):
new_lst = lst[::-1]
return new_lst


lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))
