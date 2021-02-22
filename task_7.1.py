#1
def in_to_cm(inch):
    cm = inch * 2.54
    print(cm)
    return(cm)

#2
def cm_to_in(cm):
    inch = cm / 2.54
    print(inch)
    return(inch)

#3
def mile_to_km(mile):
    km = mile * 1.609
    print(km)
    return(km)


#4
def km_to_mile(km):
    mile = km / 1.609
    print(mile)
    return(mile)

#5
def lb_to_kg(lb):
    kg = lb * 0.45
    print(kg)
    return(kg)

#6
def kg_to_lb(kg):
    lb = kg * 2.205
    print(lb)
    return(lb)

#7
def oz_to_gm(oz):
    gram = oz * 28.35
    print(gram)
    return(gram)

#8
def gm_to_oz(gm):
    oz = gm / 28.35
    print(oz)
    return(oz)

#9
def gl_to_ltr(gl):
    ltr = gl * 3.785
    print(ltr)
    return(ltr)

#10
def ltr_to_gl(ltr):
    gl = ltr / 3.785
    print(gl)
    return(gl)

#11
def pt_to_ltr(pt):
    ltr = pt * 0.568
    print(ltr)
    return(ltr)

#12
def ltr_to_pt(ltr):
    pt = ltr * 1.76
    print(pt)
    return(pt)


request = int(input('''Enter a number from 1 to 12 to transfer:
1-2 - inches to centimeters and vice versa
3-4 - miles to kilometers and vice versa
5-6 - pounds to kilograms and vice versa
7-8 - ounces to grams and vice versa
9-10 - gallons to liters and vice versa
11-12 - pints to liters and vice versa
or press 0 to quit

'''))

while request != 0:
    if request in range(1, 13):
        if request == 1:
            number = float(input('''
Inches to Centimeters
Enter any number: '''))
            in_to_cm(number)
        elif request == 2:
            number = float(input('''
Centimeters to Inches
Enter any number: '''))
            cm_to_in(number)
        elif request == 3:
            number = float(input('''
Miles to Kilometers
Enter any number: '''))
            mile_to_km(number)
        elif request == 4:
            number = float(input('''
Kilometers to Miles
Enter any number: '''))
            km_to_mile(number)
        elif request == 5:
            number = float(input('''
Pounds to Kilograms
Enter any number: '''))
            lb_to_kg(number)
        elif request == 6:
            number = float(input('''
Kilograms to Pounds
Enter any number: '''))
            kg_to_lb(number)
        elif request == 7:
            number = float(input('''
Ounces to Grams
Enter any number: '''))
            oz_to_gm(number)
        elif request == 8:
            number = float(input('''
Grams to Ounces
Enter any number: '''))
            gm_to_oz(number)
        elif request == 9:
            number = float(input('''
Gallons to Liters
Enter any number: '''))
            gl_to_ltr(number)
        elif request == 10:
            number = float(input('''
Liters to Gallons
Enter any number: '''))
            ltr_to_gl(number)
        elif request == 11:
            number = float(input('''
Pints to Liters
Enter any number: '''))
            pt_to_ltr(number)
        elif request == 12:
            number = float(input('''
Liters to Pints
Enter any number: '''))
            ltr_to_pt(number)
        request = int(input('''
Enter a number from 1 to 12, or 0 to quit:

'''))
    else:
        request = int(input('''Use only numbers from 1 to 12, and 0 to quit:

'''))
        
    
