def get_value():
    data = {"a": 1, "b": 2}
    return data.get("c", "Key not found")
print(get_value())