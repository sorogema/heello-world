contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]
name = input()

for i in contacts :
    if name == i[0]:
        print(name + ' is ' + str(i[1]))
        break
else :
    print('Not Found')
