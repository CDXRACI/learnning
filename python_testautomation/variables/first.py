import math 
#variable
name = "cao_dai_phucd"
salary = 1000
#define variable with spec data type
name1: str = " hello "
salary1: int = " 2000 "


#print
print("Hello cao dai phuc", name)

print ( "var 1", name1 )
print ( " salary1 ", salary1 )
#datatype
print("--> Hello ", type( name ))
print("--> Hello ", type( salary ))
#print with specific character
print("hello\ncdp") # using \ not use \"
print(len(name))
print(name.find('a'))
print(name.lower())
print(name.upper())
#is behind check correct or not correct
print(name.isupper()) 
print(name.islower())
print(name[2])

#------------------NUMBER-----------------------------
fl_var: float = 0.222
in_var: int  = 123
in_var2: int = 34
print(fl_var)
print((in_var*in_var2))
print(" hello world", in_var)
print(10%3)
print(abs(-2))
print(pow(3,2))
print(math.sqrt(4))
print(max(2,5))
print(min(1,3))
print(round(3.812, 3))
#print("hello world "  +  in_var ) // wrong

#---------------------Input-----------------
var_str1: str = input("please typing in the input: ")
var_str2: str = input("enter your name: ")
print("hello" + var_str1 + " xin chao" + var_str2 )
