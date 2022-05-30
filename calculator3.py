# This will be me revisting the calculator code after a couple of weeks of not coding anything. 
# Let's see how much I retained. 

# Get 2 numbers and an operator from the user.
while True:
    try:
        num1 = int(input('Enter a digit: '))
        break
    except ValueError:
        print('Please input a number!')
        continue
print('You have entered:', + num1)

op = 0
while True:
    try:
        op = input('Type an operator (+, -, *, /): ')
        if op == '+' or op == '-' or op == '*' or op == '/':
            break
        else:
            print('An operator was not selected') 
            continue
    except:
        continue
    
    
while True:
    try:
        num2 = int(input('Enter a digit: '))
        break
    except ValueError:
        print('Please input a number!')
        continue
print('You have entered:', + num2)

# Code to do the math.
if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    print(num1 / num2)