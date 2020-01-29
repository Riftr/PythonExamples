# Dictonary - key value pairs
#  - refer to it by its key
#  - use camel case 

#Basic dictionary
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

# Access different ways

# By Key
print(monthConversions["Nov"])

# By Get (can specify a default value if not found)
print(monthConversions.get("Dec"))
print(monthConversions.get("Luv"))  # returns None
print(monthConversions.get("Luv", "Not a valid key")) # returns default value instead


# By Index - note *3.7* onwards is order preserving, before that they were orderless
# This code puts the dict into a list to get them
# https://stackoverflow.com/questions/4326658/how-to-index-into-a-dictionary
print(list(monthConversions)[0])
print(list(monthConversions)[1])
print(list(monthConversions)[2])

# Another way of accessing by index by avoiding copying to a list
def get_first_key(dictionary):
    for key in dictionary:
        return key
    raise IndexError

first_key = get_first_key(monthConversions)
print(get_first_key(monthConversions))
print(monthConversions[first_key])
