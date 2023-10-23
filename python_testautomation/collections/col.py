# collection as array
hello = ["hello1","hello2", "hello3"]
print(hello[2])
print(hello[0:3])
#for
for hellox in hello:
    print(hellox) 

#dicionary as structure
confis = {
    "browser":"opera",
    "aut":"google site",
    "test": "smoke",
    "log": True
}

print(confis.get("aut"))
for var1 in confis.values():
    print(var1)
if "var1" in confis:
    print("Exist")