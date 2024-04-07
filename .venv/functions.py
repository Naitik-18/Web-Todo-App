import os

if not os.path.exists('todos.txt'):
    with open('todos.txt' , 'w') as file:
        pass

FILEPATH = "todos.txt"

def get_todos(filepath = FILEPATH):                   # Here filepath is the parameter and "todos.txt" is
    # Doc-string                                      # the default argument value if no value is given.
    '''Read a text file and returns a list
    of to-do items.'''
    filepath = os.path.join(os.getcwd(), "todos.txt")
    # os.getcwd() to get the current working directory of the application.
    # os.path.join() to construct a relative path to "todos.txt" from the root directory of the application.

    with open(filepath, 'r') as file_local:
        todos_local = [line.strip() for line in file_local.readlines()]
    return todos_local

def write_todos(todos_arg, filepath = FILEPATH):
    '''
    Write the to-do items list to a text file.
    '''
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)



#print(__name__)
#if __name__ == '__main__':           # Built-in variable __name__ records the name
#    print("Hello")                   # of the currently running module or script.
#    print(get_todos())