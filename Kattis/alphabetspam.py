spam = input()
whitespace = []
lowercase = []
uppercase = []
symbols = []

for i in spam:
    if i == '_':
        whitespace.append(i)
    elif i.islower():
        lowercase.append(i)
    elif i.isupper():
        uppercase.append(i)
    else:
        symbols.append(i)

print(str(len(whitespace) / len(spam)))
print(str(len(lowercase) / len(spam)))
print(str(len(uppercase) / len(spam)))
print(str(len(symbols) / len(spam)))