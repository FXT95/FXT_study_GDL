from operator import index
import random


list_all=[]
list_title=[]
for i in range(1000):
    list_temp=[]
    list_temp.append("a"+str(i))
    list_temp.append(random.randint(50,100))
    list_all.append(list_temp)
    list_title.append("a"+str(i))


#search the a?
list_a=["a10","a20","a51","a66"]
for i in range(len(list_a)):
    a=list_a[i]
    #print(list_all[list_title.index(a)])
    print(str(list_all[list_title.index(a)][0])+"="+str(list_all[list_title.index(a)][1]))
    #print(list_all[list_title.index(a)][1])


