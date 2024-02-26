#Jimena Garciaprieto
#Takes two values (feet and inches) and converts to meters

ft = int(input('Feet: '))
inch = int(input('Inches: '))

inches = (ft*12) + inch
meters = inches / 39.37

print(f'{meters:.2f} meters')
