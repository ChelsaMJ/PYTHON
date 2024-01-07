##Input: lst = [10,20,30,40]
##Output: 4
##Explanation: The output is 4 because the length of the list is  4.

# Initializing list
test_list = [1, 4, 5, 7, 8]

# Printing test_list
print("The list is : " + str(test_list))

# Finding length of list using loop
# Initializing counter
counter = 0
for i in test_list:

	# incrementing counter
	counter = counter + 1

# Printing length of list
print("Length of list using naive method is : " + str(counter))
