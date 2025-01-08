# #addition and deletion happens from same end
# #array implementation of stack
# stack=[]
# top=-1
# def push(item):#since its dynamic,no overflow
#     stack.append(item)
#     top=len(stack)-1
#     print(stack)

# def pop():
#     if top==-1:
#         return print("stack empty,underflow")
#     print(f"element to be deleted is : {stack[top]}")
#     stack.pop(top)
#     print(stack)

# def traverse():
#     for num in stack:
#         print(num)
# while(True):
#     print(''' methods:
#     1.push
#     2.pop
#     3.traverse
#     4.exit''')

#     val=int(input("choose a value"))
#     match val:
#         case 1:
#             num=input("enter a value")
#             push(num)
#         case 2:
#             pop()
#         case 3:
#             traverse()
#         case 4:
#             exit(0)

#sll implementation
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class stack:
    def __init__(self):
        self.head=None
        self.size=0

    def push(self,val):#insert in the beginning
        self.size+=1
        newNode=Node(val)
        if self.head==None:
            self.head=newNode
            return
        newNode.next=self.head
        self.head=newNode
        

    def pop(self):#delete from the beginning
        if self.size==0:
            print("stack empty")
            return
        print("element to be popped is : ",self.head.value)
        curr=self.head
        self.head=self.head.next
        curr.next=None
        self.size-=1

    def traverse(self):
        if self.head==None:
            print("list empty")
        else:
            curr=self.head
            while(curr):
                print(f"{curr.value}->",end=" ")
                curr=curr.next
            print(None)

st=stack()
st.push(9)
st.push(8)
st.push(7)
st.push(6)
st.push(5)
st.traverse()
st.pop()
st.traverse()
st.pop()
st.pop()
st.push(10)
st.traverse()

