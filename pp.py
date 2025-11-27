# # Question 1

# # #DECLARE arrayData : ARRAY [0:9] OF INTEGER

# arrayData = [10,5,6,7,1,12,13,15,21,8]

# def linerSearch(num):
#     global arrayData
#     index = 0
#     while index < 10:
#         if num == arrayData[index]:
#             return True
#         else:
#             index +=1
#     return False

# x = linerSearch(int(input("Enter a value to search: ")))
# if x == True:
#     print("Number found...")
# else:
#     print("Number not found...")

# def bubbleSort():
#     global arrayData
#     for x in range(0,len(arrayData) - 1):
#         for y in range(0,len(arrayData) - 1):
#             if arrayData[y] < arrayData[y+1]:
#                 temp = arrayData[y]
#                 arrayData[y] = arrayData[y+1]
#                 arrayData[y+1] = temp
    
# bubbleSort()
# print(arrayData)

# question 2

#DECLARE Animals : ARRAY [0:9] OF STRING

Animals = ["" for index in range(10)]
Animals = ["horse", "lion", "rabbit", "mouse", "bird", "deer", "whale", "eleplant", "kangaro","tiger" ]


def sortDecending():
    global Animals
    ArrayLength = len(Animals)
    for x in range(0,ArrayLength - 1):
        for y in range(0,ArrayLength- x - 1):
            if Animals[y][0:1] < Animals[y+1][0:1]:
                temp = Animals[y]
                Animals[y] = Animals[y+1]
                Animals[y+1] = temp
    
sortDecending()
for index in range(10):
    print(Animals[index])