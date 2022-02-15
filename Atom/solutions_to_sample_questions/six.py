def display_names(names):
    for i, name in enumerate(names):
        if i == len(names) - 1:
            print(name)
        else:
            print(name, end=", ")        

def display_B(names):
    for name in names:
        if name[0] == 'B':
            print(name)


names = ["Fred", "Barb", "Morris", "Alice", "Bob", "Wanda"]
display_names(names)
display_B(names)
names.sort()
print(names)
names.sort(reverse=True)
print(names)