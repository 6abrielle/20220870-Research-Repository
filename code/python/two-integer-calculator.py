'''Calculator program using conditionals'''

num1 = 0
num2 = 0
result = 0


num1 = int(input("Enter first number: "))
opp = str(input("Choose an operation + - * /: ")) # this code has an error here. "SyntaxError: unexpected E0F while parsing".
# = assignment operator
# == comparison operator
num2 = int(input("Enter second number: "))

if(opp == '+'):
    result = num1+num2
elif(opp == '-'):
    result = num1-num2
elif(opp == '*'):
    result = num1*num2
elif(opp == '/'):
    result = num1/num2; 
else:
    print("Wrong Input")

print("The answer is ", result)

#figuore out what the error is in this code and how i can make it work.
