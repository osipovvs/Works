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

# Отредактировать задачу
SQL_UPDATE_TASK = """
    UPDATE organiser 
    SET name=? 
        message=?
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
