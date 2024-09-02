x = 84

if x == 15:
    print("x is equal to 15")

elif x != 15:
    print(f"x does not equal 15, it equals {x}")
    if x < 15:
        print(f"In order for x to equal 15, you must add {15-x}")
    elif x > 15:
        print(f"In order for x to equal 15, you must subtract {x-15}")

# Fun math shit

a = 8

b = 9

type = "Subtract" # Options: Add, Subtract, Multiply, Divide

def math(num1,num2,type):

    if type == "Multiply":
        print(f"{num1} multiplied by {num2} is: {num1*num2}")
        
    elif type == "Subtract":
        print(f"{num1} minus {num2} is: {num1-num2}")

    elif type == "Add":
        print(f"{num1} plus {num2} is: {num1+num2}")

    if type == "Divide":
        print(f"{num1} divided by {num2} is: {num1/num2}")
    
math(a, b, type)