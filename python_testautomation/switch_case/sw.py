#sw
num1 = 20
if( num1 >= 30 ):
        print(" 30 ")
elif( num1 == 10 ):
        print(" 10 ")
elif( num1 == 5 ):
        print(" 5 ")
else:
        print(" 20 ")

#case2


def switch(lang):
    if(lang == "hello"):
        return "hello"
    elif(lang == "hello1"):
        return "hello1"
    elif(lang == "hello2"):
        return "hello2"
    elif(lang == "helloX"):
        return "helloX"

print(switch("hello2"))  

#sw3
lang: str = "hello1"
match lang:
    case "hello1":
        print("hello1")
    case "hello2":
        print("hello2")
    case "hello3":
        print("hello3")
