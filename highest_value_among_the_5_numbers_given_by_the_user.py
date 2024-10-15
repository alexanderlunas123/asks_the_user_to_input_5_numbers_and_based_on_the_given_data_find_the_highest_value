import pyfiglet

title = pyfiglet.figlet_format("\nHIGHEST NUMBER", font="slant")
print(title)

#input for the 1st num
#input for the 2nd num
#input for the 3rd num
#input for the 4th num
#input fot the 5th num
while True:
   first_number = input("\nInput the first number (any range): ")
   if first_number.isdigit():
        first_number = int(first_number)
        break
   else:
        print("Invalid input, must be a digit.")
        print("Please try again.\n")  

while True:         
   second_number = input("Input the second number (any range): ")
   if second_number.isdigit():
        second_number = int(second_number)
        break
   else:
        print("Invalid input, must be a digit.")
        print("Please try again.\n")

while True:         
   third_number = input("Input the third number (any range): ")
   if third_number.isdigit():
        third_number = int(third_number)
        break
   else:
        print("Invalid input, must be a digit.")
        print("Please try again.\n")    

while True:         
   fourth_number = input("Input the fourth number (any range): ")
   if fourth_number.isdigit():
        fourth_number = int(fourth_number)
        break
   else:
        print("Invalid input, must be a digit.")
        print("Please try again.\n")

while True:         
   fifth_number = input("Input the fifth number (any range): ")
   if fifth_number.isdigit():
        fifth_number = int(fifth_number)
        break
   else:
        print("Invalid input, must be a digit.")
        print("Please try again.\n")
                  
#var for the assumed initial/current highest value = 1st Number
#var for the assumed initial/current number with the highest value = 1st Number(string)
highest_value = first_number
number_with_the_highest_value = 'first number'


#if the 2nd Number is > the current highest value
     #then the current highest value is now the 2nd Number
     #then the current number with the highest value is now the 2nd Number(string)
if second_number > highest_value:
     highest_value = second_number
     number_with_the_highest_value = 'second number'

#if the 3rd Number is > the current/latest highest value
     #then the current/latest highest value is now the 3rd Number
     #then the current/latest number with the highest value is now the 3rd Number(string)
if third_number > highest_value:
     highest_value = third_number     
     number_with_the_highest_value = 'third number' 
     
#if the 4th Number is > the current/latest highest value
     #then the current/latest highest value is now the 4th Number
     #then the current/latest number with the highest value is now the 4th Number(string)
if fourth_number > highest_value:
     highest_value = fourth_number
     number_with_the_highest_value = 'fourth number'

#if the 5th Number is > the current/latest highest value
     #then the current/latest highest value is now the 5th Number
     #then the current/latest number with the highest value is now the 5th Number(string)
if fifth_number > highest_value:
     highest_value = fifth_number  
     number_with_the_highest_value = 'fifth number'      

#print the var containing the number with the highest value together with the var containing the highest value itself
print(f'\nThe {number_with_the_highest_value} have the highest value: {highest_value}\n')
