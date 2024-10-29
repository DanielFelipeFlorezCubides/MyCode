fullName = input('Put your full name: ')
age = int(input('Put your age: ')) # Input function only save what you write as a string, if you need something else aside of a string we have to convert it.
gender = input('Put your possible gender options, M, F, X: ')
height = float(input('Put your height: '))

print(f""" 
    Hello user {fullName}, how are you? Python greets you.
    Thanks for share your age {age}, I didn't know you were a human {gender} type
    and your height were {height}.
""")