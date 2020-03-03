try:
    for i in range(1, 11):
        cases = input().split(' ')
        del cases[0]
        for j in range(len(cases)):
            cases[j] = int(cases[j])
        print('Case ' + str(i) + ':', min(cases), max(cases),
              str(int(max(cases)) - int(min(cases))))
except EOFError:
    pass
