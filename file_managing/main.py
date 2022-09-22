file = open("file_managing\demo.txt", "w")
file.write("This is the text written to the file ")
file.close()

file = open("file_managing\demo.txt", "r")
content = file.read()
print(content)


file = open("file_managing\demo.txt", "a")
file.write("This is the new line ")
file.close()
