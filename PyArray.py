#program ot rotate array by distance d
import  array
def rotate_array(arr,d,n):
    print('before rotation')
    for i in arr:
        print(i, end=' ')

    for i in range(d):
           pop_ele=arr.pop(0)
           arr.append(pop_ele)


    print('\nafter rotation')
    for i in arr:
        print(i,end=' ')



arr=array.array('i',[1,2,3,4,5])
n=len(arr)
d=int(input('enter distance to rotate'))

rotate_array(arr,d,n)
