print("hello world!")

#zad 1
def imienaz(a,b):
    return(a+"."+b)

a="M"
b="Kownacki"

print(imienaz(a,b))


#Zad 2

def foo(a,b):
    return(a[0].upper()+"."+b)

a="Michal"
b="Kownacki"

print(foo(a,b))


#Zad 3

def foo2(a,b,c):
    d=str(a)+str(b)
    d=int(d)
    return(d-c)

print(foo2(20,22,20))


#Zad 4

def foo3(a,b,foo):
    return foo(a,b)

print(foo3(a,b,foo))

#Zad 5

def foo4(a,b):
    if a>0 and b>0 and b!=0:
        return a/b

print(foo4(10,2))


#Zad 6 odzielny skrypt






