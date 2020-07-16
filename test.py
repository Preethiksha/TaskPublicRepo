string_value = input("enter name:")
print( type(string_value))
age = int(input("enter age:"))
print( type(age))
marks = input("enter marks(separate using comma):").split(',')
print( type(marks))
tuple_data = tuple(input("enter subject(separate using comma):").split(','))
print( type(tuple_data))
set_data = set(input("enter semester(separate using comma):").split(','))
print( type(set_data))

user_data = {}


user_data['name'] = string_value
user_data['age'] = age
user_data['marks'] = marks
user_data['subjects'] = tuple_data
user_data['semester'] = set_data

print(user_data)
print( type(user_data))

#list
NumList = []

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

print("\nPositive Numbers in this List are : ")
for j in range(Number):
    if(NumList[j] >= 0):
        print(NumList[j], end = '   ')
        
        
 # Python Program to Add two Lists
 
NumList1 = [10, 20, 30]
NumList2 = [15, 25, 35]
total = []
 
for j in range(3):
    total.append( NumList1[j] + NumList2[j])
 
print("\nThe total Sum of Two Lists =  ", total)


# Functions Example
def sumAndAverage(x, y, z):
    Sum = x + y + z
    Average = Sum/3
    print("\n %d is the Total Sum of three Numbers." %Sum)
    print("\n %d is the Average of three Numbers.\n" %Average)
    
# Allows User to enter three values
a = int(input("\nPlease Enter the First Value. a =  "))
b = int(input("\nPlease Enter the Second Value. b =  "))
c = int(input("\nPlease Enter the Third Value. c =  "))

# Calling the Function
sumAndAverage(a, b, c)
sumAndAverage(10, 20, 30)
