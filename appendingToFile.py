# Writing text to file will clear existing data
# Appending text to file will add further text but will not delete existing data
appendMe = '\nAppending this to the file!'
appendFile = open('exampleFile.txt', 'a')
appendFile.write(appendMe)
appendFile.close()