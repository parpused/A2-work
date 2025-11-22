# # DECLARE ARRAY 

# my_list = [3, 5, 7, 9, 11, 12, 14, 16, 18, 21, 24, 26, 28, 30, 32, 35, 37, 39, 42, 44, 46, 48, 50, 53, 55, 57, 59, 61, 63, 65, 67, 70, 72, 74, 76, 78, 80, 83, 85, 87, 89, 91, 93, 95, 97, 98, 99, 100] 

# def binary_search(num):
#     global my_list
#     top = 0
#     bottom = len(my_list) - 1
#     while top <= bottom:
#         middle = int((top+bottom)/2)
#         if num == my_list[middle]:
#             return middle
#         elif num> my_list[middle]:
#             top == middle +1
#         else:
#             bottom = middle -1
#     return -1

# num = int(input("Enter a number to search: "))
# x = binary_search(num)
# if x == "-1":
#     print("Nmber not found ...") 
# else:
#     print("Number found at",x)


my_list = [ 5, 7, 9, 11, 12, 14, 16, 18, 21, 24, 26, 28, 30, 32, 35, 37, 39, 42, 44, 46, 48, 50, 53, 55, 57, 59, 61, 63, 65, 67, 70, 3, 72, 74, 76, 78, 80, 83, 85, 87, 89, 91, 93, 95, 97, 98, 99, 100]

def bubble_sort():
    global my_list
    for x in range(len(my_list) -1):
        for y in range(len(my_list) -1):
            if my_list[y] > my_list[y +1]:
                temp = my_list[y]
                my_list[y] = my_list[y +1]
                my_list[y+1]=temp

def binary_search(num):
    global my_list
    top = 0
    bottom = len(my_list) - 1  
    while top <= bottom:
        middle = (top + bottom) // 2
        if num == my_list[middle]:
            return middle
        elif num > my_list[middle]:
            top = middle + 1
        else:
            bottom = middle - 1
    return -1

bubble_sort()

num = int(input("Enter a number to search: "))
x = binary_search(num)
if x == -1:
    print("Number not found ...")
else:
    print("Number found at index", x)

