
my_dict = {0:"Hello", 1:"World", 2: "Python", 3:"Programming"}
print(my_dict[0])

my_dict2 = {"Hello":0, "World":1, "Python":2, "Programming":3, "Language": 4}
print(my_dict2["Hello"])

# Add elem to dict
my_dict[5] = "New"
print(my_dict)

# Change existing elem
my_dict[0] = "Hi"
print(my_dict)

my_dict[1] = ["this", "can", "be", "a", "list"]
print(my_dict)

# How to use the get method
print(my_dict.get(0))
print(my_dict.get(6))
print(my_dict.get(6, "Not found"))

# Use of keys and value methods
print(my_dict.keys())
print(my_dict.values())

# Use of items method
print(my_dict.items())

for key, value in my_dict.items():
    print(f"key: {key}, value: {value}")

wordfreq = {}
punctuation = ".!,?\n"
with open("Dracula.txt") as file:
    for line in file:
        print(line, end="")
        for p in punctuation:
            line = line.replace(p, "")
        line = line.lower()
        words = line.split(" ")
        for word in words:
            if len(word) < 5:
                continue
            wordfreq[word] = wordfreq.get(word, 0) + 1

topfreq = list(wordfreq.values())
topfreq.sort(reverse=True)
topfreq = topfreq[:10]
print(topfreq)

for word, freq in wordfreq.items():
    if freq in topfreq:
        print(f"{word}: {freq}")

for topword in topfreq:
    for key in wordfreq:
        if wordfreq[key] == topword:
            print(f"{key}: {topword}")
            del wordfreq[key]
            break

def print_b_words(file_name):
    punctuation = ",.!?\n"
    with open(file_name, 'r') as file:
        for line in file:
            for p in punctuation:
                line = line.replace(p, "")
            words = line.split(" ")
            for word in words:
                if word.startswith(('B')) and len(word) == 3:
                    print(word)

print(print_b_words("Yankee.txt"))
