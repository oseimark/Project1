#Hash Table 

hash_table = list()
#Inserting an element in a hash table
def Insert(key, value):
    global hash_table
    hash_table[len(hash_table):] = [key]
    hash_table[len(hash_table)+1:] = [value]

#Searching an element in the hash table
def Search(key):
    location = hash_table.index(key)
    print(location)
    while location * 2 <= len(hash_table):
        return hash_table[(location-1) * 2 + 1]   #index offset start with 0 so we minus 1 of the key
        break
    
#deleting an element in hash table
def delete_(key):
    global hash_table
    hash_table.remove(Search(key))
    hash_table.remove(key)

    
Insert(1, ["Henry Siaw", "Computer Science"])
Insert(5, ["Mark Finley", "Computer Science"])
Insert(3, ["Daniel Atisika", "Computer Science"])

print(Search(5))





