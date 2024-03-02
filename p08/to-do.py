user_list = []
file = open('list.txt', 'r')
for i in file.readlines():
    s = i.strip()
    user_list.append(s)

while True:
    print('##List##')
    print(" 1. Add Task \n 2. Edit Task \n 3. Delete Task \n 4. Show list \n 5. Exit")

    action = int(input('Action: '))
    if action == 5:
        file = open('list.txt', 'w')
        for i in user_list:
            file.write(f'{i}\n')
        break
    elif action == 1:
        task = input('Input task: ')
        user_list.append(task)
    elif action == 4:
        i = 0
        for item in user_list:
            print(i, ' > ', item)
            i += 1
    elif action == 3:
        delete_index = int(input('Input index: '))
        del user_list[delete_index]
    elif action == 2:
        n = int(input('Input n: '))
        new = input('Input new: ')
        user_list[n] = new
        
