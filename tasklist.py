import os

file = open('tasklist.txt', 'w')
for line in os.popen('tasklist'):
    file.write(line)
    file.flush()
file.close()

file = open('tasklist.txt')
for line in file:
    print(line.rstrip())
