1. print("")
1.1 gan 1 bien string = " "
1.2 ("" + 'content ' "") cong 1 chuoi string ben ngoai vao trong
1.3 cac ky tu dac biet trong python
	\n newline
	\r return
	\t tab
	-> in dau " \"
1.4 
g_string.lower
g_string.upper
g_string.islower() -> yes return true
		   -> wrong return false
g_string.isupper() //

g_string.upper.isupper() # right

len(phrase) -> return length

g_string.index("character/string") -> find where character is
g_string.replace("des","tar") -> replace tar by des string

1.5 thuat toan 
uu tien trong ngoac truoc ngoai ngoat sau ()

abs() -> lay tri tuyet doi
pow() -> lay can 2 pow(4,3 ) = 4x4x4
max() -> lay gia tri lon nhat giua 2 so ( a, b)
min() -> lay so nho nhat giua 2 so ( a, b)
round() -> lam tron so 111.23 => 111
sqrt() -> lay can 

+ - * / %
input() <=> scanf
name = input("enter your name")
print(name)

2. # comment

3. list # liet ke 1 loat danh sach
list = []


list 
list = ["string", number]
-> liet ke cac thanh phan su dung
print(list)
print(list[0]) -> in thanh phan
print(list[0:1]) -> in thanh phan 0,1

list[0] = "hello" // gan
av  = list[0] // doc
---------------------------
list functions

random_number = [ 1,3,4,6,7]
list = ["kevil", " du", " jim " ]
list.extend( random_number ) // noi chuoi list bang random_number
print(list)

list.append("odx") // noi odx vao list
list.insert(1, "odx") //chen du bangg odx trong list , tang phan tu list len 1 don vi day du ra vi tri so 2
	("kevil", "odx", "du", "jim ")
list.remove("jim") // remove jim ra khoi list
list.clear() xoa cac phan tu 
list.index("kevil") in ra vi tri phan tu
list.count("kevil") dem xem trong list co may kevil
list.sort() // sap xep bang cach dung ki tu nho nhat o dau moi phan tu trong list de sap xep
list.reverse() dao nguoc cac vi tri cua phan tu trong list
list1 = list.copy() gan chuoi list cho list1


------------------------------

tuples
