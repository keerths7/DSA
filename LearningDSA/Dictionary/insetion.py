# Time Complexity- O(1)
# Space Complexity- O(1) 

my_dict = {"name": "Keerthana", "age": 23, "address": "India", "hobby": "reading"}
my_dict["name"] = "Keerthi"     # updating value of a key
my_dict["city"] = "Chennai"     # inserting a key value pair


# Amortized Cost:
# When the dictionary is half full and we add more items, the dictionary's size is doubled 
# to make room for more entries. This resizing happens occasionally, so the cost of resizing 
# is spread out over many insertions, keeping the average time per operation fast.

'''
Hash Function: When you insert a key-value pair into a dictionary, the hash function computes a hash value for the key. This hash value is used to determine the index (or bucket) where the key-value pair should be stored in the hash table.
Direct Access: Once the hash value is computed, you can directly access the location where the key-value pair is stored in the hash table. Since hash tables allow fast lookups, updates (or modifications) to the value associated with a key can be done in constant time, O(1), without having to move or shift any other entries.
Updating Values: If you update a value for an existing key (as in my_dict["name"] = "Keerthi"), you simply update the value at the corresponding hash table index without needing to reorganize the entire structure.
Inserting New Keys: Similarly, when you insert a new key-value pair (as in my_dict["city"] = "Chennai"), the hash function calculates the appropriate index for the new key, and the new pair is inserted directly at that location.
'''