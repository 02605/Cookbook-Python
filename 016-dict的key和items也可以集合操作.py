a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    's': 2,
    'x': 1
}

print(a.keys() - b.keys())
comm = a.items() & b.items()
print(comm, type(comm))