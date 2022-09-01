'''
Problem: Ask user to enter two numbers and then print the addition of those numbers.

Break down the problem into pseudo-code (this can also be done as a flowchart, however this is time consuming on a computer)

1. Create two variables -- num1 and num2
2. Ask user to input numbers
3. Store input into variable
4. Calculate sum of variables
5. Print sum
'''

num1 = 0 # first variable
num2 = 0 # second variable
# assigned default values as 0

num1 = input("Enter First Number") # taking input of first variable
num2 = input("Enter Second Number") # taking inupt of second variable
# user will see messages and input will be stored in the variables num1 and num2

# print(type(num1)) use this code to test what type the variable is

sum = (num1) + (num2) # adding the two variables together

print("The sum of Two Numbers is", sum) # printing the sum of the variables

# Arithmetic Operators that can be used include:
# +, -, *, /, %

'''
In Dr. Samrad's example it added as a string rather than an integer by default, meaning 21+21=2121 rather than the correct answer 42.
I didn't have this issue, but here is how it can be fixed:

amend sum = (num1) + (num 2) to convert the type of variable:
sum = int(num1) + int(num2)

sum = str(num1) + str(num2) gives the undesired result yielded in the example given during class by default.

I wonder why this is?

See the test for type/class of variable above in line 21 comment.
'''
