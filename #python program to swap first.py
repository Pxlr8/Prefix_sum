#python program to swap first
#and last element of the list

#swap function


from keyword import kwlist


def swaplist(newlist):
    size = len(newlist)

    # swapping
    temp = newlist[0]
    newlist[0] = newlist[size-1]
    newlist[size-1] = temp

    return newlist

#driver code
newlist = [12,34,4,56,32]

print(swaplist(newlist))