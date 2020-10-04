
# Fruit Name, Weight, dateofpurchase, Color, Quantity
fruits = ("apple", 2.5, 16101979, 'red', 10)

print("Tuple - It's same as 'List', only declaration syntax is changed")
print("Tuple is fast as compared to List, it's immutable & write-protected (to an extent)")
print("Tuple - values can be of different data-types")
print("\tNOTE: Traverse tuple from start & Index will be '0'")
print("\tNOTE: Traverse tuple from end & Index will be '-1'")
print("\n")
print("Tuple is ['apple', 2.5, 16101979, 'red', 10]")
print("\tFirst item in tuple (i.e. [0] element)\t\t", fruits[0])
print("\tLast item in tuple (i.e. [-1] element)\t\t", fruits[-1])
print("\tPrint range (i.e. [y:x] elements)\t\t\t", fruits[2:4])
print("\tMid to last (i.e. [y: or y::] elements)\t\t", fruits[2:])
print("\tStart to mid (i.e. [:x] elements\t\t\t", fruits[:3])
print("\t\tNOTE: x 'Exclusive' in all above cases\n")

print("\tStart & specific item (i.e. [::x] elements\t", fruits[::3])
print("\t\tNOTE: x 'Inclusive'\n")

print("\tPrint Entire Tuple (i.e. [::])\t\t\t\t", fruits[::])
print("\tPrint Entire Tuple (i.e. list name only)\t\t", fruits)
print("\n")

print("Tuple Functions")
print("\tNOTE: Tuple is immutable - means once declared can't be changed")
print("\t\tNo Insert of element in-between")

#fruits.insert(2, "Tasty")
#print("\tInsert element at index 2\t\t\t\t\t", fruits)

#fruits.append("Kashmiri Apple")  # fromCity
#print("\tAppend element to the List\t\t\t\t\t", fruits)

# fruits.pop(-2)
# print("\tDelete element (Method 1)\t\t\t\t\t", fruits)
# del fruits[-1]
# print("\tDelete element (Method 2)\t\t\t\t\t", fruits)
#
# fruits[-1] = "Red"
# print("\tUpdate value at particular index\t\t\t", fruits)