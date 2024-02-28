path = "a.fa"
with open(path, "r") as f:
    c = f.read().count(">")
print(c)
