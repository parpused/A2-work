# DECLARE my_list : ARRAY [0:4] OF STRING
my_list = ["" for i in range(5)]
tos = -1

def push(new_item):
    global my_list,tos
    if tos == 4:
        print("FULL")
    else:
        tos+=1
        my_list[tos]= new_item
        print("PUSHED")

def pop():
    global my_list,tos
    if tos == -1:
        print("EMPTY")
    else:
        my_list[tos]= ""
        tos-=1
        print("POPPED")


def display():
    global my_list,tos
    for i in range(5):
        print(i,my_list[i])
    print("Top of the stack",tos)


push("A")
push("B")
push("C")
pop()
push("D")
push("E")
push("F")
pop()
push("E")
push("E")
push("E")
pop
push("E")
push("E")


display()
print(my_list)


