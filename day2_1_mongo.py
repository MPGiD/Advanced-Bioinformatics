from pymongo import MongoClient

client = MongoClient()
db = client.PIK3CA

## Set db
cursor = db.vcf.find()
## Set counter
x=0

for document in cursor:
##    print("ENST00000263967" in document["ann"])

    subset = ((document["ann"]))
##    print(subset)
    item = subset.split("|")[6]
    if item == "ENST00000263967":
            x += 1


print(x)
