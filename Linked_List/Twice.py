def duplicate_number(nmb):
    for i in range(len(nmb)):
        nmb[i]=nmb[i]+1
       #print()
       
    for i in nmb:
        if(nmb[abs(i)]<0):
            return ((abs(i))-1)
        else:
            nmb[abs(i)]=-1*nmb[abs(i)]
    return None
arr = [0, 0]
solution = 0

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    output = duplicate_number(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")
arr = [0, 0]
solution = 0

test_case = [arr, solution]
test_function(test_case)

arr = [0, 2, 3, 1, 4, 5, 3]

solution = 3

test_case = [arr, solution]
test_function(test_case)

arr = [0, 1, 5, 4, 3, 2, 0]
solution = 0

test_case = [arr, solution]
test_function(test_case)

arr = [0, 1, 5, 5, 3, 2, 4]
solution = 5

test_case = [arr, solution]
test_function(test_case)