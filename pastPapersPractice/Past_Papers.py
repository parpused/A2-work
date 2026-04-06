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

ArrayNodes = [[-1 for x in range(3)] for y  in range(20)]
FreeNode = 6
RootPointer = 0
ArrayNodes = [[1,20,5],[2,15,-1],[-1,3,3],[-1,9,4],[-1,10,-1],[-1,58,-1]]


def SearchValue(RootPointer,ValueToFind):
    if RootPointer == -1:
        return -1
    else:
        if ArrayNodes[RootPointer][1] == ValueToFind:
            return RootPointer
        if ArrayNodes[RootPointer][1] > ValueToFind:
            return SearchValue(ArrayNodes[RootPointer][0], ValueToFind)
        if ArrayNodes[RootPointer][1] < ValueToFind:
            return SearchValue(ArrayNodes[RootPointer][2], ValueToFind)

def PostOrder(RootPointer):
    if ArrayNodes[RootPointer][0] != -1:
        PostOrder(ArrayNodes[RootPointer][0])
    print(str(ArrayNodes[RootPointer][1]))
    if ArrayNodes[RootPointer][2] != -1:
        PostOrder(ArrayNodes[RootPointer][2])

# main program
returnValue = SearchValue(RootPointer,15)
if returnValue == -1:
    print("Not  Found")
else:
    print("Found at " + str(returnValue))

PostOrder(RootPointer)