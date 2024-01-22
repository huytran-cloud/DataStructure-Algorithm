database = set()
while True:
    key = input().strip()
    if key == '*':
        break
    database.add(key)

while True:
    operation, key = input().strip().split()
    if operation == '***':
        break
    if operation == 'find':
        print(1 if key in database else 0)
    elif operation == 'insert':
        if key in database:
            print(0)
        else:
            database.add(key)
            print(1)
