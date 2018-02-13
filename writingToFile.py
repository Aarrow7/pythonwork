text = "Sample writing file \nNew line!"

# Using write will remove existing data in the file
saveFile = open('exampleFile.txt', 'w')
saveFile.write(text)
saveFile.close()