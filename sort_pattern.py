# PRACTICAL 2

arr =   [ 
            ['$','#','#','$','#'],
            ['%','%','%','#','#'],
            ['$','$','%','$','%'],
            ['$','#',"&","%","#"]
        ]
new_arr = []
new_dict = {}


for i in arr:
    for j in i:
        new_arr.append(j)
        if j not in new_dict.keys():
            new_dict[j] = []

for i,element in enumerate(new_arr):
    last_index = len(new_arr)-1-i
    new_dict[element].append(element)

print(list(new_dict.values()))