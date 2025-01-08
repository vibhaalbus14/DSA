# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#-------------------approach1------------brute force-----------------
#time compexity:O((nXm)
#space complexity:O(max(n,m)
# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         def traverse(head):
#             curr=head
#             val=""
#             while curr!=None:
#                 val+=str(curr.val)
#             return val[::-1]
#         v1=int(traverse(l1))
#         v2=int(traverse(l2))
#         v=v1+v2
#         #create a list in rev order
#         v=str(v)[::-1]
#         #node creation
#         nodes=[]
#         for i in range(len(v)):
#             nodes.append(ListNode(int(v[i])))
#         #ll direction assignment
#         for i in range(len(nodes)-1):
#             nodes[i].next=nodes(i+1)
#         head=nodes[0]
#         return head

#     # def listTraversal(self,head):
#     #         curr=head
#     #         while curr!=None:
#     #             print(f"{curr.val} ->",end="")
#     #         print()
#     #         print("list traversal completed")

#----------------2 pointers approach--------------------------
#time compexity:O(max(n,m)
#space complexity:O(max(n,m)
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        ptr1=l1
        ptr2=l2
        nodes=[]
        val=0
        while ptr1!=None and ptr2!=None:
            res=ptr1.val+ptr2.val+val
            nodes.append(ListNode(res%10)) #units place
            val=res//10 #tens place
            ptr1=ptr1.next
            ptr2=ptr2.next 

        if ptr1==None and ptr2!=None:
            while ptr2!=None:
                res=ptr2.val+val
                nodes.append(ListNode(res%10)) #units place
                val=res//10 #tens place
                ptr2=ptr2.next 
        else:
            if ptr1!=None and ptr2==None:
                while ptr1!=None:
                    res=ptr1.val+val
                    nodes.append(ListNode(res%10)) #units place
                    val=res//10 #tens place
                    ptr1=ptr1.next 
        
        if val!=0:
            nodes.append(ListNode(val))
        
        #linking the nodes
        for i in range(len(nodes)-1):
            nodes[i].next=nodes[i+1]
        head=nodes[0]
        return head




        


# object=Solution()
# print(object.addTwoNumbers(l1,l2))