import numpy as np
import math

print('''** WELCOME TO THE NUTRITION CALCULATOR **\n
** This calculator calculates your Basal Metabolic Rate or BMR which is the minimum number of calories your body needs 
to function for 24 hours in a resting state.\n
** The Mifflin - ST Jeor Equation is used to accurately calculate your BMR.\n
** The calculator can be used to calculate BMR for those who use both Metric (US) as well as Imperial (UK) systems.\n
** Once Your BMR is calculated based on your inputs the calculator then provides you with your daily calorie 
requirements and time line options depending on your daily activity levels and your desired weight loss goals.\n
** Keep Going!! **
''')
# INPUT
country = input('What country do you live in, US or UK?\n')
country = country.upper()

# Hello what is your name
name = input('What is your name?\n')

gender = input('Are you a man or a woman?\n')
gender = gender.lower()

age = float(input(f'Hello {name}, how old are you?\n'))

activity = input \
    ('How often do you exercise?\n\nSedentary: (little or no exercise)\n\nLight: (1-3 days/week)\n\nModerate: '
     '(3-5 days/week)\n\nActive: (6-7 days/weeks)\n\nSuper: (2 times/day/7 days/week):\n\nPlease answer based on the '
     'Activity descriptions provided above: ')

activity = activity.lower()
if activity == 'sedentary':
    a = 1.2
elif activity == 'light':
    a = 1.375
elif activity == 'moderate':
    a = 1.55
elif activity == 'active':
    a = 1.725
else:
    a = 1.9

bmr = 0

if country == 'US':
    weight = float(input('What is your weight in pounds?\n'))
    feet = float(input('What is your height in feet?\n'))
    inches = float(input('What is your height in inches?\n'))
    total_inches = (feet * 12) + inches
    desired_weight_option = input("Do you wish to lose or gain weight? Please type 'lose' or 'gain'\n")
    desired_weight = float(input('What is your desired weight in pounds?\n'))
    print('***********************************************************************')
    if gender == 'man':
        bmr = (4.536 * weight) + (15.88 * total_inches) - (5 * age) + 5
    else:
        bmr = (4.536 * weight) + (15.88 * total_inches) - (5 * age) - 161;

elif country == 'UK':
    kilos = float(input('What is your weight in kilograms?\n'))
    feet = float(input('What is your height in feet?\n'))
    inches = float(input('What is your height in inches?\n'))
    centimeters = ((feet * 12) + inches) * 2.54
    desired_weight_option = input('Do you wish to loose weight or gain weight?\n')
    desired_weight_kilos = float(input('What is your desired weight in kilograms?\n'))
    print('***********************************************************************')
    if gender == 'man':
        bmr = (10 * kilos) + (6.25 * centimeters) - (5 * age) + 5
    else:
        bmr = (10 * kilos) + (6.25 * centimeters) - (5 * age) - 161
else:
    print('Please provide a valid input')

bmr = round(bmr)

print(f'Your BMR is:\n{bmr}')

maintenance_calories = bmr * a
maintenance_calories = round(maintenance_calories)
print(f'Your daily maintenance calories are:\n{maintenance_calories}')

weekly_calories = maintenance_calories * 7
print(f'Your weekly maintenance calories are:\n{weekly_calories}')
print('***********************************************************************')

desired_weight_option = 0

if desired_weight_option == 'gain':
    one_pound_daily = maintenance_calories + 500
    one_pound_weekly = weekly_calories + 3500
    print \
        (f'To gain 1 pound a week your calorie intake should be:\nDaily Total:\n{one_pound_daily}\nWeekly Total:\n{one_pound_weekly}')

    one_half_daily = maintenance_calories + 750
    one_half_weekly = weekly_calories + 5250
    print \
        (f'To gain 1.5 pounds a week your calorie intake should be:\nDaily Total:\n{one_half_daily}\nWeekly Total:\n{one_half_weekly}')

    two_pound_daily = maintenance_calories + 1000
    two_pound_weekly = weekly_calories + 7000
    print \
        (f'To gain 2 pounds a week your calorie intake should be:\nDaily Total\n{two_pound_daily}\nWeekly Total:\n{two_pound_weekly}')
    print('***********************************************************************')
