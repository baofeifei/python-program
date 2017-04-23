#coding:utf-8
def step(max):
    a,b,n= 0,1,0
    while n < max:
        yield b
        a,b = b,a+b
        n = n + 1

if __name__ == "__main__":
    print list(step(10))
#原理走台阶有两种方法，一个是一次走一步，一个是一次走两步：因为走上第10级台阶有两种方法，一种是第8级台阶跨2步，一种是
#第9级台阶跨一步，所以跨上第10级台阶的方法有2方法加起来。
#所以 B = A + B 
