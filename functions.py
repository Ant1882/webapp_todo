FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    '''Retrieve the todo list from the file'''
    with open(filepath, 'r', encoding='UTF-8') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def save_todos(_todos, filepath=FILEPATH):
    '''Save the todo list to the file'''
    with open(filepath, 'w', encoding='UTF-8') as file_local:
        file_local.writelines(_todos)


#print(__name__)
if __name__ == "__main__":
    print("Hello")
    print(get_todos())
