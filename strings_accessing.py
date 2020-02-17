'''
	Strings are array of unicode characters and we can access by index like array element access
	we use [] for accessing the string elements

	Indexing allows a negative address reference for accessing the elements from right to left

	-1 = last element in string
	-2 = second last element in string

	if we use other than numbers for accessing the string we will get TypeError.

	we get IndexError if we are try to access the element out of range

'''

string1 = "Purna chandrarao"
print("Starting element in the string")
print(string1[1])
print("\n")

print("Last element in the string")
print(string1[-1])
print("\n")


'''
	String slicing : To access the range of characters from string we use slice operator(:)

	0 : Start index

	-1 : Last index

	Last index is not count in string slicing
	
'''

string1 = "Purna chandrarao"
print("Initial String")
print(string1)
print("\n")

print(" String range 1 to 5")
print(string1[1:5])
print("String range second element to last second element")
print(string1[2:-2])



