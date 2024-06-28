A = [[1,2,3],
     [4,5,6],
     [8,0,10]]

B = [[12,3, 5],
     [7,6,4],
     [9, 90, 100]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        result [i][j] = A[i][j] + B[i][j]

for r in result :
    print(r)