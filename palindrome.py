"""
Author  : Vivek Shinde
Date    : 06/06/2020
purpose : Practice problem solving
code    : To take size of list as input & make corresponding list.To find whether number is palindrome.if yes
          print number or else print that numbers next palindrome
"""

user_input_test_case = int(input('Enter your number of test cases : '))
# Create an empty list to sore the elements in list one by one
mylist = []
for i in range(user_input_test_case):
    user_input_number = int(input('Enter number :'))

    # All the elements get added one by one as for loop gets repeated
    mylist.append(user_input_number)

for i in mylist:
    # convert int i to string for escaping from nonscriptable error
    reverse_str = str(i)[::-1]
    if str(i) == reverse_str:
        print(f'{i} is palindrome')
    else:
        # To store each(single) value of i in x when the for loop get repeated
        x = i
        while True:
            i = int(i) + 1
            reverse_str = str(i)[::-1]
            if str(i) == reverse_str:
                print(f'the next palindrome for {x} is {i} ')
                break





