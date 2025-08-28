students = {'jhon':45,'rohan':40,'rahul':35,'ruhi':50}
name = input('Enter your name: ')
if name in students:
    print(f"{name} 's marsks : {students[name]}")
else:
    print(f"{name} not found in the records")