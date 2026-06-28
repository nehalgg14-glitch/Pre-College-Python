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
