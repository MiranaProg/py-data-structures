import array
def reverse(arr,start,end):
    while start < end:
        temp = arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        start+=1
        end-=1


def display():
    for items in arr:
        print(items,end=' ')

arr = array.array('i',[2,4,1,5,6,3,8,])
d = 3
n = len(arr)

reverse(arr,0,d-1)
reverse(arr,d,n-1)
reverse(arr,0,n-1)

print('array after rotation:\n')
display()
