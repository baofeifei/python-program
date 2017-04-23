def lstsperad(lst):
    for item in lst:
        if isinstance(item,list):
            for item1 in lstsperad(item):
                yield item1
        else:
            yield item

if __name__ == "__main__":
    lst = [1,[2,[3,[4]]]]
    for i in lstsperad(lst):
        print i
    print list(lstsperad(lst))
