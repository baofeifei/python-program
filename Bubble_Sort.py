#coding:utf-8
def BubbleSort(lst):
    size = len(lst)
    for i in range(size):
        for n in range(i+1,size):
            if lst[i] > lst[n]:
                lst[i],lst[n] = lst[n],lst[i]
    return lst

if __name__ == "__main__":
    lst = [8,9,5,7,17,15,82,73,47,56]
    print BubbleSort(lst)
#原理：lst[i]与后面每一项即lst[i+1:]进行比较，把最小的放到前面，i从0变化到len(lst)
#全部刚好比对完，完成排序。如果从大到小排序那那就是lst[i]>lst[n]
