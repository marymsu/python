#Formula for converting Fahrenheit height into celsius C = (5/9) * (F - 32)
temp = int(input("Enter Temperature in Fahrenheit:"))
if temp >= 100:
  celsius_converter = (5/9) *(temp-32)
  print("The Temperature in Celsius is:", celsius_converter)
elif temp <50:
  print("The Temperature is too low")
  
 
 #Question two #Please form a list out of Fibonacci number from 1 to 50. 
#First two Fibonacci numbers are 1. 
#The next numbers are the sum of the previous two.
xterms = int(input("Enter terms:"))

#xterms
x1= 0
x2= 1

count= 0

if xterms <= 0:
  print("please enter a positive integer")
elif xterms==1:
  print("Fibonacci number upto", xterms)
  print(x1)
else:
  print("Fibonacci sequence")
  while count < xterms:
    print(x1)
    xth = x1+x2

#updated values
    x1= x2
    x2= xth
    count+=1


#Question three calculating bonus

salary = int(input("Enter your salary in dollars:"))
year_of_service = int(input("Enter the year of service:"))
if year_of_service>=5:
  bonus= 0.05 * salary
  net_bonus = bonus + salary
  print("The Net Bonus is:", net_bonus)
else:
  print("Bonus not payable")
  
#T Question Four ake input of ages of 3 people by user and determine oldest and youngest among them.

x= int(input("Enter your age X:"))
y= int(input("Enter your age Y:"))
z= int(input("Enter your age Z:"))

print(x,y,z)

if x>y:
  print("X is older than Y")
  if x>z:
    print("X is older than Z")
  else:
    print("X is younger than Z")
else:
  print("X is younger than Y")
  
 #Question 5
 number_of_classes = int(input("Enter the Number of classes held"))
classes_held = int(input("Enter the Number of classes attended."))
attendance = (classes_held/number_of_classes)/100
print("Percent of the classes attend is:", attendance)

if attendance>=0.75:
  print("The Student sit for the exams")
elif attendance<0.75:
   print("The Student cannot sit for the exams")

#Question 6
letters = input("Enter a letter")

for letter in letters:
  if letter in "a, e, i, o, u":
    print("The letter entered is a Vowel!")
  elif letters == "y":
    print("Y is sometimes a vowel and sometimes a consonant.")
else:
  print("The letter is a consonant.")
 

