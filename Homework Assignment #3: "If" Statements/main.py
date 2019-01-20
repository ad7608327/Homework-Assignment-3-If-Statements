"""
The Purpose of this Script is
Create a function that accepts 3 parameters and checks for equality between any two of them.
"""
A=input("What Do you Want (Assignment or extra credit) > ")
#num1, num2, num3 = int(input("Number 1 > ")), int(input("Number 2 > ")), int(input("Number 3 > "))

def Assignment(num1,num2,num3):
    #              ( num1 )
    # num1 equal any number
    if num1 == num2:
        print(num1,"is Equal",num2)
    elif num1 == num3:
        print(num1,"is Equal",num3)
    # num1 doesn't equal any number
    if num1 != num2:
        print(num1,"doesn't Equal",num2)
    elif num1 != num3:
        print(num1,"doesn't Equal",num3)
    # num1 greater than any number
    if num1 > num2:
        print(num1,"Greater than",num2)
    elif num1 > num3:
        print(num1,"Greater than",num3)
    # num1 greater than equal any number
    if num1 >= num2:
        print(num1,"Greater than Equal",num2)
    elif num1 >= num3:
        print(num1,"Greater than Equal",num3)
    # num1 smaller than any Number
    if num1 < num2:
        print(num1,"Smaller than",num2)
    elif num1 < num3 :
        print(num1,"Smaller than",num3)
    # num1 <= any number
    if num1 <= num2:
        print(num1,"Smaller than Equal",num2)
    elif num1 <= num3:
        print(num1,"Smaller than Equal",num3)
    #                ( num2 )
        # num2 equal any number
    if num2 == num1:
        print(num2,"is Equal",num1)
    elif num2 == num3:
        print(num2,"is Equal",num3)
        # num2 doesn't equal any number
    if num2 != num1:
        print(num2,"doesn't Equal",num1)
    elif num2 != num3:
        print(num2,"doesn't Equal",num3)

        # num2 greater than any number
    if num2 > num1:
        print(num2,"Greater than",num1)
    elif num2 > num3:
        print(num2,"Greater than",num3)
        # num2 greater than equal any number
    if num2 >= num1:
        print(num2,"Greater than Equal",num1)
    elif num2 >= num3:
        print(num2,"Greater than Equal",num3)
        # num2 smaller than any Number
    if num2 < num1:
        print(num2,"Smaller than",num1)
    elif num2 < num3 :
        print(num2,"Smaller than",num3)
        # num2 <= any number
    if num2 <= num1:
        print(num2,"Smaller than Equal",num1)
    elif num2 <= num3:
        print(num2,"Smaller than Equal",num3)
    #               ( num3 )
    # num3 equal any number
    if num3 == num1:
       print(num3,"is Equal",num1)
    elif num3 == num2:
       print(num3,"is Equal",num2)
    # num3 doesn't equal any number
    if num3 != num1:
       print(num3,"doesn't Equal",num1)
    elif num3!= num2:
       print(num3,"doesn't Equal",num2)
    # num3 greater than any number
    if num3 > num1:
       print(num3,"Greater than",num1)
    elif num3 > num2:
       print(num3,"Greater than",num2)
    # num3 greater than equal any number
    if num3 >= num1:
       print(num3,"Greater than Equal",num1)
    elif num3 >= num2:
       print(num3,"Greater than Equal",num2)
    # num3 smaller than any Number
    if num3 < num1:
       print(num3,"Smaller than",num1)
    elif num3 < num2 :
       print(num3,"Smaller than",num2)
    # num3 <= any number
    if num3 <= num1:
      print(num3,"Smaller than Equal",num1)
    elif num3 <= num2:
      print(num3,"Smaller than Equal",num2)
    return num1,num2,num3
if A =="Assignment":
    num1, num2, num3 = int(input("Number 1 > ")), int(input("Number 2 > ")), int(input("Number 3 > "))
    Assignment(num1, num2, num3)
elif A == "extra credit":
    num1, num2, num3 = int(input("Number 1 > ")), int(input("Number 2 > ")), input("Number 3 > ")
    print("WARNING:", num3, type(num3))
    num3 = int(input("You Need to Convert it to intger \nWrite the Number Again I will Do that Dont Worry > "))
    Assignment(num1, num2, num3)
else :
    print ("Erorr:you Need to Type Assignment or extra credit" )
