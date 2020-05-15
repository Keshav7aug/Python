def deep_rev(L):
	for i in range(len(L)):
		if(isinstance(L[i],(list))==True):
			L[i] = deep_rev(L[i])
	return L[::-1]
				
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = deep_rev(arr)
    if output == solution:
        print("Pass")
    else:
        print("False")
		
arr = [1, 2, 3, 4, 5]
solution = [5, 4, 3, 2, 1]
test_case = [arr, solution]
test_function(test_case)
arr = [1, 2, [3, 4, 5], 4, 5]
solution = [5, 4, [5, 4, 3], 2, 1]
test_case = [arr, solution]
test_function(test_case)

arr = [1, [2, 3, [4, [5, 6]]]]
solution = [[[[6, 5], 4], 3, 2], 1]
test_case = [arr, solution]
test_function(test_case)

arr =  [1, [2,3], 4, [5,6]]
solution = [ [6,5], 4, [3, 2], 1]
test_case = [arr, solution]
test_function(test_case)