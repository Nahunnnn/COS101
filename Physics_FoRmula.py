print("Physics Formula Generator")
print("a = Momentum formula")
print("b = Force formula")
print("c = Work formula")
print("d = Pressure formula")
print("e = Density formula")
print()

z = input("Which  of these 5 formulas do you want to use? ").lower()

# Momentum
if z == "a":
    print("Momentum = m * v")
    mass = float(input("Enter mass (kg): "))
    velocity = float(input("Enter velocity (m/s): "))
    momentum = mass * velocity
    print(f"\nMomentum = {momentum} kg·m/s")
#Force
elif z == "b":
    print("Force = m * a")
    mass = float(input("Enter mass (kg): "))
    acceleration = float(input("Enter acceleration (m/s^2): "))
    force = mass * acceleration
    print(f"\nForce = {force} N")   
#Work
elif z == "c":
    print('Work= f*d')
    force= float(input("Enter force(N)"))
    distance= float(input("Enter distance(m)"))
    Work= force * distance 
    print(f"\nWork= {Work} Nm")
#Pressure
elif z == "d":
    print ('Pressure=F/A')
    force= float(input("Enter force(N)"))
    area = float(input("Enter area (m^2)"))

    Pressure = force/area
    print(f"\nPressure= {Pressure} N/m^2")
#Density
elif z == "e":
    print ('Density=m/V')
    mass= float(input("Enter mass(kg)"))
    volume = float(input("Enter volume (m^3)"))

    Density = mass/volume
    print(f"\nDensity= {Density} kg/m^3")
      
else:
    print ("Invalid (Choose between formula a-e")
