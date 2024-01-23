# get the file
with open("ASSIGNMENT.MD", "r", encoding="utf-8") as f:
    content = f.read()

# capitalize the first letter of each word
content = '\n'.join(' '.join(word.title() for word in line.split()) for line in content.split('\n'))

# write the file
with open("ASSIGNMENT-out.md", "w", encoding="utf-8") as f:
    f.write(content)
