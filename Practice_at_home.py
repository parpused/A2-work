# #Liner Search code 
# my_list = [7, 23, 1, 45, 12, 89, 34, 6, 58, 19]
# item = int(input("Please Enter the number that you want to find: "))
# found = False
# for index in range(len(my_list)) :
#     if item == my_list[index]:
#         found = True
# if found:
#     print("item Found")
# else:
#     print("Item was not found")

## The above code is correct

# #Binary Search

# my_list = [1, 6, 7, 12, 19, 23, 34, 45, 58, 89]
# item = int(input("Enter the number you want to search: "))
# found = False
# lower_bound = 0
# upper_bound = len(my_list) - 1
# while (found == False) and (lower_bound != upper_bound ):
#     index = (upper_bound + lower_bound)//2
#     if item == my_list[index]:
#         found = True
#     if item > my_list[index]:
#         lower_bound = index + 1
#     if item < my_list[index]:
#         upper_bound = index - 1
# if found:
#     print("Item Found")
# else:
#     print("Item Not found")

## The above code is correct
