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
                  
#var for the max value
highest_value = max(first_number, second_number, third_number, fourth_number, fifth_number)
#var for the number/s with the max value
number_or_numbers_with_the_highest_value = []

#if the max value is == to the 1st num
     #then var for the number/s with the max value will bear the str '1st Number' together with the .append() method
#if the max value is == to the 2nd num
     #then var for the number/s with the max value will bear the str '2nd Number' together with the .append() method
#if the max value is == to the 3rd num
     #then var for the number/s with the max value will bear the str '3rd Number' together with the .append() method
#if the max value is == to the 4th num
     #then var for the number/s with the max value will bear the str '4th Number' together with the .append() method
#if the max value is == to the 5th num
     #then var for the number/s with the max value will bear the str '5th Number' together with the .append() method
if highest_value == first_number:
    number_or_numbers_with_the_highest_value.append('1st Number')
if highest_value == second_number:
    number_or_numbers_with_the_highest_value.append('2nd Number')
if highest_value == third_number:
    number_or_numbers_with_the_highest_value.append('3rd Number')
if highest_value == fourth_number:
    number_or_numbers_with_the_highest_value.append('4th Number')
if highest_value == fifth_number:
    number_or_numbers_with_the_highest_value.append('5th Number')   

#print the var for the number/s with the max value together with the var for the max value
print(f'\nThe {", ".join(number_or_numbers_with_the_highest_value)} have the highest value: {highest_value}\n')
