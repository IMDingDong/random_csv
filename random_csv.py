import csv
import random

num_list = []

for i in range(1000000):
    num = str(random.randint(1, 1000000))
    num_list.append(num)

f = open('numbers.csv', 'w', newline='')
writer = csv.writer(f, delimiter=",")
writer.writerow(num_list)

f.close()
