test_cases = int(input())
for _ in range(test_cases):
    length = int(input())
    string = str(input())
    print('here is the matrix:')
    ans = "Yes"
    if length ** 0.5 != int(length**0.5):
        ans = "No"
    else:
        r = int(length ** 0.5)
        for i in range(0,length,r):
            line = string[i:i+r]
            print(line)
            if i == 0 or i ==  length - r:
                if line != '1'* r:
                    ans = "No"
            else:
                if line != ('1'+ '0'*(r-2) + '1'):
                    ans = "No"
    print("-----------")
    print("The answer is:")
    print(ans)


        
