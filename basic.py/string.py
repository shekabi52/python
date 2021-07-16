s="100shjk2345daso"
s1=""
max=0
for i in range(0,len(s)):
    if(s[i].isdigit()):
        s1+=s[i]
    else:
        if(int(s1)>max):
            max=int(s1)
        s1="0"

if(int(s1)>max):
    max=int(s1)

print(max)
