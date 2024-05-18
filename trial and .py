s=input()
my_dict=["A","E","I,","O","U","Y"]
i,j=0,1
_max=0
s="A"+s+"A"
while j<len(s):
    if s[i] in my_dict:
        if s[j] not in my_dict:
            j+=1
        else:
            _max=max(_max,j-i)
            i=j
            j+=1
    else:
        i+=1
        j+=1
print(_max)

