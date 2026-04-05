# Python Challenge Day 9

# Write a program to implement a menu-driven stack using list.


stack=[]

def push():
    value=int(input("Enter value: "))
    stack.append(value)
    print("Pushed:", value)

def pop():
    if len(stack)== 0:
        print("Stack is empty")
    else:
        print("Popped:", stack.pop())

def peek():
    if len(stack)==0:
        print("Stack is empty")
    else:
        print("Top element:" ,stack[-1])

def display():
    if len(stack)==0:
        print("Stack is empty")
    else:
        print("Stack: ", stack)

while True:
    print("\n ---Stack Menu---")
    print("1.  Push")
    print("2.  Pop")
    print("3. Peek")
    print("4  Display")
    print("5.  Exit")

    choice= int(input("Enter Choice: "))

    if choice == 1:
        push()
    elif choice ==2:
        pop()
    elif choice==3:
        peek()
    elif choice ==4:
        display()
    elif choice ==5:
        print("Exiting")
        break
    else:
        print("Invaild Choice")
