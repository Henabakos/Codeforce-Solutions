t=int(input())
ax,ay,az=[],[],[]
for i in range(t):
    x,y,z=map(int,input().split())
    ax.append(x)
    ay.append(y)
    az.append(z)
if sum(ax)==0 and sum(ay)==0 and sum(az)==0:
    print("YES")
else:
    print("NO")