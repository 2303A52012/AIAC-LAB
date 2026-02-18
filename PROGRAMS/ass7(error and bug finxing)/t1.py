# Bug: Mutable default argument
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
print(add_item(1,[6,8,9]))
print(add_item(2))

# [6, 8, 9, 1]
# [2]