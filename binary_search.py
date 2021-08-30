def binary_search(list,target):
    first=0
    last=len(list)-1 #constant time

    while first <= last:
        midpoint = (first+last)//2 #if there is an odd number, "//" calculates the nearest whoole number
        if list[midpoint]==target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint+1
        else:
            last=midpoint-1
    return None

def verify(index):
    if index is not None:
        print("target found at ", index)
    else:
        print("bummer")


numbers=[1,4,5,6,7,12]
result=binary_search(numbers,12)
verify(result)