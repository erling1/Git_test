assigments = open("adventofcode4.txt","r").read()

pairofelves = assigments.split("\n")
elf = []
elf_final = []

for i in pairofelves:
    #a = i.split(",")
    #i.split(",")
    elf.append(i.split(","))

eachelf = []

for i in elf:
    eachelf.append(i[0])
    eachelf.append(i[1])

list1 = []
for i in eachelf:
    a = i.split("-")
    list1.append(i.split("-"))
    
Lower_range = []
Higher_range = []

for i in list1:
    Lower_range.append(i[0])
    Higher_range.append(i[1])
    
Overlapping_departments = []

for i in range(len(Lower_range)):
    if Lower_range[i-1]<Lower_range[i] and Higher_range[i-1] >Higher_range[i]:
        Overlapping_departments.append(1)
        

print(sum(Overlapping_departments))




