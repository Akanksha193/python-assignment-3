a={1:10,2:20}
b={3:30,4:40}
c={}
for d in (a,b): c.update(d)
print(c)