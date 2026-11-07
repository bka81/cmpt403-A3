

# read the cipher files and save them as raw bytes:
with open("ctext0", "rb") as f:
    data = f.read()

print(len(data))
print(list(data[:10]))