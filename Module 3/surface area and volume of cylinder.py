# Python program to calculate surface volume and area of a cylinder. 

pi=22/7
height=float(input("Height of cylinder:"))
radius=float(input("Radius of cylinder:"))
volume=pi*radius*radius*height
surface_area=((2*pi*radius)*height)+((pi*radius**2)*2)
print("Volume of cylinder is:",volume)
print("Surface area of cylinder is:",surface_area)