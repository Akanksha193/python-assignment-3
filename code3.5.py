x = [3,5,4,6,8,10,20,3,7,9,32,67]
z = []
for item in x:
    if item%2==0:
        print('even number')
    else:
        z.append(item)
print(z)