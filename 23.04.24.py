def find_x(list1):
    for i in range (len(list1)):
        if list1[i]==6:
            return i

print(find_x([1,3,4,5,6,8]))



def find_ss(list2):
    i=0
    for a in list2:
        if a ==6:
            return i
        i+=1
print(find_ss([1,6,3,4,5,8]))
