# You start a fucntion using def which means defining a function
# A basic function without parameters
def example():
    print("A basic function.")
    number1 = 5 + 9
    print(number1)

example()    
# Function with parameters
def simple_addition(num1, num2):
    print(num1,"+",num2, "=")
    total = num1 + num2
    print(total)

simple_addition(5, 5)    

#------
def simple(var1, var2=4):
    print(var1, "and",var2)

simple(5)    
# -----
def basic_window(width, heigh, font="TNR",
                bgc="White", scrollbar=True):
    print(width, heigh, bgc, font)      

basic_window(500, 350)
basic_window(500, 350, bgc="Blue")       
