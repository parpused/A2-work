class Students:
    # PRIVATE StudentID : STRING
    # PRIVATE Name : STRING
    # PRIVATE Age : INTEGER
    # Setter
    def __init__(self):
        self.__StudentID = ""
        self.__Name = ""
        self.__Age = 0
    def SetID(self, ID):
        self.__StudentID = ID
    def SetName(self, na):
        self.__Name = na
    def SetAge(self, Ag):
        self.__Age = Ag
    # Getter
    def GetID(self):
        return self.__StudentID
    def GetName(self):
        return self.__Name
    def GetAge(self):
        return self.__Age
    # Display    
    def display(self):
        print("StudentID: ",self.__StudentID)
        print("Name: ",self.__Name)
        print("Age: ",self.__Age)

# MyStudent = Students()
# MyStudent.SetID("MR1001")
# MyStudent.SetName("SHAHEER")
# MyStudent.SetAge(18)
# MyStudent.display()


class Subjects(Students):
    # PRIVATE Sub1
    # PRIVATE Sub2
    # PRIVATE Sub3

    def __init__(self):
        super().__init__()
        self.__Sub1 = 0
        self.__Sub2 = 0
        self.__Sub3 = 0

    def SetSubjects(self,s1,s2,s3):
        self.__Sub1 = s1
        self.__Sub2 = s2
        self.__Sub3 = s3

    def GetSub1(self):
        return self.__Sub1
    def GetSub2(self):
        return self.__Sub2
    def GetSub3(self):
        return self.__Sub3

    def display(self):
        super().display()
        print("1st subject: ", self.__Sub1)
        print("2nd subject: ", self.__Sub2)
        print("3rd subject: ", self.__Sub3)

MyStudent = Subjects()
MyStudent.SetID("MR1001")
MyStudent.SetName("SHAHEER")
MyStudent.SetAge(18)
MyStudent.SetSubjects(123,456,789)
MyStudent.display()
