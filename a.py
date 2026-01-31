def numLen(num):
    len=0
    while(num>0):
        num=num//10
        len+=1
    return len

def replaceElLen(arr):
    
    for i in range(len(arr)):
        arr[i] = numLen(arr[i])
    
    return arr

arr=[12,7,321,11,7080]

print(replaceElLen(arr))

    