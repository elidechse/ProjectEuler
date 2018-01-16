filename = "p082_matrix.txt"

f = open(filename, "r")
data = f.readlines()
f.close()

new_data = []

for i in range(len(data)):
    new_data.append([int(x) for x in data[i].split(",")])

N = len(new_data)
aux = new_data * 1


for col in range(N - 1, -1, -1):

    column = []
    for i in range(N):
        column.append(aux[i][col])

    for row in range(N - 1, -1, -1):
        if col == N - 1:
            aux[row][col] = aux[row][col]
        else:
            temp = aux[row][col] + aux[row][col + 1]
            for i in range(N):
                curr = sum(column[min(i, row): max(i, row) + 1]) + aux[i][col + 1]
                if (curr <= temp):
                    aux[row][col] = curr
                    temp = curr

column = []
for i in range(N):
    column.append(aux[i][0])
print(min(column))

