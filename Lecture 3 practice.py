# Pre-College-Python
print("hello world")
list = [2, 1 , 3]
list.insert(2, 6)
print(list)
list.sort()
print(list)
list.append(5)
print(list)
list.insert(0, 4)
list.sort()
print(list)
list.insert(5,1)
print(list)
list.sort()
print(list)
list.remove(4)
print(list)
list.remove(1)
print(list)

#Tuple
tuple = (1,2,3,4,5,6,7,8,9)
print(type(tuple))
print(tuple.index(5))
print(tuple.count(2)) 

#WAP to ask the user to enter their 3 favourite names of movies and store them in a list.
movies = []
movie1 = input("Enter your first favourite movie: ")
movie2 = input("Enter your second favourite movie: ")
movie3 = input("Enter your third favourite movie: ")
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print("Your favourite movies are:", movies)

#Palindrome method
list1 = [1,2,1]
list2 = [1,2,3]
copy_list1 = list1.copy()
copy_list1.reverse()
print("The list is a palindrome") if copy_list1 == list1 else print("The list is not a palindrome")
copy_list2 = list2.copy()
copy_list2.reverse()
if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")

    copy_list2 = list2.copy()
copy_list2.reverse()
print("The list is a palindrome") if copy_list2 == list2 else print("The list is not a palindrome")
copy_list2 = list2.copy()
copy_list2.reverse()
if(copy_list2 == list2):
    print("palindrome")
else:
    print("not palindrome")


#WAP to count the no. of students with A grade in the following tuple.
Grades = ("C" , "D" , "A" , "B" , "B" , "A" )
#count = Grades.count("A")
#print("Number of students with A grade:", count)
print("Number of students with A grade: ", Grades.count("A"))

#store the above grades in list and sort them from "A" to "D"
grade_list = ["C", "D", "A", "B", "B", "A"]
grade_list.sort()
print("Sorted grades from A to D:", grade_list)

#Chatgpt ques based on what i learnt from 3 lectures.

#1. Take your name as input and print:
name = input("Enter your name: ")
print(name)

#2. Take two integers from the user. Print:Sum, Difference, Product.
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
print("Sum: ", a + b)
print("Difference: ", a - b)
print("Product: ", a * b)

#3. Take the radius of a circle. Print its area. (Use π = 3.14)
radius = float(input("Enter the radius of the circle: "))
area = 3.14 * radius * radius
print("Area of the circle: ", area)

#4. Take length and breadth of a rectangle. Print: Area, Perimeter.
length = float(input("Enter your length of a rectangle: "))
breadth = float(input("Enter your breadth of a rectangle: "))
print("Area of the rectangle: ", length*breadth )
print("Perimeter of the rectangle: ", 2*(length+breadth))

#5. Take marks of three subjects. Print: Total, Average.
marks1 = float(input(" Enter marks of first student1: "))
marks2 = float(input(" Enter marks of second student2: "))
marks3 = float(input(" Enter marks of third student3: "))
print("Total marks: ", marks1 + marks2 + marks3)
print("Average marks: ", (marks1 + marks2 + marks3) / 3)

#6. Take two numbers.Print whether: First number is greater, First number is smaller,Both are equal.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    print("First number is greater than the second number.")
elif num1 < num2:
    print("First number is smaller than the second number.")
else:
    print("Both numbers are equal.")

#7. Take a number. Print: Square, Cube.
a = float(input("Enter a number: "))
print("Square of a num a: ", a**2)
print("Cube of a num a: ", a**3)

#8. Take age.Print: After 5 years =, 10 years ago =
Age = int(input("Enter your age: "))
print("Age after 5 years: ", Age + 5)
print("Age 10 years ago: ", Age - 10)

#Take principal, rate and time. Find Simple Interest. Formula:SI = (P × R × T)/100
P = float(input("Enter your principal amount: "))
R = float(input("Enter your rate of interest: "))
T = float(input("Enter your time in years: "))
SI = (P * R * T) / 100
print("Simple Interest: ", SI)  

#Take a float. Convert it into int. Observe the output.
num = float(input("Enter a float number: "))
print("Integer value: ", int(num))

#Take two boolean values from the user. Print:AND, OR, NOT.
bool1 = bool(input("Enter first boolean value (True/False): "))
bool2 = bool(input("Enter second boolean value (True/False): "))
print("AND: ", bool1 and bool2)
print("OR: ", bool1 or bool2)
print("NOT first boolean value: ", not bool1)

#Take your birth year. Calculate your age. (Current year = 2026)
birth_year = int(input("Enter your birth year: "))
current_year = 2026
age = current_year - birth_year
print("Your age is:", age)

#Swap two variables without using a third variable.
a = 1
b = 2
print(a,b)
a , b = b,a 
print(a,b)




