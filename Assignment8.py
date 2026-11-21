file=open("hello.txt","r")
lines=file.readlines()
for i in lines:
    print(i)



linecount=len(lines)
print(linecount)

extract_line=lines[:2]
for i in extract_line:
    print(i)

file.close()


new_file=open("hii.txt","a")
new_file.writelines(extract_line)
new_file.close()
