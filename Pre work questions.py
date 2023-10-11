# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
# The first line of the code has been defined as below.

#     def hello_name(user_name):
def hello_name(user_name):
    """write a greeting that prints username"""
    user_name = input('Please type in your username:')
    return user_name

users_name = hello_name('')
print('Hello, ' + users_name + '!')



print('\n')
# # Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

#     def first_odds():

def first_odds():
    for num in range(1, 101, 2):
        print(num)

first_odds()



print('\n')
# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below.

#     def max_num_in_list(a_list):

def max_num_in_list(a_list):
    if max_num_in_list:
        return max(a_list)

a_list = [21, 32, 34, 83]
max_number = max_num_in_list(a_list)
print(f'the max number is {max_number}')



print('\n')
# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, 
# but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

#     def is_leap_year(a_year):

def is_leap_year(a_year):
    if (a_year % 4 == 0 and a_year % 100 !=0) or (a_year % 400 == 0):
        return True
    else:
        return False
    
a_year = 2023
leap = is_leap_year(a_year)
print("Is " + str(a_year) +  " a leap year?")
print(leap)



print('\n')
# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.

#     def is_consecutive(a_list):

def is_consecutive(a_list):
    if not a_list:
        return False
    for i in range(1, len(a_list)):
        if a_list[i] != a_list[i-1] + 1:
            return False
    return True

list_0 = [2, 3, 4, 5, 6, 7]
list_1 = [1, 2, 4, 5]
print(is_consecutive(list_0))
print(is_consecutive(list_1))

