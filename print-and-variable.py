print("Test Pass - Double quotes are good to use in print() function")
print('Test Pass - Single quote is good to use in print() function')
print("Test Pass - Use Double quotes to print ' in the String")
print('Test Pass - Use Single quotes to print " in the String')
print("Test Fail - No Single or Double quotes leads to --> Syntax Error")
print("\n")

number = 2020
objective = "Learning Python"
learningfrom = 'udemy'

print("\tNOTE: No need to provide data-type, automatic detection based on value")
print("Test Pass - Using , to concatenate different data-type like String and Number -", number)
print("Test Pass - Using {} and format() to concatenate different data-type like String and Number")
print("\t{} {} {} {} {}". format(objective, "from", learningfrom, "in", number))
print("\t{}".format(objective, learningfrom), "--> One {} missing (compare with previous output)")
print("\t\tNOTE: Number of {} and arguments in format() must match else output will be based on number of {}")

print("Test Fail - Using + to concatenate different data-type like String and Number --> TypeError")
# Uncomment to test above Test Fail
# print("Test Fail - Using + to concatenate String and Number -->" + num)
print("\n")

print("Test Pass - Use , for Strings Concatenation -", objective, learningfrom)
print("\tNOTE: Space is automatically added between string concatenation when , is used")
print("Test Pass - Use + for Strings Concatenation -" + objective + ' ' + learningfrom)
print("\tNOTE: Need to add Space for string concatenation when + is used")
print("\n")

print("Test Pass - Declare multiple variables in single line")
print("Test Pass - Use special character like tab, enter within Single/Double quotes")
num, decimal, text = 16, 5.5, "Python is Solid"
print("\tConcatenate different Data Types Variables -", '\n\tInteger:', num, "\n\tFloat:\t", decimal, "\n\tString:\t", text)
print("\n")

print("Test Pass - Use 'type(variable name)' to check data-type")
print("\tVariable 'num' is of type", type(num))
print("\tVariable 'decimal' is of type", type(decimal))
print("\tVariable 'text' is of type", type(text))