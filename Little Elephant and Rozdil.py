n=int(input())
time_req=list(map(int,input().split()))
min_time_req=min(time_req)
if time_req.count(min_time_req)>=2:
    print("Still Rozdil")
else:
    a=time_req.index(min_time_req)
    print(a+1)