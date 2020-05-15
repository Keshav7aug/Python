def Reverse(s):
    if(len(s)==0):
        return ''
    else:
        return Reverse(s[1:])+s[0]
A=input()
print(Reverse(A))