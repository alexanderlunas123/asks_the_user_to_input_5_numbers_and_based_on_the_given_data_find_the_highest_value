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
highest_value = first_number

#if the 2nd Number is > the current highest value
     #then the current highest value is now the 2nd Number
if second_number > highest_value:
     highest_value = second_number

#if the 3rd Number is > the current/latest highest value
     #then the current/latest highest value is now the 3rd Number
if third_number > highest_value:
     highest_value = third_number      
     
#if the 4th Number is > the current/latest highest value
     #then the current/latest highest value is now the 4th Number
if fourth_number > highest_value:
     highest_value = fourth_number

#if the 5th Number is > the current/latest highest value
     #then the current/latest highest value is now the 5th Number
if fifth_number > highest_value:
     highest_value = fifth_number           

#print the var containing the highest value 
print(f'\nThe highest value: {highest_value}\n')
