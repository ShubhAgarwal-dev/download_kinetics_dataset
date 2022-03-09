import json

with open(r'resources\classes.json', mode='r') as file:
    classes = json.load(file)
    file.close()

if '__name__' == '__main__':
    for cls in classes:
        print(cls)
