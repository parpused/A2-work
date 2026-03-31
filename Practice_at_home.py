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

# #bubble sort

# my_list = [7, 23, 1, 45, 12, 89, 34, 6, 58, 19]
# no_swap = False
# top = len(my_list) 
# while no_swap == False and top > 0:
#     no_swap = True
#     for index in range(top - 1):
#         if my_list[index] > my_list[index+1]:
#             temp = my_list[index]
#             my_list[index] = my_list[index+1]
#             my_list[index+1] = temp
#             no_swap = False
#     top = top - 1

# print(my_list)

## The above code is correct

# #Insertion sort

# my_list = [7, 23, 1, 45, 12, 89, 34, 6, 58, 19]
# upper_bound = len(my_list)
# lower_bound = 0
# for index in range(lower_bound+1,upper_bound):
#     key = my_list[index]
#     place = index - 1
#     if my_list[place] > key:
#         while place >= lower_bound and my_list[place] > key:
#             temp = my_list[place+1]
#             my_list[place+1] = my_list[place]
#             my_list[place]= temp
#             place = place -1
#         my_list[place+1] = key
# print(my_list)

## The above code is correct

# #Stack

# stack = ["" for index in range(10)]
# top_pointer = -1
# base_pointer = -1
# stack_full = 10
# items = ""

# def push(item):
#     global top_pointer
#     if top_pointer < len(stack) - 1 :#stack_full -1:
#         top_pointer = top_pointer + 1
#         stack[top_pointer] = item
#     else:
#         print("Stack is full") 

# def pop():
#     global top_pointer,base_pointer,items
#     if top_pointer == base_pointer :
#         print("Stack is empty")
#     else:
#         items = stack[top_pointer]
#         top_pointer = top_pointer -1

# pop()
# push("shaher")
# push("shaher1")
# push("shaher2")
# push("shaher3")
# push("shaher4")
# pop()
# push("shaher5")
# push("shaher6")
# push("shaher7")
# push("shaher8")
# push("shaher")
# pop()
# push("shaher9")
# pop()
# push("shaher10")
# pop()
# pop()
# push("shaher11")
# pop()
# push("shaher12")
# push("shaher13")
# pop()
# pop()
# push("shaher14")
# print(my_list)

## The above code is correct

# #Queue

# queue = ["" for index in range(10)]
# front_pointer = 0
# rear_pointer = -1
# queue_full = 10
# queue_length = 0
# item = ""

# def enqueue(item):
#     global queue_length, rear_pointer
#     if queue_length < queue_full:
#         if rear_pointer < len(queue) -1:
#             rear_pointer+=1
#         else:
#             rear_pointer = 0
#         queue_length+=1
#         queue[rear_pointer] = item
#     else:
#         print("Queue is full cant enqueue 😭😭")

# def dequeue():
#     global queue_length,front_pointer,item
#     if queue_length == 0:
#         print("Queue is empty  cant dequeue 😭😭")
#     else:
#         item = queue[front_pointer]
#         if front_pointer == len(queue) - 1:
#             front_pointer = 0
#         else:
#             front_pointer+=1
#         queue_length-=1

# enqueue("shaheer1")
# enqueue("shaheer2")
# enqueue("shaheer3")
# enqueue("shaheer4")
# enqueue("shaheer5")
# enqueue("shaheer6")
# dequeue()
# enqueue("shaheer7")
# enqueue("shaheer8")
# enqueue("shaheer9")
# enqueue("shaheer10")
# dequeue()
# enqueue("shaheer11")

## The above code is correct

# Linked list Searching 

myLinkedList = [42, 17, 89, 34, 56, 12, 77, 23, 91, 45, 68, 10]
myLinkedListPointers = [-1, 0, 1, 2, 3, 6, 7, 8, 9, 10, 11, -1]
startPointer = 11
nullPointer = -1

def find(itemSearch):
    found = False
    itemPointer = startPointer
    while itemPointer != nullPointer and not found:
        if myLinkedList[itemPointer] == itemSearch:
            found = True
        else:
            itemPointer = myLinkedListPointers[itemPointer]
    return itemPointer

# Enter item to search for
item = int(input("Please enter item to be found: "))
result = find(item)
if result != -1:
        print("Item found")
else:
    print("Item not found")