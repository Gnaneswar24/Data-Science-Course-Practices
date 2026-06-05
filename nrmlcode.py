import sys
print("hello World")
s="1234"
name_int=int(s)
print(name_int)
q=10.00
w=10.000
t="string"
j=2+1j
r=int(q)
print(r)
print(r,"is r is the integer?",isinstance(r,int))
print(q,"is q is the integer?",isinstance(q,int))
print(sys.getsizeof(q))
print(sys.getsizeof(r))
print(sys.getsizeof(t))
print(sys.getsizeof(j))
print(id(r))
print(id(q))
print(id(t))
print(id(j))
print(r,q,t,j)