searchname = input("Enter name to search: ").upper()
found = False

myFile = open("TP25.txt", "r")

info = myFile.readline().strip()

while info != "" and found == False:
    studentID, name, age, gender = info.split()
    if searchname == name:
        print(studentID, name, age, gender)
        found = True
    else:
        info = myFile.readline().strip()

if found == False:
    print("Name not found.")
myFile.close()


myFile = open("TP25.txt", "r")

info = myFile.readline().strip()        # strip elininates any unecessary characters such as \n. Eliinating \n allows the output to have no space lines 

while info != "":
    studentID, name, age, gender = info.split()         # split checks for the first space and splits the words into seprate variables 
    print(studentID, name)
    info = myFile.readline().strip()

myFile.close()





