def max_sum_subarray(ls):
    max_sum=0
    for i in ls:
        max_sum+=i
    for i in range(len(ls)):
        sum=ls[i]
        for j in range(i+1,len(ls)):
            sum+=ls[j]
            if(sum>max_sum):
                max_sum=sum
    return max_sum