else:
    one_pound_daily = maintenance_calories - 500
    one_pound_weekly = weekly_calories - 3500
    print \
        (f'To lose 1 pound a week your calorie intake should be:\nDaily Total:\n{one_pound_daily}\nWeekly Total:\n{one_pound_weekly}')

    one_half_daily = maintenance_calories - 750
    one_half_weekly = weekly_calories - 5250
    print \
        (f'To lose 1.5 pounds a week your calorie intake should be:\nDaily Total:\n{one_half_daily}\nWeekly Total:\n{one_half_weekly}')

    two_pound_daily = maintenance_calories - 1000
    two_pound_weekly = weekly_calories - 7000
    print \
        (f'To lose 2 pounds a week your calorie intake should be:\nDaily Total\n{two_pound_daily}\nWeekly Total:\n{two_pound_weekly}')
    print('***********************************************************************')

desired_weight = 0
weight = 0
desired_weight_kilos = 0
kilos = 0
if country == 'US':
    if desired_weight_option == 'gain':
        deficit = desired_weight - weight
        deficit = round(deficit)
    else:
        deficit = weight - desired_weight
        deficit = round(deficit)
else:
    if desired_weight_option == 'gain':
        deficit = desired_weight_kilos - kilos
        deficit_kilos = round(deficit)
        deficit = round(deficit * 2.205)
    else:
        deficit = kilos - desired_weight_kilos
        deficit_kilos = round(deficit)
        deficit = round(deficit * 2.205)

deficit_kilos = 0

if country == 'US':
    if desired_weight_option == 'gain':
        print(f'Your target weight requires you to gain:\n{deficit} pounds')
        length = float(input('How many pounds a week would you like to gain? 1, 1.5, or 2 ?:\n'))
        print('***********************************************************************')
    else:
        print(f'Your target weight requires you to loose:\n{deficit} pounds')
        length = float(input('How many pounds a week would you like to loose? 1, 1.5, or 2 ?:\n'))
        print('***********************************************************************')
else:
    if desired_weight_option == 'gain':
        print(f'Your target weight requires you to gain:\n{deficit_kilos} kilos')
        length = float(input('How many kilos a week would you like to gain? .45, .68, or .90 ?:\n'))
        if length == .45:
            length = 1
        elif length == .68:
            length = 1.5
        else:
            length = 2
        print('***********************************************************************')
    else:
        print(f'Your target weight requires you to loose:\n{deficit_kilos} kilos')
        length = float(input('How many kilos a week would you like to loose? .45, .68, or .90 ?:\n'))
        if length == .45:
            length = 1
        elif length == .68:
            length = 1.5
        else:
            length = 2
        print('***********************************************************************')

duration = 0
if length == 1:
    for i in range(deficit, 0, -1):
        if deficit >= 0:
            deficit -= 1
            duration += 1


elif length == 1.5:
    for i in np.arange(deficit, 0, -1.5):
        if deficit >= 0:
            deficit -= 1.5
            duration += 1


elif length == 2:
    for i in range(deficit, 0, -2):
        if deficit >= 0:
            deficit -= 2
            duration += 1

months = duration / 4
months = math.ceil(months)
years = months / 12
years = round(years, 2)

if duration >= 4:
    print(f'Goal can be achieved in:\n{duration} weeks')
    print(f'Goal can be achieved in:\n{months} months')
    if duration >= 12:
        print(f'Goal can be achieved in:\n{years} year(s)')
    else:
        print('')
else:
    print(f'Goal can be achieved in:\n{duration} weeks')
print('***********************************************************************')
