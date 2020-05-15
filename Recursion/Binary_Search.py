def Binary_Search(arr,target):
	return Bin_Srch(arr,0,len(arr)-1,target)
def Bin_Srch(arr,st,end,trgt):
	mid=(st+end)//2
	if(st>end):
		return -1
	elif(arr[mid]==trgt):
		return mid
	else:
		if(trgt<arr[mid]):
			return(Bin_Srch(arr,st,mid-1,trgt))
		else:
			return(Bin_Srch(arr,mid+1,end,trgt))
print(Binary_Search([1,2,3,4,5,6,7,8,9,10],8))