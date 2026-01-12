from pathlib import Path
# Write a file (mode 'w' overwrites)
file_path = "data.txt"
f = open(file_path, "w", encoding="utf-8")
f.write("Alice")
f.close()

# Append a second line
f = open(file_path, "a", encoding="utf-8")
f.write("\nBob")
f.close()

#print(Path(file_path).read_text(encoding="utf-8"))
with  open(file_path, "a", encoding = "utf-8") as f:
    f.write("\nabc1234")
with open(file_path, 'r', encoding="utf-8") as f:
    print(f.read())