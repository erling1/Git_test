import numpy as np

data = open("AdventOfCode1.txt", "r").read()

data1 = data.split("\n")


list1 = []
list2 = []

for i in range(len(data1)):
    if data1[i] != '':
        list1.append(int(data1[i]))
    else:
        list2.append(list1)
        list1 = []




k =[]
newlist2 = []

for i in list2:
    k.append(np.sum(i))
print(k)

helllllo












#for i in list2:
   # newlist3.append(eval(i))
   # print(newlist3)



#for i in list2:
    #newlist3 = list(map(int , list2[1]))



#for sublist in list2:
    #for string in sublist:
       # int1 = eval(string)
        #newlist2.append(int1)

#print(newlist2)







#for i in j:
    #for j in list2:
        #newlist2[i] = eval(list2[i][j])



#for n in list2:
    #newlist2 = eval
    #k.append(np.sum(eval(list2[n])))

#k.sort()

#test = list2[2]

#test1 = np.array([test]).astype(np.float)


#print(newlist2)

#print(k[-1])

#for line in data.readfiles():
    #result = eval(line)
    #line = line.split()
    #if line:
        #line = [int(i) for i in line]
        #lists.append(line)



#data.close()

#newList = [i[0] for i in lists]




#val = map(float, open("AdventOfCode1.txt"))

