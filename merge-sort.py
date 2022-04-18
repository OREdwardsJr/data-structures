#Iterative approach

a = [2, 8, 15, 18]
b = [5, 9, 12, 17]

def merge_fxn(list1: list, list2: list) -> list:
    if list1 == [] and list2 == []:
        return []
    elif list1 == []:
        return list2
    elif list2 == []:
        return list1
    else:
        output = []
        while list1 != [] and list2 != []:
            if list1[0] < list2[0]:
                output.append(list1.pop(0))
                if list1 == []:
                    return output + list2
            elif list2[0] < list1[0]:
                output.append(list2.pop(0))
                if list2 == []:
                    return output + list1
            else:
                output.append(list1.pop(0))
                list2.pop(0)

print(merge_fxn(a, b))   



#Recursive Approach
a = [2, 8, 15, 18, 25, 27, 39]
b = [5, 9, 12, 17]

def merge_fxn(list1: list, list2: list, output=[]) -> list:
    if list1 == [] and list2 == []:
        return output
    elif list1 == []:
        return output + list2
    elif list2 == []:
        return output + list1
    else:
        if list1[0] < list2[0]:
            output.append(list1.pop(0))
        elif list2[0] < list1[0]:
            output.append(list2.pop(0))
        else:
            output.append(list1.pop(0))
            list2.pop(0)
        return merge_fxn(list1, list2, output)

print(merge_fxn(a, b))   


#Merging more than 2 lists
'''
You need to find a way to capture when a list is empty. 
You tried indexing the empty list but and empty list isn't subscriptable. 
'''

a = [4, 6, 12, 10**4]
b = [3, 5, 9, 10**4]
c = [1, 10, 16, 10**4]
d = [2, 4, 8, 10**4]

def merge_multiple(list1: list, list2: list, list3: list, list4: list, output=[]) -> list:
    if len(list1 + list2 + list3 + list4) == 4:
        return output
    else:
        min_val = min(list1[0], list2[0], list3[0], list4[0])
        if (list1[0] == min_val):
            output.append(list1.pop(0))
        elif (list2[0] == min_val):
            output.append(list2.pop(0))
        elif (list3[0] == min_val):
            output.append(list3.pop(0))
        elif (list4[0] == min_val):
            output.append(list4.pop(0))
        else: 
            output.append(list4.pop(0))
        
        return merge_multiple(list1, list2, list3, list4, output)

print(merge_multiple(a, b, c, d))
