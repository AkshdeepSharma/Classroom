N = int(input())
simonCommand = "Simon says "
for i in range(N):
    command = input()
    if command.startswith(simonCommand):
        print(command[11:])
