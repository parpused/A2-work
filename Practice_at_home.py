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

# myLinkedList = [42, 17, 89, 34, 56, 12, 77, 23, 91, 45, 68, 10]
# myLinkedListPointers = [-1, 0, 1, 2, 3, 6, 7, 8, 9, 10, 11, -1]
# startPointer = 11
# nullPointer = -1

# def find(itemSearch):
#     found = False
#     itemPointer = startPointer
#     while itemPointer != nullPointer and not found:
#         if myLinkedList[itemPointer] == itemSearch:
#             found = True
#         else:
#             itemPointer = myLinkedListPointers[itemPointer]
#     return itemPointer

# # Enter item to search for
# item = int(input("Please enter item to be found: "))
# result = find(item)
# if result != -1:
#         print("Item found")
# else:
#     print("Item not found")

# Past PastPapers
# def Unknown(x,y):
#     if x < y:
#         print(str(x+y))
#         return(Unknown(x+1,y) *2)
#     else:
#         if x == y:
#             return 1
#         else:
#             print(str(x+y))
#             return(int(Unknown(x-1,y)/2))

# def IterativeUnknown(x,y):
#     total = 1
#     while x != y :
#         print(str(x+y))
#         if x < y :
#             x = x+1
#             total*= 2
#         else:
#             x = x-1
#             total = int(total/2)
#     return total

# print("10,15")
# print(str(IterativeUnknown(10,15)))
# print("10,10")
# print(str(IterativeUnknown(10,10)))
# print("15,10")
# print(str(IterativeUnknown(15,10)))

# class Picture:
#     # PRIVATE description : STRING
#     # PRIVATE width : INTEGER
#     # PRIVATE height : INTEGER
#     # PRIVATE frameColor : STRING

#     def __init__(self, description_p, width_p, height_p, frameColor_p):
#         self.__description = description_p # STRING
#         self.__width = width_p # INTEGER
#         self.__height = height_p # INTEGER
#         self.__frameColor = frameColor_p # STRING

#     def GetDescription(self):
#         return self.__description
    
#     def GetHeight(self):
#         return self.__height
    
#     def GetWidth(self):
#         return self.__width
    
#     def GetColour(self):
#         return self.__frameColor

#     def SetDescription(self, newDescription):
#         self.__description = newDescription

# PictureArray = [Picture('',0,0,"") for i in range(100)]

# def ReadData(PictureArray):
#     file_name = r"F:\project\class\pastPapersPractice\Pictures.txt"
#     counter = 0
#     try:
#         file = open(file_name,"r")
#         description = (file.readline()).strip().lower()
#         while description != "":
#             width = int((file.readline()).strip())
#             height = int((file.readline()).strip())
#             frame = (file.readline()).strip().lower()
#             PictureArray[counter] = Picture(description,width,height,frame)
#             description = (file.readline()).strip().lower()
#             counter +=1
#         file.close()
#     except IOError:
#         print("Could not find the file")
#     return counter , PictureArray

# numberOfPicture, PictureArray = ReadData(PictureArray)

# frameColor = input("Enter the description: ").lower()
# max_Width = int(input("Enter the width: "))
# max_Height = int(input("Enter the height: "))
# print("Matches frame shown")
# for i in range(0, numberOfPicture):
#     if PictureArray[i].GetWidth()<= max_Width  and PictureArray[i].GetHeight() <= max_Height  and frameColor <= PictureArray[i].GetColour():
#         print(PictureArray[i].GetDescription(), str(PictureArray[i].GetWidth()), str(PictureArray[i].GetHeight()))

# arrayNode = [[0 for x in range(3)] for y in range(20)]
# rootPointer = -1
# freeNode = 0

# def addNode(arrayNode, rootPointer, freeNode):
#     nodeData = int(input("Enter the data: "))
#     if freeNode <= 19:
#         arrayNode[freeNode][0] = -1
#         arrayNode[freeNode][1] = nodeData
#         arrayNode[freeNode][2] = -1
#         if rootPointer == -1:
#             rootPointer = 0
#         else:
#             placed = False
#             currentNode = rootPointer
#             while placed == False:
#                 if nodeData < arrayNode[currentNode][1]:
#                     if arrayNode[currentNode][0] == -1:
#                         arrayNode[currentNode][0] = freeNode
#                         placed = True
#                     else:
#                         currentNode = arrayNode[currentNode][0]
#                 else:
#                     if arrayNode[currentNode][2] == -1:
#                         arrayNode[currentNode][2] = freeNode
#                         placed = True
#                     else:
#                         currentNode =  arrayNode[currentNode][2]
#         freeNode = freeNode +1
        
#     else:
#         print("Tree is full")
#     return arrayNode,rootPointer,freeNode
        
