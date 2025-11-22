#DECLARE my_list : ARRAY [0:4] OF STRING
my_list = ["" for i in range(5)]
head = -1
tail = -1

def display():
    global my_list,head,tail
    for i in range(5):
        print(i,my_list[i])
    print("Head",head,"Tail",tail)

def enqueue(new_item):
    global my_list,head,tail
    if (head == 0 and tail == 4) or (head == tail+1):
        print("FULL")
    else:
        if head == -1 and tail == -1:
            head   = 0 
            tail = 0
        elif tail == 4:
            tail = 0
        else:
            tail +=1
        my_list[tail] = new_item
        print("ENQUEUE")

def dequeue():
    global my_list,head,tail
    if head == -1 and tail == -1:
        print("EMPTY")
    else:
        if head == tail:
            head = -1
            tail = -1
        elif head == 4:
            head ==0
        else:
            head +=1 

enqueue("Q")
enqueue("E")
enqueue("H")
dequeue()
enqueue("J")
enqueue("L")
dequeue()
enqueue("F")
enqueue("R")
dequeue()
dequeue()
enqueue("l")
enqueue("d")
dequeue()
enqueue("b")


display()