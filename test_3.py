# practical 1: 
#   preparation: there will be a list of spells you can use apis/ external source as well to pupopulate the initial list of spelling#   then our program will create pattern 1 in terminal. and also it will display the random spellings from list of initial spells with random alphabet replaced with _ and it will ask for spelling if spelling is correct then pattern will remain the same if spelling goes wrong it will add ----| if second spelling is incorrect then it will add another | to pattern and if pattern B completes it should print you loose there will be 10 spellings to be answered. if all the 10 answer will be correct then final pattern will remain same as pattern 1. and it will print you passed. to print pass you must give correct answer to all spells.

#   how to handle scenarios where partial answer is failed:#        in this scenario on 10th spell attempt it will show the pattern b if any of spell is incorrect
#   corner case:#   Fried - fired#   if this types of spelling in selected list and _ at both second and third place then either of
#  step 1: first create this pattern on initialization in terminal
#  how to add patterns on incorrect spells#   1 |#   2 |#   3 |#   4 |#   5 O#   6 -#   7 |#   8 -#   9 /#   10 \
# parretrn 1    |#           |#           |#           |#           |#           |#           |_________




# |----|# |  |# |  |# |    |# |  O# |   -|-# |  /\# |_________


# practical 2:


# minumum steps to solve the puzzle
# there will be a puzzle like = [ [$,#,#,$,#],[%,%,%,#,#],[$,$,%,$,%]]
# what you have to do is return minimum possible steps to sort this in this [[$,$,$,$,$],[%,%,%,%,%],[#,#,#,#,#]] Note: array will be dynamic
# for example to sort the first array we have to Move # from first array to 3rd array and from 3rd array we move $ to first array so it will considere 2 operations


# practical 3:
# [
#    [0,0,0,1,1,1,0,0,0],
 #   [1,0,1,0,1,1,5,6,7],
 #   [7,7,7,9,9,9,0,0,0],
 #   [0,0,0,1,1,5,0,0,7],
 #   [1,2,3,4,5,6,7,8,9],
 #   [1,1,0,0,0,0,3,7,8],
 #   [7,7,7,6,7,0,0,0,8],
 #   [6,5,1,1,0,0,0,3,3],
 #   [1,1,4,0,0,0,2,2,2]
# ]
# we make will return the some of I from given array array will be dynamic we can enter any dimention of array it should work with dynamic arrays

# 0[0] , 1[0] , 2[0] 
#        1[1] 
# 0[2] , 1[2] , 2[2]

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