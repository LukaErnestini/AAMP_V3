import csv

def matrix_mult(a, b):
    sum = 0
    for i in range(len(a)):
        sum += a[i] * b[i]

    return sum

reader = csv.reader(open("Linearna funkcija/Podatki.txt"), delimiter=" ")

x, y = [], []
next(reader) 
for row in reader:   
    x.append(float(row[0]))
    y.append(float(row[1]))

X = matrix_mult(x, y)
print(X)