try:
    f = open('classes/test', 'r')
    print(f.read())
    f.close()
except FileNotFoundError as e:
    print("Error: The file was not found.", e)

