### Escriba un código en python que determine cual grupo de personas contiene la mayor de todas las alturas de todas las personas ###

group1 =[177,145,167,190,140,150,180,130]

group2 =[165,176,145,189,170,189,159,190]

group3 =[145,136,178,200,123,145,145,134]

group4 =[201,110,187,175,156,165,156,135]

def Average(group):
    average = sum(group) / len(group)
    return average

average1 = Average(group1)
print("Group1, " + str(round(average1, 2)))

average2 = Average(group2)
print("Group2, " + str(round(average2, 2)))

average3 = Average(group3)
print("Group3, " + str(round(average3, 2)))

average4 = Average(group4)
print("Group4, " + str(round(average4, 2)))

highestscore = max((average1,average2,average3,average4))
print("The group with the people most tall is the group2 with",  highestscore)
#############################################
Ouput 

Group1, 159.88
Group2, 172.88
Group3, 150.75
Group4, 160.62
The group with the people most tall is the group2 with 172.875

Process finished with exit code 0
