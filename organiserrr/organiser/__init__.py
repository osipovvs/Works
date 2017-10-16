import os.path as path
import sys

from organiser import storage

get_connection = lambda : storage.connect('organiser.sqlite')

def act_show_tasks():
    """Show all the tasks"""
    with get_connection() as conn:
        rows = storage.show_all(conn)

    template = '{row[id]} - {row[name]} - {row[deadline]} - {row[status]}'

    for row in rows:
        print(template.format(row=row))


def act_add_task():
    """Add a task"""
    name = input('\nEnter the name of the task: ')
    message = input('\nEnter the description of the task: ')
    deadline = input('\nEnter the deadline (YYYY-MM-DD): ')

    if not name:
        return

    with get_connection() as conn:
        name = storage.add_task(conn, name, message, deadline)

    print('The new task "{}" added successfully'.format(name))



def act_edit_task():
    """Edit a task"""
    pk = input('\nEnter the number (id) of the task to be updated: ')
    name = input('\nEnter new name of the task: ')
    message = input('\nEnter new description of the task: ')
    deadline = input('\nEnter new deadline (YYYY-MM-DD): ')

    with get_connection() as conn:
        storage.edit_task(conn, (name, message, deadline, pk))


def act_finish_task():
    """Finish a task"""
    pk = input('\nEnter the id of the task to be marked as finished: ')

    with get_connection() as conn:
        storage.finish_task(conn, pk)


def act_restart_task():
    """Restart a task"""
     pk = input('\nEnter the id of the task to be marked as finished: ')

    with get_connection() as conn:
        storage.restart_task(conn, pk)


def act_menu():
    print("""
        WELCOME TO ORGANISER!

        Please choose an action:
         1. Show the list of tasks
         2. Add a new task
         3. Edit a task
         4. Finish a task
         5. Restart a task
         m. Show menu
         q. Exit""")


def action_exit():
    """Exit the program"""
    sys.exit(0)


def main():
    creation_schema = pth.join(
        pth.dirname(__file__), 'schema.sql'
    )

    with get_connection() as conn:
        storage.initialize(conn, creation_schema)

    actions = {
        '1': act_show_tasks,
        '2': act_add_task,
        '3': act_edit_task,
        '4': act_finish_task,
        '5': act_restart_task,
        'm': act_menu,
        'q': action_exit
    }

    act_menu()
    
    while True:
        cmd = input('\nEnter a command: ')
        action = actions.get(cmd)

        if action:
            action()
        else:
            print('Error: unknown command!')