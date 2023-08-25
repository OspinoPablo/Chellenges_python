word = input(": ")
word_clone = ""
word.lower()

for i in word:
    
    if i != " ":
        word_clone += i

print("Si" if word_clone[::1] == word_clone else "No")