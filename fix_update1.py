import os
import re

for file in os.listdir():
    if '.txt' in file:
        file_name = str(file).replace('.txt','')
        with open(file, 'r') as read:
            names = sorted(set(read.readlines()))
            k = []
            for name in names:
                try:
                    formated_name = str(name.rstrip()).split('\t')[2]
                except:
                    formated_name = str(name.rstrip())
                if re.match("^[a-zA-Z0-9_]{2,16}$", formated_name):
                    k.append(name)
                else:
                    print(f'Not matched name: {name}')
            # names = [name for name in names if re.match(r"^[A-Za-z0-9_]{2,16}$", name.rstrip())]
        with open(f'{file_name}_output.txt', 'w') as write:
            write.writelines(k)