A = [[1,2,3],
     [4,6,7],
     [4,8,9]]

B = [[23,45,6],
     [12,13,15],
     [1,1,2,]]

Result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            Result[i][j] += A[i][k] * B[k][j]
for i in Result:
                 print(i)  

