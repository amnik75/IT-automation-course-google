import csv

with open('csv_file.csv') as file:
    f = csv.reader(file)
    for r in f:
        n,f,b = r
        print(r)

names = [['amir','nik'] ,['amin','nik']]
with open('my_file.csv','w') as f:
    w = csv.writer(f)
    w.writerows(names)

# It reads the first line of the file to observe keys then we can access each row with dictionary and keys
with open ('humans.csv') as h:
    r = csv.DictReader(h)
    for row in r:
        print("name:{} family:{}".format(row['name'],row['family']))

# It first write header to the file and then we can write the information to the file with dictionary
humans = [{'name':'amir','family':'nik'},{'name':'amin','family':'pir'}]
keys= ['name','family']
with open('humans.csv','w') as h:
    w = csv.DictWriter(h,fieldnames=keys)
    w.writeheader()
    w.writerows(humans)
