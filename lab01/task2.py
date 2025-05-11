test_case=int(input())
for i in range(test_case):
    string1,num1,operation,num2=input().split()
    first_num=int( num1)
    second_num=int(num2)
    if operation=="+":
        result=(first_num+second_num)
    if operation=="-":
        result=(first_num-second_num)
    if operation=="*":
        result=(first_num*second_num)
    if operation=="/":
        result=(first_num/second_num)
    print(round(result,6))