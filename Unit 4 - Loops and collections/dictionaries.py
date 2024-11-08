## Dictionary is a type of collection like a list
# alist is a collection of items in a sequence
# a dictionary is diff
# Dictionaries store data in key-value pairs
# You can retreive data quickly by using a unique key
# instead of by index (position)

# Example
# lists use brackets [], dictionaries use braces{}

kaden = {
    "name"  : "Kaden",
    "age"   : 18,
    "city"  : "St. Michael",
    "pets"  : 4,
    "height": 5.10
}

# Each key must be unique

# Retrieving values from a dictionary
print(kaden["age"]) #prints age


#This will error if key doesnt exist: KeyError


# .get allows you to retreive a value without erroring
# when the key doesn't exist
# second parameter is what is given if key does not exist

print(kaden.get("height"))
print(kaden.get("country", "Location not found."))

# You can add new values to an existing dictionary
kaden["country"] = "USA"

#You can modify existing values
kaden["age"] = 18.4

# You can remove existing values
kaden.pop("pets")

#iterate through dictionary using for loop!
for key, value in kaden.items():
    print(key+ " = " +str(value))
# Dictionary Functions
print(kaden.keys()) #returns all keys
print(kaden.values())#returns all values
print(kaden.items())#returns all key-value pairs
print(kaden.clear())#removes all items from dictionary