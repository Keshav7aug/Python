def fact(N):
    if N<1:
        return -1
    elif N==1:
        return 1
    else:
        return N*fact(N-1)
N=int(input())
while N>0:
    A=int(input())
    print(fact(A))
    N-=1