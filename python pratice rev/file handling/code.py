# Writing to a file (overwrites if file exists)
with open('example.txt', 'w') as f:
    f.write('This is a new file.\n')

# Appending to a file (adds to the end)
with open('example.txt', 'a') as f:
    f.write('This line is appended.\n')

# Reading from a file
with open('example.txt', 'r') as f:
    content = f.read()
    print(content)