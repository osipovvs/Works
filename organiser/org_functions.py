def show_tasks():
    print("Show all the tasks")


def add_task():
    print("Add a task")


def edit_task():
    print("Edit a task")


def finish_task():
    print("Finish a task")


def restart_task():
    print("Restart a task")


def commands():
    menu_text = """
        WELCOME TO ORGANISER!

        Please choose an action:
         1. Show the list of tasks
         2. Add a new task
         3. Edit a task
         4. Finish a task
         5. Restart a task
         6. Exit\r
    """
    k = int(input(menu_text))
    while k != 6:
        if k == 1:
            show_tasks()
        elif k == 2:
            add_task()
        elif k == 3:
            edit_task()
        elif k == 4:
            finish_task()
        elif k == 5:
            restart_task()
        k = int(input(menu_text))
