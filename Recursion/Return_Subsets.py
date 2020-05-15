def all_Subsets(ls):
    Ans=[]
    if(len(ls)<=1):
        Ans=[ls]
    else:
        for i in range(len(ls)):
            if [ls[i]] not in Ans:
                Ans.append([ls[i]])
            j=i+1
            if j<len(ls):
                sme=all_Subsets(ls[j:])
                for k in sme:
                    k.insert(0,ls[i])
                    if k not in Ans:
                        Ans.append(k)
    return Ans

def subsets(ls):
    Ans=[[]]
    Ans.append(all_Subsets(ls))
    return Ans
    
for a in subsets('abcde'):
    print(a)