
# coding: utf-8

# In[13]:

#Problem 1
#Prompt the user for their name and force the entry to be a string-type varable:
Name=str(input("What's your name? "))
#Create a string-type variable that concatenates the input with the desired greeting
Output= "Hello, " + Name + ", how are you?"
#Print the Output string
print(Output)


# In[14]:

#Problem 2
#Prompt the user for the input word and force the variable to a string-type:
Input_Word=str(input("What is youre input string?: "))
#Print the user-input value as well as the number of characters in that input in a single output:
print(Input_Word + " Has " + str(len(Input_Word)) + " Characters " , sep=" ")


# In[16]:

#Problem 3
#Prompt user for input and force the variables to be string-type:
Noun=str(input("Enter a Noun: "))
Verb=str(input("Enter a Verb: "))
Adj=str(input("Enter an Adjective: "))
Adv=str(input("Enter an Adverb: "))
#Use a single output statement to create the Mad Lib by concatenating the variables with the rest of the string:
print("The "+ Adj + " " + Noun +" will "+ Verb + " " + Adv, sep=" ")


# In[17]:

#Problem 4
#Prompt user for numbers:
Number_1=input("Enter a number: ")
Number_2=input("Enter another number: ")
#Create string-type variables for the formulas in the output statement:
Addt=str(Number_1)+" + "+str(Number_2)
Subt=str(Number_1)+" - "+str(Number_2)
Multip=str(Number_1)+" * "+str(Number_2)
Divi=str(Number_1)+" / "+str(Number_2)
#Create new integer-type variables using user-input and calculate soltions:
Add=int(Number_1) + int(Number_2)
Sub=int(Number_1)-int(Number_2)
Multi=int(Number_1)*int(Number_2)
Div=int(Number_1)/int(Number_2)
#Print the formula solution variables as concatenated strings with a line break between them:
print(str(Addt)+" = "+str(Add), str(Subt)+" = "+str(Sub), str(Multip)+" = "+str(Multi), str(Divi)+" = "+ '{0:.0f}'.format(Div), sep="\n")


# In[29]:

#Problem 5
#Prompt the user for current age and retirement age. Force these inputs into integer-type variables:
Age=int(input("What is your current age: "))
Retirement_Age=int(input("What age do you want to retire: "))
#Import the datetime add-on:
import datetime
#Create a new variable for the current year as an integer using datetime:
This_Year=int((datetime.datetime.now().strftime ("%Y")))
#Create a new variable that will calculate the year of retirement by subtracting the current year from the user-input desired retirement year
Year_of_Retirement=int(This_Year)+int(Retirement_Year)
#Use the newly created variable to also calculate the number of years until retirement:
Years_to_Retire=(Year_of_Retirement-This_Year)
#Print your two output statements, converting variables into strings and concatenating them together:
print("You have " + str(Years_to_Retire) + " years left until you can retire.", sep=" ")
print("It's " + str(This_Year) + ", so you can retire in", Year_of_Retirement, sep=" ")


# In[19]:

#Problem 6
#Create two variables that prompt the user for input to get values for the room length and width. Define these variables as integer-type:
Room_Length=int(input("What is the length of the room in feet?: "))
Room_Width=int(input("What is the width of the room in feet? "))
#Calculate the room area in feet by multiplying the two variables together:
Room_Area_in_Square_Feet=Room_Length*Room_Width
#Store the conversion factor of feet to meters as a variable:
Conversion_Factor=float(.09290304)
#Use the stored conversion variable to calculate the are of the room meters:
Room_Area_in_Square_Meters=Room_Area_in_Square_Feet*Conversion_Factor
#Print the input verification statement:
print("You entered dimensions of", Room_Length, "feet by", Room_Width, "feet.")
#Print the area of the room in square feet and meters using the formatting command to limit the displayed decimal places:
print("The area is " + str(Room_Area_in_Square_Feet) + " square feet", "{0:.3f}".format(Room_Area_in_Square_Meters) + " square meters", sep="\n")


