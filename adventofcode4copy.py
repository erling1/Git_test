assigments = open("adventofcode4.txt","r").read()


 
pairofelves = assigments.split("\n")
elf = []

for i in pairofelves:
    elf.append(i.strip("-"))



print(elf)