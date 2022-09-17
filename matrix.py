# PRACTICAL 3

matrix = [
  [0,0,0,1,1,1,0,0,0],
  [1,0,1,0,1,1,5,6,7],
  [7,7,7,9,9,9,0,0,0],
  [0,0,0,1,1,5,0,0,7],
  [1,2,3,4,5,6,7,8,9],
  [1,1,0,0,0,0,3,7,8],
  [7,7,7,6,7,0,0,0,8],
  [6,5,1,1,0,0,0,3,3],
  [1,1,4,0,0,0,2,2,2]
]
sum_arr = []
for i in range(int(len(matrix)/3)):
    i = i*3
    first =  matrix[i]
    second = matrix[i+1]
    third =  matrix[i+2]
    for j in range(int(len(first)/3)):
        j = j*3
        sum_arr.append(first[j]+second[j]+third[j]+second[j+1]+first[j+2]+second[j+2]+third[j+2])
print(sum_arr)