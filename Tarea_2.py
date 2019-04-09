######### Crear líneas de código en Python que calcule el promedio de los valores contenidos en una lista.#####

New_list = [27,45,87,23,45,65]
def Average(New_list):
    return sum(New_list) / len(New_list)

average = Average(New_list)
# Printing average of the list
print("Average of the New_ list is =", round(average, 2))

### Escriba un código en python que determine cual grupo de personas contiene la mayor de todas las alturas de todas las personas ###

group1 =[177,145,167,190,140,150,180,130]

group2 =[165,176,145,189,170,189,159,190]

group3 =[145,136,178,200,123,145,145,134]

group4 =[201,110,187,175,156,165,156,135]

def Average1 (group1):
    return sum(group1) / len(group1)
average1 = Average1(group1)
print(round(average1,2))

def Average2 (group2):
    return sum(group2) / len(group2)
average2 = Average2(group2)
print(round(average2,2))

def Average3 (group3):
    return sum(group3) / len(group3)
average3 = Average3(group3)
print(round(average3,2))

def Average4 (group4):
    return sum(group4) / len(group4)
average4 = Average4(group4)

print(round(average4,2))

highestscore = max((average1,average2,average3,average4))
print("The group with the people most tall is the group4 with",  highestscore)




