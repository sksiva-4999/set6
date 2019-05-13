k,n=map(int,input().split())
arr=list(map(int,input().split()))
for i in range(0,k):
    if(arr[i]==n):
        print("yes")
        break
else:
    print("no")
