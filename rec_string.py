def reverse_str(str1):
    # recursive function needs two case - base case and recursive case
    # base case for this program - if the length of string is 1 or string is empty
    if len(str1)==1:
        return str1
    else:
        return reverse_str(str1[1:])+str1[0]

str1 = input("Enter the string: ")
str2 = reverse_str(str1)
print(str2)

