from pymongo import MongoClient

client = MongoClient()
db = client.PIK3CA

## Read input
cursor = db.vcf.find()
## Set counter
x=0

## Formatted string; 5 columns
string = '{}\t' * 5
print(string.format("CHR", "POS", "DEPTH S2", "DEPTH S3", "COUNTER"))

## Loop through your input and print only lines with S2 Depth && S3 Depth greater than 7
for document in cursor:
    chromo = document['chr']
    pos = document ['pos']
    DStwo = document['samples'][2]
    DSthree = document['samples'][3]

    if DStwo > 7 and DSthree > 7 :
        x += 1
        print(string.format(chromo, pos, DStwo, DSthree, x))



