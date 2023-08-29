word = input(": ").replace(" ", "")
print("Si es" if word[::-1] == word else "No es")