# def printAll(arrayNode):
#     for i in range(len(arrayNode)):
#         print(str(arrayNode[i][0])," ", str(arrayNode[i][1]), " ", str(arrayNode[i][2]))

# def inOrder(arrayNode, rootPointer):
#     if arrayNode[rootPointer][0] != -1:
#         inOrder(arrayNode,arrayNode[rootPointer][0])
#     print(str(arrayNode[rootPointer][1]))
#     if arrayNode[rootPointer][2] != -1:
#         inOrder(arrayNode,arrayNode[rootPointer][2])


# # main progaram
# for i in range(10):
#     arrayNode , rootPointer, freeNode = addNode(arrayNode , rootPointer, freeNode)
# printAll(arrayNode)
# inOrder(arrayNode,rootPointer)

# class node:
#     def __init__(self, theData, nextNodeNumber):
#         self.data = theData
#         self.nextNode = nextNodeNumber


# def outputNodes(linkedList,startPointer):
#     while startPointer != -1:
#         print(str(linkedList[startPointer].data))
#         startPointer = linkedList[startPointer].nextNode    
        
# def addNode(linkedList,startPointer,emptyList):
#     dataToAdd = int(input("Enter the data to add: "))
#     if emptyList == -1:
#         return False    
#     newNodeIndex = emptyList
#     emptyList = linkedList[emptyList].nextNode
#     linkedList[newNodeIndex] = node(dataToAdd,-1)
#     if startPointer == -1:
#         startPointer = newNodeIndex
#         return True
#     while linkedList[startPointer].nextNode != -1:
#         startPointer = linkedList[startPointer].nextNode
#     linkedList[startPointer].nextNode = newNodeIndex
#     return True
    
# linkedList = [node(1,1),node(5,4),node(6,7),node(7,-1),node(2,2),node(0,6),node(0,8),node(56,3),node(0,9),node(0,-1)]
# startPointer = 0
# emptyList = 5 

# outputNodes(linkedList,startPointer)
# returnValue = addNode(linkedList,startPointer,emptyList)
# if returnValue:
#     print("Item added successfully")
# else:
#     print("The list is full")
# outputNodes(linkedList,startPointer)

# DECLARE arrayData [0:10] ARRAY OF INTEGER


# def linearSearch(value):
#     for index in arrayData:
#         if index == value:
#             return True
#     return False

# def bubbleSort():
#     temp = 0
#     for x in range(0,10):
#         for y in range(0,9):
#             if theArray[y] < theArray[y+1]:
#                 temp = theArray[y]
#                 theArray[y+1] = temp
# 

# class treasureChest:
#     # PRIVATE question : STRING
#     # PRIVATE answer : INTEGER
#     # PRIVATE points : INTEGER
    
#     def __init__(self, questionP,answerP,pointsP):
#         self.__question = questionP
#         self.__answer = answerP
#         self.__points = pointsP
    
#     def getQuestion(self):
#         return self.__question

#     def checkAnswer(self,userAnswer):
#         if self.__answer == userAnswer:
#             return True
#         else:
#             return False

#     def getPoints(self, attempts):
#         if attempts == 1:
#             return self.__points
#         elif attempts == 2:
#             return self.__points // 2
#         elif attempts in (3,4):
#             return self.__points // 4
#         else:
#             return 0
    
# # arrayTreasure (5) TreasureChest
# arrayTreasure = []
# def readData():
#     arrayTreasure.clear()  
#     fileName = r"F:\project\class\pastPapersPractice\TreasureChestData.txt"
#     try:
#         file = open(fileName,"r")
#         dataFetched = (file.readline()).strip()
#         while dataFetched != "":
#             question = dataFetched
#             answer = int((file.readline()).strip())
#             points = int((file.readline()).strip())
#             arrayTreasure.append(treasureChest(question,answer,points))
#             dataFetched = (file.readline()).strip()
#         file.close()    
#     except IOError:
#         print("Could not find the file")


# readData()
# questionNumber = int(input("Enter the question number you want to attempt (1 to 5): "))
# if questionNumber <1 or questionNumber > 5:
#     print("Invalid choice")
# else:
#     print(arrayTreasure[questionNumber -1].getQuestion())
#     result = False
#     count = 0
#     while result == False:
#         answer = int(input("Enter your answer: "))
#         result = arrayTreasure[questionNumber-1].checkAnswer(answer)
#         count +=1   
#     print("The user has been awaded ",int(arrayTreasure[questionNumber-1].getPoints(count))," points")

# 9618/41/O/N/22

# Question 1

# DataArray = ["" for i in range(100)]

# def ReadFile ():
#     fileName = r"F:\project\class\pastPapersPractice\IntegerData.txt"
#     count = 0
#     try:
#         file = open(fileName,"r")
#         data = file.readline().strip()
#         while data != "":
#             DataArray[count] = data
#             count = count +1
#             data = file.readline().strip()
#         file.close()
#     except IOError:
#         print("File not found")

