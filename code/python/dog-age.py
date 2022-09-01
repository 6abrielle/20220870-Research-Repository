'''
Write a Python program that calculates a dog's age in dog's years.

Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.

Your program should look as follows:
  Input a dog's age in human years: 15
  The dog's age in dog's years is 73

pseudo-code
1. Create variable -- human_years
2. Ask user to input the age of the dog in human years
3. Store input into variable
4. Boolean
    a. if: human_years <= 2 (human_years * 10.5)
    b. else: 21 + (human_years - 2) * 4)
5. Print the dog's age in dog years

'''

human_years = 0 
# assigning default value to 0

human_years = input("Enter the dog's age in human years. Round to the closest year") 
#input from user will be stored in human_years variable

# print(type(human_years))--testing the data type

if human_years <= 2:
    dog_years = human_years * 10.5

else: dog_years = (21 + (human_years - 2) * 4)

print("The dogs age in dog years is", dog_years)
