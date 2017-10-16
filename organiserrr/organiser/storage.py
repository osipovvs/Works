import os.path as pth
import sqlite3

#Вывести список задач
SQL_SELECT_ALL = """                  
    SELECT
        id, name, message, deadline
    FROM
        organiser
"""
# Добавить задачу
SQL_ADD_TASK = """
    INSERT INTO organiser (name, message, deadline) VALUES (?, ?, ?)
"""

#Посмотреть задачу с определённым названием
SQL_SELECT_TASK_BY_NAME = SQL_SELECT_ALL + " WHERE name=?"

# Отредактировать задачу
SQL_UPDATE_TASK = """
    UPDATE organiser 
    SET name=?, 
        message=?,
        deadline=?
    WHERE id=?
"""

# Завершить задачу
SQL_FINISH_TASK = """
    UPDATE organiser SET status=0 WHERE id=?
"""

# Начать задачу сначала
SQL_RESTART_TASK = """
    UPDATE organiser SET status=1 WHERE id=?
"""

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def connect(db_name=None):
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)
    conn.row_factory = dict_factory

    return conn

def initialize(conn, creation_schema):
    with conn, open(creation_schema) as f:
        conn.executescript(f.read())


def show_all(conn):
    """Shaws all the tasks"""
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL)
        return cursor.fetchall()


def add_task(conn, name, message, deadline):
    """Adds a new task into the database"""
    if not name:
        except ValueError:
            print("Please name the task.")
        return

    with conn:
        found = find_task_by_name(conn, name)

        if found:
            return found.get('message', 'deadline')

        cursor = conn.execute(SQL_ADD_TASK, (name, message, deadline))

        return name


def edit_task(conn, id):
    """Edit a task"""
    with conn:
        cursor = conn.execute(SQL_UPDATE_TASK, (name, message, deadline, id))
        conn.commit()

def finish_task(conn, pk):
    """Finish a task"""
    with conn:
        cursor = conn.execute(SQL_FINISH_TASK, pk)
        conn.commit()

def restart_task(conn, pk):
    """Restart a task"""
    with conn:
        cursor = conn.execute(SQL_RESTART_TASK, pk)
        conn.commit()

