#zad 7
list=[2,1,3,7]

def foo(list):
    return tuple(list)

a=foo(list)
print(a)
print(type(a))

#zad 8 oddzielny skrypt

#zad 9

def day(a):
    days={1: "poniedzialek",
          2: "wtorek",
          3: "sroda",
          4: "czwartek",
          5: "piatek",
          6: "sobota",
          7: "niedizela"}
    return days[a]

print(day(1))


#zad 10

a="kajak"
def palindrom(string):
    a=len(string)-1
    for i in range(len(string)):
        if string[i] != string[a-i]:
            return False
    return True

print(palindrom(a))










