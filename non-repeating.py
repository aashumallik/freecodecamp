arr = [1,1,1,2]
mydict={}
for i in arr:
    if(i in mydict):
        mydict[i]=mydict[i]+1
    else:
        mydict[i]=1
for key in mydict:
    if(mydict[key]==1):
        print(key)
        break