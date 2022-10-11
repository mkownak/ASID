list=[]

n=int(input("ile chcesz wpisac wartosci do tablicy: "))

i=0
while i<n:
    a=int(input(f"podaj element na indeksie {i}: "))
    list.append(a)
    i=i+1

list=tuple(list)
print(list)