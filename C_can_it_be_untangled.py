
s=input().strip()
st=[]

for c in s:
    if not st:
        st.append(c)
        continue
    if st[-1]==c:
        st.pop()
    else:
        st.append(c)
if not st:
    print("Yes")
else:
    print("No")