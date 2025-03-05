class Node:
    def __init__(self,data):
        self.data = data
        self.Next= None
def Travecal_Linkelist(data):
    corrnent = data
    while corrnent is not None:
        print(corrnent.data)
        corrnent=corrnent.Next
    return
def Scarch_LinkList(head,key):
    carent =head
    while carent is not None:
        if carent.data ==key:
            return True
        carent = carent.Next
    else:
        return False
def lenght(head):
    count = []
    carent = head
    while carent is not None:
        count.append(carent.data)
        carent = carent.Next
    return len(count)
def Insert(head,New_data):
    new_node = Node(New_data)
    new_node.Next = head
    return New_data
def Insert_end(head,New_data):
    new_node = Node(New_data)
    if head is None:
        return new_node
    last = head
    while last.Next:
        last = last.Next 
        last.Next = new_node
    return head
if __name__ =="__main__":
    head = Node(10)
    head.Next = Node(20)
    head.Next.Next =Node(30)
    head.Next.Next.Next = Node(40) 
result = Travecal_Linkelist(head)
print(result , end=" ")
key =20
if Scarch_LinkList(head,key):
    print(f"Yes: Persent in element linkelist {key}")
else:
    print("NO")
#lenghts = lenght(head)
#print(lenghts)
#New_data =5
#Insert_linklist = Insert(head,New_data)
#print(Insert_linklist)
New_data =  50
last_Insert = Insert_end(head,New_data)
print(last_Insert)
result = Travecal_Linkelist(head)
print(result , end=" ")