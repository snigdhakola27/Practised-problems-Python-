# union set
prsn1 = {"bat", "net", "brush", "cap", "chocolate", "bat"}
prsn2 = {"bat", "net", "brush", "cap", "pen", "book"}
prsn3 = prsn1 | (prsn2)
print(prsn3)

#or

prsn1 = {"bat", "net", "brush", "cap", "chocolate", "bat"}
prsn2 = {"bat", "net", "brush", "cap", "pen", "book"}
prsn3 = prsn1.union(prsn2)
print(prsn3)