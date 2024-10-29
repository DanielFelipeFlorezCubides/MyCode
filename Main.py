name = input('Tell me your name: ')
sentence = (f'hello world {name}')
print(sentence)

name = 'Daniel Felipe Florez Cubides' # Variable string type
age = 20 # Variable int type
height = 1.781 # Variable double type
trainer = False # Varible tipo boolean
hobbies = ['Programacion', 'Deportes', 'Musica'] # Variable list or array type
direction = (dict) ["country": "Colombia", "State": "Santander"] # Object type

# The things you cannot do with variables types
# nombre 1 = miguel//
# try to combine different types, example: print("Pi") is still a string, not int type

print(name, '\n', age) # '\n' is used for create the same function as enter in the same print line

print(f"""
    Student's name: {name}\n    Student's age: {age}
""")                            # Correct way to concatenate and keep a clean code