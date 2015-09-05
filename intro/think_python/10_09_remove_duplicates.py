
'''
Write a function called remove_duplicates that takes a list and returns a new list
with only the unique elements from the original. Hint: they don't have to be in the same order

'''

def remove_duplicates(t):
    c = t[:]
    c.sort()

    new = []
    new.append(c[0])

    for i in range(len(c)-1):
        if c[i] != c[i+1]:
            new.append(c[i+1])
    return new


test1 = [1,2,3,4,5]
test2 = [1,2,2,2,3,3,4,5]
test3 = [1]

print remove_duplicates(test1)
print remove_duplicates(test2)
print remove_duplicates(test3)


# Not sure what the author was getting at by saying they don't have to be
# in order. By simply traversing the list, we can match the two conditions,
# that the item is a duplicate (>1) in items but does not already exist
# (<1) in newList. Once those conditions are met than we can append
# whatever i to newList.

def remove_duplicates2(items):
    newList = []
    for i in items:
        if items.count(i) > 1:
            if newList.count(i) < 1:
                newList.append(i)
        i += 1
    print items
    print newList

items = [1, 1, 2, 4, 5, 6, 7, 8, 8, 9, 10, 7]

remove_duplicates2(items)

def remove_duplicates3(input_list):
    '''For each item in the list see if there is a duplicate.'''
    # create empty dictionary to store key/value pairs
    unique_item_dict = {}
    removed_duplicates_list = []
    for item in input_list:
        # if already existing, pass
        if unique_item_dict.has_key(item):
            pass
        # otherwise, add to dict
        else:
            unique_item_dict[item] = 1

    # create new list based on dict key values
    for dict_item in unique_item_dict.iterkeys():
        removed_duplicates_list.append(dict_item)

    return removed_duplicates_list
