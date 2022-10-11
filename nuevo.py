dct = {'uno':'dos', 'tres':'uno' , 'dos':'tres'}
v = dct['tres']
#for k in range (len(dct)):
 #   v = dct[v]
#print (v)

lst=[i for i in range(-1, -2)]
print (len(lst))

def fun (x,y):
    if x == y:
        return x
    else:
        return fun(x, y-1) 
print (fun(0,3))

#dd= {"1":"0", "0":"1"}
#for x in dd.vals():
 #   print(x, end="")

lst=[1,2]
for v in range(2):
    lst.insert(-1,lst[v])

print(lst)
a=1
b=0
a= a^b
b= a^b
a= a^b
print(a,b)

tup=(1,2,4,8)
tup=tup[-2:-1]
tup[-1]
print(tup)

dct={}
dct['1']=(1,2)
dct['2']=(2,1)

for x in dct.keys():
    print(dct[x][1],end="")

lst=[[x for x in range(3)] for y in range (3)]
for r in range(3):
    for c in range (3):
        if lst[r][c] %2 != 0:
            print("#")
