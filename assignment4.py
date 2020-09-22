#Question One
my_list = [34, 56, 76, 45, 2, 12, 67, 98, 37, 54, 66]
for low in my_list:
  lowest_sum = my_list [4] + my_list[5]
print("Lowest Sum is:", lowest_sum)


my_list = [34, 56, 76, 45, 2, 12, 67, 98, 37, 54, 66]
for highest in my_list:
  highest_sum = my_list [2] + my_list[7]
print("Highest Sum is:", highest_sum)

#Question Two

user_name = input("Enter your Username")

 
names = ["David", "Michael", "John", "James", "Greg", "Mark", "William", "Richard", "Thomas", "Steven", 
          "Mary", "Susan", "Maria", "Karen", "Lisa", "Linda", "Donna", "Patricia", "Debra", "Eric"]
names.append(user_name)

scores = [99, 87, 78, 86, 68, 94, 76, 97, 56, 98, 76, 87, 79, 90, 73, 93, 82, 69, 97, 98]

print(user_name, "Your score is: ", scores[-1])

#Question 3

names = ["David", "Michael", "John", "James", "Greg", "Mark", "William", "Richard", "Thomas", "Steven", 
          "Mary", "Susan", "Maria", "Karen", "Lisa", "Linda", "Donna", "Patricia", "Debra", "Eric"]
scores = [99, 87, 78, 86, 68, 94, 76, 97, 56, 98, 76, 87, 79, 90, 73, 93, 82, 69, 97, 98]

 
max_score = scores [0]
for score in scores:
   if score > max_score:
     max_core = score
print("The maximum score is:", max_score)
print("The maximum score count is:", scores.count(99))


#QUESTION 5

months_name =["January", "February", "March", "April", "May", "June","July", "August", "September", 
"October", "November", "December"]
days_count = [31,28,31,30,31,30,31,31,30,31,30,31]

months_and_days = [months_name, days_count]

#print(months_and_days)

spring = ['March', 'April', 'May']
summer = ['June', 'July', 'August']
fall = ['September', 'October', 'November']
winter = ['December', 'January', 'February']
months_by_season = [spring, summer, fall, winter]

print(months_by_season[0])
print(months_name[2])

print(days_count[2])


#QUESTION 6
months_name =["January", "February", "March", "April", "May", "June","July", "August", "September", 
"October", "November", "December"]
days_count = [31,28,31,30,31,30,31,31,30,31,30,31]

months_and_days = [months_name, days_count]

#print(months_and_days)

spring = ['March', 'April', 'May']
summer = ['June', 'July', 'August']
fall = ['September', 'October', 'Novembers']
winter = ['December', 'January', 'February']
months_by_season = [spring, summer, fall, winter]

print("The season is:", months_by_season[0])
print("The month is: ", months_name[2])

print("The number of days in a month are:", days_count[2])

summer_days_count = days_count[5] + days_count[6] + days_count[7]

print("The summer days count sum is:", summer_days_count)