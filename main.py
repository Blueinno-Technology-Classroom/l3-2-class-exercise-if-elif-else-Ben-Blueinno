##################################################
'''
Q1: 
'''

# TODO: Write your code here

weight = float(input('weight(kg) = '))
height = float(input('height(m) = '))

bmi = weight / (height * height)
interpret = 'unknown'
if bmi < 18.5:
    interpret = 'you are underweight'
elif bmi < 24.9:
    interpret = 'you have a normal weight'
elif bmi < 29.9:
    interpret = 'you are overweight'
elif bmi < 34.9:
    interpret = 'you are in obesity class I'
elif bmi < 39.9:
    interpret = 'you are in obesity class II'
else:
    interpret = 'you are in obesity class III'

print(f'{weight} / ({height} x {height}) = {bmi}')
print(f'Your BMI is {bmi}, {interpret}.')
##################################################
'''
Q2:
'''

# TODO: Write your code here
size = input('Size (S, M, L): ')
add_pepperoni = input('Add pepperoni (Y/N): ')
extra_cheese = input('Extra cheese (Y/N): ')

bill = 0
if size == 'S':
    bill += 45
elif size == 'M':
    bill += 50
else:
    bill += 55

if add_pepperoni == 'Y':
    if size == 'S':
        bill += 5
    else:
        bill += 8

if extra_cheese == 'Y':
    bill += 3

print(f'Your final bill is ${bill}.')

##################################################
