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
#var assigning a list for the current/latest number(s) with the highest value 
highest_value = first_number
number_with_the_highest_value = []

#if the var for the assumed initial/current highest value is indeed the 1st Number
     #then 'first number' (string) will be appended to the var assigning a list for the current/latest number(s) with the highest value
if highest_value == first_number:
     number_with_the_highest_value.append('"first number"')

#if the 2nd Number is > the current highest value
     #then the current/latest highest value is now the 2nd Number
     #then 'second number' (string) will be added and reset the previous possible executions to the var assigning a list for the current/latest number(s) with the highest value
#elif the 2nd Number does indeed shares the same value as the current highest value   
     #then 'second_number' (string) will be appended to the var assigning a list for the current/latest number(s) with the highest value
if second_number > highest_value:
     highest_value = second_number
     number_with_the_highest_value = ['"second number"']
elif second_number == highest_value:
     number_with_the_highest_value.append('"second number"')

#if the 3rd Number is > the current/latest highest value
     #then the current/latest highest value is now the 3rd Number
     #then 'third number' (string) will be added and reset the previous possible executions to the var assigning a list for the current/latest number(s) with the highest value
#elif the 3rd Number does indeed shares the same value as the current/latest highest value       
     #then 'third number' (string) will be appended to the var assigning a list for the current/latest number(s) with the highest value
if third_number > highest_value:
     highest_value = third_number 
     number_with_the_highest_value = ['"third number"']
elif third_number == highest_value:         
     number_with_the_highest_value.append('"third number"') 
     
#if the 4th Number is > the current/latest highest value
     #then the current/latest highest value is now the 4th Number
     #then 'fourth number' (string) will be added and reset the previous possible executions to the var assigning a list for the current/latest number(s) with the highest value 
#elif the 4th Number does indeed shares the same value as the current/latest highest value    
     #then 'fourth number' (string) will be appended to the var assigning a list for the current/latest number(s) with the highest value
if fourth_number > highest_value:
     highest_value = fourth_number
     number_with_the_highest_value = ['"fourth number"']
elif fourth_number == highest_value:     
     number_with_the_highest_value.append('"fourth number"')

#if the 5th Number is > the current/latest highest value
     #then the current/latest highest value is now the 5th Number
     #then 'fifth number' (string) will be added and reset the previous possible executions to the var assigning a list for the current/latest number(s) with the highest value
#elif the 5th Number does indeed shares the same value as the current/latest highest value     
     #then 'fifth number' (string) will be appended to the var assigning a list for the current/latest number(s) with the highest value
if fifth_number > highest_value:
     highest_value = fifth_number  
     number_with_the_highest_value = ['"fifth number"']
elif fifth_number == highest_value:  
     number_with_the_highest_value.append('"fifth number"')      

#print the var assigning a list for the current/latest number(s) with the highest value together with the var containing the current/latest highest value itself
print(f'\nThe {"; ".join(number_with_the_highest_value)} have the highest value: {highest_value}\n')

