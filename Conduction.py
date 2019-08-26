#Program to find heat dissipation due to conduction

#Conductivity of material
k=float(input("Enter the thermal conductivity of given material:-"))

#Diameter of given rod
d=float(input("Enter the Diameter of given specimen:-"))

#Area is given by
Area=(3.143*d**2)/4

#Initial temperature
T1=float(input("Enter the initial Temperature:-"))

#Final temperature
T2=float(input("Enter the final temperature:-"))

#length of rod
x=float(input("Enter the length of given specimen:-"))
Q=k*Area*(T2-T1)/x

print(Q,"KJ/m")

