import random
while True:
    file = open("vocs.txt", "r")
    dict = {}

    for line in file:
        if ' ' in line:
            data = line.split(' ')
            dict[data[0]] = data[1][:-1]
        if '-' in line:
            data = line.split('-')
            dict[data[0]] = data[1][:-1]
        if '  ' in line:
            data = line.split('  ')
            dict[data[0]] = data[1][:-1]
        if '    ' in line:
            data = line.split('    ')
        if ':' in line:
            data = line.split(':')
            dict[data[0]] = data[1][:-1]
        if '   ' in line:
            data = line.split('   ')
            dict[data[0]] = data[1][:-1]
    file.close()

    word = random.choice(list(dict.keys()))
    answ = input(word+":")
    if answ == dict[word]:
        print("True")
    else:
        print(dict[word], "!!")
