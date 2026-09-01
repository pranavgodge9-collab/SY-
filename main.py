file = open("textfile.txt","r")
print(file.read())

file.seek(0)
total_lines = len(file.readlines())
print(total_lines)

file.seek(0)
lines = file.readlines()
two_lines = (lines[0],lines[1])
print(two_lines)


file.seek(0)
new_file = open("extracted.txt","w")
write = two_lines
new_file.writelines(write)

file.close()
new_file.close()


