
import random
zulu = 0
for i in range(1,10):
    i = random.randint(1,1000)
    zulu += i
print(zulu)

f = open("x-files.txt", "w")
while True:
    line = input("Give me text to put into a file: ")
    if line.lower() == "stop":
        break
    f.write(line + "\n")
f.close()

#with operation allows you not to have to specify the close
print("Hi :)")
searchVar = input("Enter what word you want to look for: ")

num_watch = 0
with open("x-files.txt","r") as f:
    for line in f:
        num_watch += line.lower().count(searchVar)

print("the word",searchVar, "shows up", num_watch,"times in the file.")
import random
def greet():
    """
    This is a basic function used for teaching.
    It just prints two lines of text.
    """
    print("Hello, World!")
    print("Bye World!")
    return 7

def operation_threenum(a,b,c):
    """
    This function sums 3 numbers
    :param a: the first number
    :param b: the second number
    :param c: the third number
    :return: the sum of the 3 numbers
    """
    return a * b + c
def read_threenum(e=0,f=0,g=0):
    """
    This function reads 3 numbers from the user
    :return: The 3 numbers
    """
    e = int(input("Enter first: "))
    f = int(input("Enter second: "))
    g = int(input("Enter third: "))
    return e, f, g

print(operation_threenum(a = 3, b = 7, c = 10))

zulu = read_threenum()
print(zulu[0] * zulu[2])

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst[1] = 11
lst[2] = lst[3] - lst[1]
print(lst)

r = ['a','b','c']
x = r.pop(1)
print(r)



