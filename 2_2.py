string = input("Введите строку: ")

result = { }
for c in string.lower():
    if c != ' ': 
        c_count = string.lower().count(c)
        result[c] = c_count

print(f"\n{result}")
