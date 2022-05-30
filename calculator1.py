# Basic calculator
# No error feedback from code (Only error messages from system)

i = int(input('Enter a number: '))
j = input('Choose an operator (+, -, *, /):')
k = int(input('Enter another number: '))

if j == "+":
    print( i + k)

elif j == "-":
    print( i - k)

elif j == "*":
    print( i * k)

else:
    j == "/"
    print( i / k)