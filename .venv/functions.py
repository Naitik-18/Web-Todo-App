FILEPATH = "todos.txt"
def get_todos(filepath = FILEPATH):                   # Here filepath is the parameter and "todos.txt" is
    # Doc-string                                      # the default argument value if no value is given.
    '''Read a text file and returns a list
    of to-do items.'''
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
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