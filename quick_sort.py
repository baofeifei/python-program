def qsort(lst):
    if lst == []:
        return []
    else:
        mid = lst[0]
        little = qsort([x for x in lst[1:] if x < mid])
        big = qsort([x for x in lst[1:] if x > mid])
        return little + [mid] + big


if __name__ == "__main__":
    lst = [-9,8,-100,-73,9,11,-5,72,89,65]
    print qsort(lst)
