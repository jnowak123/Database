with open('DANE/wykreslanka.txt') as f:
    arr = [list(x.strip()) for x in f]

rows = []
for i_row, row in enumerate(arr):
    for i in range(len(row)):
        if ''.join(row[i:i+6]) == 'matura':
            rows.append(i_row)

columns = []
for col_i in range(len(arr[0])):
    for row_i in range(len(arr) -5):
        if ''.join([arr[row_i][col_i], arr[row_i+1][col_i], arr[row_i+2][col_i], arr[row_i +3][col_i], arr[row_i +4][col_i], arr[row_i +5][col_i]]) == 'matura':
            columns.append(col_i)

print(rows, columns)

maxlen = 0
res = []
for i_row, row in enumerate(arr):
    repeat = 1
    for i in range(len(row) -1):
        if row[i] == row[i+1]:
            repeat += 1
        else:
            repeat == 0
        if repeat > maxlen:
            res = [i_row]
            maxlen = repeat
        elif repeat == maxlen:
            res.append(i_row)
print(maxlen, res)