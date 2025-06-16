import numpy as np

a=np.random.randint(50, size=(5,4))
print(f"Array:{a}")


# Extracting the elements across anti-diagonal
i=0
k=3
print("The elements across anti-diagonal are:")
while(k>=0):
    print(a[i][k])
    i+=1
    k-=1

# Maximum value in each row of the array
print("The maximum value in each row the array respecitvely are:")
for i in range(0,5):
    max=a[i][0]
    for j in range(1,4):
        if(a[i][j]>max):
            max=a[i][j]
    print(max)

# A new array "b" which contains only the elements less than or equal to the overall mean of the initial array "a"
print("New array with elements less than or equal to the overall mean of initial array:")
mean_a = a.mean()
b=a.copy()

for i in range(0,5):
    for j in range(0,4):
        if(b[i][j]<=mean_a):
            continue
        else:
            b[i][j]=0       
print(b)

# Supposed ki we are solving this subpart under the given case of a numpy with size of (5,4)
result = []
def numpy_boundary_tranversal(matrix):
    rows=5
    cols=4
    # Top row
    for k in range(cols):
        result.append(int(matrix[0][k]))
    
    # Right-most column (excluding top corner)
    for i in range(1, rows):
        result.append(int(matrix[i][cols - 1]))
    
    # Bottom-most row (excluding right corner)
    if rows > 1:
        for k in range(cols - 2, -1, -1):
            result.append(int(matrix[rows - 1][k]))
    
    # Left-most column (excluding top and bottom)
    if cols > 1:
        for i in range(rows - 2, 0, -1):
            result.append(int(matrix[i][0]))

numpy_boundary_tranversal(a.copy())
print(result)
