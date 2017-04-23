#coding:utf8
def BinarySearch(lst,value):
    low,high = 0,len(lst)-1
    while(low < high):
        mid = (low + high)/2
        if lst[mid] < value:
            low = mid + 1
        elif lst[mid] > value:
            high = mid
        else:
            return mid
    return low if lst[low] == value else False


if __name__ == "__main__":
    lst = [1,2,3,4,5,6,7,8,9]
    print BinarySearch(lst,9)
#return Low if lst[Low] == value else False
#第一个作用为单数列的时候，直接进行判断，第二个作用当上面循环判断结束，还没查到，直接输出False
