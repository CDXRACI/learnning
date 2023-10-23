#dicionary as structure
confis = {
    "browser":"opera",
    "aut":"google site",
    "test": "smoke",
    "log": True
}


def func_var1():
    name: str = "phuccd"
    salary: int = 1500
    print("Hello world")
    print("name is: " + name )
    print(" salary is ", + salary )

func_var1()

def getDic(key):
    return confis.get(key)

print(getDic("browser"))