def nth_row_pascal(n):
    if(n==0):
        return [1]
    else:
        A=[1]
        B=nth_row_pascal(n-1)
        for a in range(len(B)-1):
            A.append(B[a]+B[a+1])
        A.append(1)
        return A
def print_space(n):
    for i in range(n):
        print(' ',end=' ')
        
a=int(input())
print(nth_row_pascal(a))

