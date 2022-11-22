import os
path = "D:/hatt6/Zalo_AI_Cha/FAS/dataset/fake/"
counter = 0
list_del = []
for file in os.listdir(path):
    if (counter % 7) == 0:
        list_del.append(path+file)
    counter += 1
for each in list_del:
    os.remove(each)