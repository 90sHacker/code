import csv
import random


male = []
female = []

def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

def grouper(list):
    group = {}
    for i, val in enumerate(list):
        group[f'Group {i+1}'] = val

    return group

with open('staff.csv') as staff:
    csv_reader = csv.DictReader(staff)
    for row in csv_reader:
        if(row['Gender'] == 'M'):
            male.append(row['Name'])
        else:
            female.append(row['Name'])


male_list = random.sample(male, len(male))
female_list = random.sample(female, len(female))
print(len(male_list))
print(len(female_list))

#split the male into 4 equal
team = []
splitter = list(split(male_list, 4))
splits = list(split(female_list, 4))

# print(splitter)
# print(splits)
for i in range(4):
    splitter[i].extend(splits[i])

groups = str(grouper(splitter))

f = open('groupfile.txt', 'a')
f.write(groups)