import string

import random

num = string.digits

cha = string.ascii_lowercase

pn = 139/6

coz = 609 / 139

depart = ["a", "b", "c", "d", "f", "e"]

program = []

ocz = []
module = []


for i in depart:
    pre_prog = []
    for j in range(int(pn)):
        progrm = f"{i}{random.choice(num)}{random.choice(cha)}"

        pre_prog.append(progrm)
    program.append(pre_prog)


for i in program:
    pre_coz = []
    for j in i:
        module = []
        for k in range(int(coz)):
            modul = f"{j}{random.choice(num)}{random.choice(cha)}"
            pre_coz.append(modul)
        module.append(pre_coz)
        pre_coz = []
    ocz.append(module)

print(program)
