# Question One
capital = $1000
daily_growth = 12%
period = 7

avg_daily_increase  = capital * daily_growth

weekly_increase = avg_daily_increase * 7

final_growth = capital + weekly_increase

print(final_growth)

# Question Two

buy = 1000
earn = 1210.68
text = "When we buy bitcoin with {} USD at the beginning of the week, we would earn {} USD at the end of the week, with an average gain of 12%."
print(text.format(buy, earn), '\n')

# Question Three

temp = input('Enter the temperature in Fahrenheit: ')
C = (5/9) * (int(temp) - 32)
print (f'Temperature (C) : {C}')

# Question Four

num = int(input("Input a three digit numbers: "))
x =num //100
x1 = (num - x*100)//10
x2 = (num - x*100 - x1*10)//10
x3 = num - x*100 - x1*10 - x2*1
print("The sum of digits in the number is", x+x1+x2+x3)

#Question Five
import math as m
length1= int(input("Enter the first side length"))
length2= int(input("Enter the second side length"))

hypotenuse = m.sqrt(length1**2 + length2**2)

print("The length of the hypotenuse is: ", hypotenuse)