# In[6]:

#Problem 7
#Prompt the user for inputs for the number of people, pizzas, and slices per pizza and force the variables to be integer-type:
Number_Of_People=int(input("How many people will be eating pizza?: "))
Number_Of_Pizzas=int(input("How many pizzas are you splitting?: "))
Number_Of_Slices=int(input("How many slices are there in a pizza?: ")) 
#Calculate the number of slices per person and use the floor limit to force the calculation to round down to the nearest whole integer:
import math
Slices_Per_Person=math.floor((Number_Of_Pizzas*Number_Of_Slices)/Number_Of_People)
#Calculate the leftover slices by subtracting the evenly divided slices from the total available slices:
Remaining_Slices=(Number_Of_Pizzas*Number_Of_Slices)-(Slices_Per_Person*Number_Of_People)
#Confirm the user's input by printing the input variables:
print(Number_Of_People, "people with", Number_Of_Pizzas, "pizzas", sep=" ")
#Print the number of slices each person gets:
print("Each person gets " + str(Slices_Per_Person) + " slices of pizza.", sep=" ")
#Print the remaining leftover slices
print("There are " + str(Remaining_Slices) + " lefover slice(s) of pizza.", sep=" ")


# In[ ]:

#Problem 8
#Prompt the user for the length and width of a room:
Room_Length=int(input("What is the length of the room you're painting?: "))
Room_Width=int(input("What is the width of the room you're painting?: "))
#Calculate the room area seperately from conversion to use in output statement:
Room_Area=Room_Length*Room_Width
#Store the conversion from square foot to gallon as a constant:
Square_Foot_Per_Gallon=350
#Calculate the number of gallons required and use the ceil limit to round up to the nearest whole integer:
import math
Required_Gallons=math.ceil(Room_Area/Square_Foot_Per_Gallon)
#Print the output of your two calculations by converting the variables into strings:
print("You will need to purchase " + str(Required_Gallons) + " gallon(s) of paint to cover " + str(Room_Area) + " square feet.", sep=" ")


# In[1]:

#Problem 9
#Prompt the user for the price and quantity of three items and set the input to float-type and integer-type variable:
Item1_Price=float(input("What is the price of the 1st item?: $"))
Item1_Quantity=int(input("Enter the quantity of item 1 purchased: "))
Item2_Price=float(input("What is the price of the 2nd item?: $"))
Item2_Quantity=int(input("Enter the quantity of item 2 purchased: "))
Item3_Price=float(input("What is the price of the 3rd item?: $"))
Item3_Quantity=int(input("Enter the quantity of item 3 purchased: "))
#Create the tax rate as a constant variable
Tax=.055
#Create a new variable that calculates the subtotal of the items:
Subtotal=Item1_Price*Item1_Quantity+Item2_Price*Item2_Quantity+Item3_Price*Item3_Quantity
#Create a new variable that calculates the tax on the items:
Total_Tax=Tax*Subtotal
#Create a new variable that calculates the total of the items:
Total=(Subtotal+Total_Tax)
print("Subtotal: " + '${:,.2f}'.format(Subtotal) , "Tax: " + '${:,.2f}'.format(Total_Tax) , "Total: " + '${:,.2f}'.format(Total) , sep="\n")


# In[12]:

#Problem 10
#Prompt the user for inputs and force inputs into proper variable type formats:
Principal=float(input("Enter the principal amount: $"))
Input_Interest_Rate=float(input("Enter the rate of interest: "))
Number_of_Years=int(input("Enter the number of years: "))
#Convert the user-input interest rate to percentage for calculation:
Interest_Rate=float(Input_Interest_Rate/100)
#Calculate the simple interest. Use the math add on to force fractions of a penny to be rounded up:
import math
Simple_Interest=Principal*(1+(Interest_Rate*Number_of_Years))
print("After " + str(Number_of_Years) + " years at " + str(Input_Interest_Rate) + "%, the investment will be worth " + '${:.2f}'.format(Simple_Interest))

