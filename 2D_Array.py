# my_data = "MR1001SHAHEER18M"

# student_id = my_data[:6]
# name = my_data[6:-3]
# age = my_data[-3:-1]
# gender = my_data[-1:]

# print(student_id)
# print(name)
# print(age)
# print(gender)

# my_list = [[0,0] for i in range(5)]
# for i in range(5):
#     student_id = int(input("Enter Student id: "))
#     marks = int(input("Enter Marks: "))

#     my_list[i][0] = student_id
#     my_list[i][1] = marks

# print(my_list)

my_list = [[1001,55],[1002,65],[1003,95],[1004,85],[1005,43]]

def liner_search(student_id):
    global my_list
    index = 0
    while index < 5:
        if student_id == my_list[index][0]:
            return my_list[index][1]
        else:
            index +=1
    return -1

student_id = int(input("Enter student id: "))
x=liner_search(student_id)
if x == -1:
    print("Student ID not found....")
else:
    print("Marks are",x)