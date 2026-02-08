#create set

set = {1,3,5,6}
set1 = {5,4,6,3,1}
print("The First set is :", set)
print("The second set is :", set1)

#Accessing Element 

for number in set :
    print(number)

#union of the set & set1

Union_set = set & set1
print('The Union set of set & set1 is :',Union_set)

#Intersection of set & set1

Intersection_set = set | set1
print("The Intersection of set & set1 is:",Intersection_set)

