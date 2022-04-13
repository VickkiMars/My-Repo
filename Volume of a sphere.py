#volume of a sphere
def Find_Volume():
    radius = int(input('Radius >>> '))
    
    rad = str(radius)
    volume = (4/3)*3.1419*(radius^3)
    

    Volume = str(volume)
    
    output = 'The volume of a SPHERE with ' + rad + 'cm radius is ' + Volume + ' cm3'
    print(output)
    
Find_Volume()
