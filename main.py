# for i in range(10):
#     print("Hello Students")
# z = x+" "+y

# x = "Shaheer"
# y = "Ghori"
# x = 23
# y = 5
# z=x % y
# print(z)

# a = int(input("Enter fisrt name: "))
# b = int(input("Enter last name: "))

# z = a + b
# print(z)

# marks = int(input("Enter marks: "))

# if marks >= 70:
#     print("A")
# elif marks >= 50:
#     print("pass")
# else:
#     print("Fail")

# num_1 = int(input("Enter num 1: "))
# num_2 = int(input("Enter num 2: "))
# opr = input("Enter operator 2: ")

# if opr == "+":
#     print(num_1 + num_2)
# elif opr == "-":
#     if num_1 > num_2:
#         print(num_1 - num_2)
#     else:
#         print(num_2 - num_1)
# elif opr == "*":
#     print(num_1 * num_2)
# elif opr == "/":
#     print(num_1 / num_2)
# else:
#     print("invaild operator")

# for index in range(11,0,-1):
#     print(f"{index} SHAHEER")

# value = input("Enter value: ")
# my_data = "SHAHEER GHORI"
# array = []
# count = 0
# for i in my_data:
#     if value.upper() == i:
#         count+=1
#         array.append(count)
#     else:
#         count+=1

# if len(array) == 0:
#     print("value not found")
# else:
#     for i in array:
#         print(f"{value} fount at {i}")

# if count != 0:
#     print(f"{value} appears {count} times")
# else:
#     print(f"{value} doesnot appears")


# value = input("Enter value: ")
# my_data = "SHAHEER GHORI"
# array = []
# count = 0
# for i in my_data:
#     if value.upper() == i:
#         count+=1
#         array.append(count)
#     else:
#         count+=1

# if len(array) == 0:
#     print("value not found")
# else:
#     for i in array:
#         print(f"{value} fount at {i}")

# my_data = "MINHAS RUPSI"
# count = -1
# found = False
# letter = input("Enter a letter: ")
# for i in my_data:
#     count+=1
#     found = True
#     print(letter,"found at",count)

# if found == False:
#     print(letter,"notfound")

# def first_letter():
#     my_data = "MINHAS RUPSI"
#     count = -1
#     found = False
#     letter = input("Enter a letter: ").upper()
#     for i in my_data:
#         count+=1
#         if i == letter:
#             found = True
#             return print(letter,"found at",count)
    
#     if found == False:
#         return print(letter,"notfound")

# print(first_letter())

# my_data = "MINHAS RUPSI"
# count = -1
# found = False
# letter = input("Enter a letter: ").upper()
# for i in my_data:
#     count+=1
#     if i == letter:
#         found = True
#         print(letter,"found at",count)
#         break

# if found == False:
#     print(letter,"notfound")

# DECLARE  MY_LIST : ARRAY [0:9] OF STRING

# my_list = ["" for i in range(5)]

# for i in range(5):
#     name = input("Enter name: ")
#     my_list[i] = name

# print(my_list)


# my_list = ['a','b','c','d','e']
# found = False
# search = input("Enter to search: ")
# for i in range(5):
#     if my_list[i] == search:
#         found = True
#         break

# if found == True:
#     print("name found at", i)
# else:
    # print("name not found")

# my_list = ['a','b','c','d','e']
# found = False
# i = 0
# name = input("Enter to name to search: ").lower()
# while found == False and i <5:
#     if my_list[i] == name:
#         found = True
#     else:
#         i+=1

# if found == True:
#     print("name found at", i)
# else:
#     print("name not found...")

