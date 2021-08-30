def linear_search(list,target):
    for i in range(0, len(list)):
        if list[i]==target:
            return i
    return None
# Runs in linear time o(n)

def verify(index):
    if index is not None:
        print("target found at ", index)
    else:
        print("bummer")


numbers=[1,4,5,6,7,12]
result=linear_search(numbers,12)
verify(result)