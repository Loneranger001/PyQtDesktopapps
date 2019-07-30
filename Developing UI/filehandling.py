
line_number = 1
with open('tran_data.tsv', 'r') as file:
    for line in file.readlines():
        if line_number != 1:
            columns = line.split()
            print('Item {0} and Location {1}'.format(columns[0],columns[1]))
        line_number += 1