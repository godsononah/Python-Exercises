import os

file = open('system_info.txt', 'w')
for line in os.popen('systeminfo'):
    file.write(line)
    file.flush()
file.close()

file = open('system_info.txt')
for line in file:
    print(line.rstrip())
