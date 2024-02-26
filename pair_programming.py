#Jimena Garciaprieto
#Takes two values (feet and inches) and converts to meters
    
ft = int(input('Feet: '))
inch = int(input('Inches: '))

inches = (ft*12) + inch
meters = inches / 39.37

print(f'{meters:.2f} meters')

#Olivia Comments:
# Improvements: define a function that can be called later, instead of having to copy and paste the code
# What Looks Good: I like that at the end it prints not just the numerical value but defines that value as being in meters. 
def inches_to_meters(feet, inch):
    inches = (feet*12) + inch
    meters = inches / 39.37
    return meters

def test_inches_to_meters():
    assert inches_to_meters(0,0) == 0
    assert inches_to_meters(3,3.37) == 1
    print("Passed all tests")
    
    
    
    
