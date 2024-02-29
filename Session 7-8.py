#string: a union of letters, can be subdivided

cars = ["audi", "bmw", "subaru"]
for i in cars:
    print(cars[1])

sulfuric = "sand"

for j in sulfuric:
    print(j)

name = "John"
second_name = "Sebastian"

text = f"Hi, {name} how are you? My name is {second_name}"
print(text)

name = "Jane"
second_name = "Mary"
text = f"Hi, {name} how are you? My name is {second_name}"
print(text)

s = "https://www.google.com/ and then there could be https://yahoo.com"
start = 0
while True:
    start = s.find("https://")
    if start == -1:
        break
    end = s.find(" ", start)
    if end == -1:

        text = "abcdefghijklmnopqrst"
        print(dir(text))

        print("anananananananan".count("ana"))
        print("anananananananan".replace("ana", "banana"))
        print("ananananananan".find("ana", 1))
        print("ananananananan".split("a"))
        print("this is a sentence and I want the words".split(" "))
        sentence = "Hello, kind sir, how may I be of service today?"
        punctuation = ".,;!?-"
        # sanitize the sentence
        for p in punctuation:
            sentence = sentence.replace(p, " ")  # replace the punctuation with nothing

        print(sentence)
        sentence = sentence.replace("  ", " ")
        # split the sentence into words
        words = sentence.split(" ")
        print(words)
base = "abcdefghijklmnopqrstuvwxyz"
print("here are some slices")
print(base[0:3])
print(base[10:])  # all the way till the end
print(base[:10])  # all the way from the beginning
print(base[:])  # the whole string

print(base[::2])  # every other letter
print(base[5:15:3])  # from 5th character to the 14th, in steps of 3
print(base[::-1])  # the whole string backwards

# my solution
hi = "Hello!"
i = -1
while i != -1 -len(hi):
    print(hi[i])
    i = i - 1

text = "abcdefghi"
i  = 0
while i < len(text):
    print(text[len(text)-1-i])
    i += 1


