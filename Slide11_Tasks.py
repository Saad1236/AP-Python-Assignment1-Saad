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
numb = int(input("Enter Number to find Factorial: "))
for i in range(numb):
    fact = numb * fact
    numb = numb-1
    if fact <= 1:
        break
print("Factorial is:", fact)


#### Fibonacci Series ####
print("Task 3=Fibonacci Series")
n = int(input("Enter index (up to which series is to be printed): "))
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

print("Enter Strings and sub-string to be checked:")
string1 = input("Enter string1: ")
string2 = input("Enter sub-string: ")
n = 0
for char in string1:
    for cha in string2:
        if char == char:
            n = n + 1
    if n == len(string2):
        print("Substring Found at", n)
        break
    else:
        print("Substring not found")

print("Enter Strings to be concatenated")
string1 = input("String1: ")
string2 = input("String2: ")
print(string1 + string2)

##### Calculator #####
print("Task 5=Calculator")


def calculator(Op1, Op2):
    select = input("Choose the Operator + - * / ")
    if select == "+":
        print("Sum of the two digits is: ", Op1 + Op2)
    elif select == "-":
        print("2nd minus 1st is: ", Op1 - Op2)
    elif select == "*":
        print("1st No multiplied by 2nd is:  ", Op1 * Op2)
    elif select == "/":
        print("1st No divided by 2nd is: ", Op1 / Op2)
    else:
        print("Select from the given operators")
        calculator(Op1, Op2)
    return 0


Operand1 = float(input("Enter 1st Number: "))
Operand2 = float(input("Enter 2nd Number: "))
calculator(Operand1, Operand2)
