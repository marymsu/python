# Question One


day = input("Day:")


days= {'1': 'monday',
'2':'Tuesday',
'3': 'Wednesday',
'4':'Thursday',
'5': 'Friday',
'6': 'Saturday',
'7': 'Sunday'
}
output=""
for ch in day:
  output+= days.get(ch, "!") + "" ""
  print (output)
  
days.pop('1')
days.pop('2')
print(days)


#Question Two

student = {
"John":{"gender":"Male","age": 25},
"Lisa":{"gender":"Female","age": 28},
"Linda":{"gender":"Female","age": 32},
        "child":{
            "Susan":{"gender":"female", "age":6}
            },
            
"Michael":{"gender":"male","age": 41},
        "children":{
            "Karen":{"gender":"female", "age":12},
            "Greg":{"gender":"female", "age": 7}
            }          
}  
children = student['children']
print(list(children))