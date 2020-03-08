def func1(world):
    print('hello', world)

prac = func1('python')
print(prac)

def fun2(world):
    val = 'hello' + str(world)
    return(val)
stt = fun2('python')
print(stt)

def fun3(x):
    y1 = x*100
    y2 = x*200
    y3 = x*300
    return[y1, y2, y3]
tuple_1 = fun3(2)
print(tuple_1)

def args_func(*args):
    for i, v in enumerate(args):
        print(i,v)
    # for t in args:
    #     print(t)

args_func('kim','park','lee')

def kw_func(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

kw_func(name1='kim',name2='lee',name3='park')

la_ex = lambda num: num+10
print(la_ex(10))

def fun_final(x,y,func):
    print(x+y+func(12))

fun_final(10,11,lambda x:x + 12)