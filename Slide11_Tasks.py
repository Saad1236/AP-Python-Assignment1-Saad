##### Variable Swap #####
print("Task 1=Variable Swap")
a = input("Enter Variable A: ")
b = input("Enter Variable B: ")
temp = a
a = b
b = temp
print("Variable A after swap: ", a)
print("Variable B after swap: ", b)

##### Factorial #####
print("Task 2=Factorial Calculator")
fact = 1
numb = int(input("Enter Number: "))
for i in range(numb):
    fact = numb * fact
    numb = numb-1
    if fact <= 1:
        break
print("Factorial is:", fact)


#### Fibonacci Series ####
print("Task 3=Fibonacci Series")
n = int(input("Enter index up to which series is to be printed): "))
k = 0
j = 1
if n <= 0:
    print("Value at index 0: ", k)
else:
    print("Value at index 0: ", k)
    print("Value at index 1: ", j)
for i in range(n - 1):
    next_value = j + k
    print("Value at index", i + 2, ":", next_value)
    k = j
    j = next_value

##### Check string operations: Len, substring, concatenate #####
print("Task 4=Check String Operations")
string1 = input("Enter string to find its length: ")
print("Length of string is: ", len(string1))

string1 = input("Enter string1: ")
string2 = input("Enter sub-string to be checked: ")
if string2 == '':
    print("Empty Substring present by default")
elif string2 in string1:
    print("Substring found")
else:
    print("Substring not found")