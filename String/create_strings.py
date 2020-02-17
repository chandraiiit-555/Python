'''
	strings are nothing but group of characters(array of bytes represent unicode characters) and 
	strings are immutable means we can't change the value of strings. 

	We used single and double quotes to represent the strings in python
	
	If you want to mix the single quote with double quotes we should use escape characters to show the
	values

	ex: " this can't use " : "this can/' use"(backslash)

	we can use thriple quotes to escape the single and double quotes.

	there is no char data type in python so single character we can assume as string with length 1

'''

'''
	Creating strings.

	we can create the strings using single quote or doubt quote or even thriple quotes also.

'''
string1_with_single_quote = 'This is chandra tanikonda'
print("strings creation with single quotes")
print(string1_with_single_quote)
print("\n")

strings_with_double_quote = "Jama Investment Advisory"
print("Strings with double quotes")
print(strings_with_double_quote)
print("\n")

strings_with_thriple_quotes = "Mutual Fund and Direct Equity Advisory Services"
print("Strings with thriple quotes")
print(strings_with_thriple_quotes)
print("\n")
