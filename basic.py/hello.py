s="madam is a word"
res=""
print(s[1:-1])
print(s[-5:])
print("reverse " +s[:-5])

s1="23 3 1 5 6"
l1=s1.split(" ")
l2=[]
print(l1)
for i in range(0,len(l1)):
    l2.append(int(l1[i]))
print(l2)

print(l2.insert(0,100))
print(l2)
del l2[::2]
print(l2)

s="geeks 24 11"
l1=s.split(" ")
print(l1)

print(5 and 6)