# def FindValues (DataArray):
#     search = int(input("Enter the number you want to search: "))
#     count = 0
#     if search >= 1 and search <= 100:
#         for i in range(len(DataArray)):
#             if  int(DataArray[i]) == search:
#                 count = count +1
#             else:
#                 continue   
#         return count
#     else:
#         return 0

# def BubbleSort(DataArray):
#     flag = True
#     while flag == True:
#         flag = False
#         for i in range(len(DataArray) - 1):
#             if int(DataArray[i]) > int(DataArray[i + 1]):
#                 temp = DataArray[i]
#                 DataArray[i] = DataArray[i + 1]
#                 DataArray[i + 1] = temp 
#                 flag = True
#     print(DataArray)            
# BubbleSort()

# # main program

# ReadFile()
# output = FindValues(DataArray)
# if output == 0 :
#     print("The integer doesnot exsists")
# else:
#     print("The integer appears ", output," times.")
# BubbleSort()


# Question 2

# class Card:
#     # PRIVATE number : INTEGER
#     # PRIVATE color : STRING

#     def __init__(self,number_P,color_P):
#         self.__number  = number_P
#         self.__color = color_P

#     def GetNumber(self):
#         return self.__number

#     def GetColor(self):
#         return self.__color

# oneRed = Card(1,"red")
# twoRed = Card(2,"red")
# threeRed = Card(3,"red")
# fourRed = Card(4,"red")
# fiveRed = Card(5,"red")

# oneBlue = Card(1,"blue")
# twoBlue = Card(2,"blue")
# threeBlue = Card(3,"blue")
# fourBlue = Card(4,"blue")
# fiveBlue = Card(5,"blue")

# oneYellow = Card(1,"yellow")
# twoYellow = Card(2,"yellow")
# threeYellow = Card(3,"yellow")
# fourYellow = Card(4,"yellow")
# fiveYellow = Card(5,"yellow")

# class Hand:
#     # PRIVATE  cards[10]: Card
#     # PRIVATE  firstCard : INTEGER
#     # PRIVATE  numberCards : INTEGER

#     def __init__(self,c1,c2,c3,c4,c5):
#         self.__cards = []
#         self.__cards.append(c1)
#         self.__cards.append(c2)
#         self.__cards.append(c3)
#         self.__cards.append(c4)
#         self.__cards.append(c5)
#         self.__firstCard = 0
#         self.__numberCards = 5

#     def GetCards(self,index):
#         return self.__cards[index]

# player_1 = Hand(oneRed,twoRed,threeRed,fourRed,oneYellow);
# player_2 = Hand(twoYellow,threeYellow,fourYellow,fiveYellow,oneBlue);

# def CalulateValue(player):
#     score = 0
#     for i in range(5):
#         card_val = player.GetCards(i)
#         score = score + card_val.GetNumber()
#         color = card_val.GetColor()
#         if color == "red":
#             score +=5
#         if color == "blue":
#             score+=10
#         if color == "yellow":
#             score+=15
#     return score

# # main program 

# if CalulateValue(player_1) == CalulateValue(player_2):
#     print("There is a draw")
# elif CalulateValue(player_1) > CalulateValue(player_2):
#     print("Player_1 is teh winner")
# else:
#     print("Player_2 is the winner")    

# Question 3

# ArrayNodes = [[-1 for x in range(3)] for y  in range(20)]
# FreeNode = 6
# RootPointer = 0
# ArrayNodes = [[1,20,5],[2,15,-1],[-1,3,3],[-1,9,4],[-1,10,-1],[-1,58,-1]]


# def SearchValue(RootPointer,ValueToFind):
#     if RootPointer == -1:
#         return -1
#     else:
#         if ArrayNodes[RootPointer][1] == ValueToFind:
#             return RootPointer
#         if ArrayNodes[RootPointer][1] > ValueToFind:
#             return SearchValue(ArrayNodes[RootPointer][0], ValueToFind)
#         if ArrayNodes[RootPointer][1] < ValueToFind:
#             return SearchValue(ArrayNodes[RootPointer][2], ValueToFind)

# def PostOrder(RootPointer):
#     if ArrayNodes[RootPointer][0] != -1:
#         PostOrder(ArrayNodes[RootPointer][0])
#     print(str(ArrayNodes[RootPointer][1]))
#     if ArrayNodes[RootPointer][2] != -1:
#         PostOrder(ArrayNodes[RootPointer][2])

# # main program
# returnValue = SearchValue(RootPointer,15)
# if returnValue == -1:
#     print("Not  Found")
# else:
#     print("Found at " + str(returnValue))

# PostOrder(RootPointer)