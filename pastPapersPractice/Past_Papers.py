



































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