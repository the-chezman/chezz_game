import math
import barGraph #has to be in same folder to run

def run1(): #asks for radius and implements circle formula
    radius = int(input("what is the radius? "))
    print("area of circle with " + str(radius) + " radius: " + str(round((math.pi * radius**2), 3))) 

def run2(): #asks for radius and height and implements cylinder formula
    radius = int(input("what is the radius? "))
    height = int(input("what is the height? "))
    print("area of cylinder with " + str(radius) + " radius and " + str(height) + " height: " + str(round((math.pi * radius**2 * height), 3))) 

def run3(): #asks for base and height and implements triangle formula
    base = int(input("what is the base? "))
    height = int(input("what is the height? "))
    print("area of triangle with " + str(base) + " base and " + str(height) + " height: " + str(round((1/2 * base * height), 3)))

def run4(): #asks for which side of triangle you want, then calculates based on pythag theorum for right triangles
    try:
        side = input("which side of triangle is missing? a, b, c only: ")
    except:
        print("enter a valid letter")
    if(side == "a"):
        try:
            sideB = int(input("what is side of b? ")) #sqrt(c^2 - b^2)
            sideC = int(input("what is side of c? "))
            sideA = math.sqrt(sideC**2 - sideB**2)
        except:
            print("enter a positive value/real value")
        
        print("side a with triangle values b as " + str(sideB) + " and side c as " + str(sideC) + ": " + str(sideA))
    elif(side == "b"):
        try:
            sideA = int(input("what is side of a? ")) #sqrt(c^2 - a^2)
            sideC = int(input("what is side of c? "))
            sideB = math.sqrt(sideC**2 - sideA**2)
        except:
            print("enter a positive value/real value")
        
        print("side a with triangle values a as " + str(sideA) + " and side c as " + str(sideC) + ": " + str(sideB))
    else:
        try:
            sideA = int(input("what is side of b? ")) #sqrt(a^2 + b^2)
            sideB = int(input("what is side of c? "))
            sideC = math.sqrt(sideA**2 + sideB**2)
        except:
            print("enter a positive value/real value")
        
        print("side a with triangle values a as " + str(sideA) + " and side b as " + str(sideB) + ": " + str(sideC))

def run5(): #takes the other file in folder to run
    barGraph.runFunction()



print("pick an option to do")
print("1. area of circle")
print("2. area of cylinder")
print("3. area of triangle")
print("4. find missing side of right triangle")
print("5. make graph")
print("6. exit")

choice = int(input("your choice: "))

while choice != 6:
    
    if choice == 1:
        run1()
    elif choice == 2:
        run2()
    elif choice == 3:
        run3()
    elif choice == 4:
        run4()
    elif choice == 5:
        run5()
    elif choice == 6:
        break
    else:
        print("pick a valid number")
    choice = int(input("your choice: "))


print("goodbye")

