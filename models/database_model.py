import sqlite3

db_file = "todo_db.db"

class ToDoDatabase():
    # establish the database connection
    # and create the table if needed.
    def __init__(self):
        self.__conn = sqlite3.connect(db_file)
        self.__cursor = self.__conn.cursor()

        # Check if database exists.  If not, 
        # create it.
        self.__cursor.execute("""
            CREATE TABLE IF NOT EXISTS ToDo (
                id INTEGER PRIMARY KEY,
                title TEXT,
                desc TEXT,
                isComplete BOOLEAN,
                completedDate TEXT  
            )                  
        """)

        self.__conn.commit()


    def __del__(self):
        self.__conn.commit()
        self.__conn.close()


    def add_new_task(self, new_item):
        sql = "INSERT INTO ToDo VALUES (NULL, ?, ?, ?, ?)"

        self.__cursor.execute(sql, (new_item.title, new_item.desc, 
                              new_item.isComplete, str(new_item.completeDate)))
        
        self.__conn.commit()

    
    def update_task(self, task):
        sql = "UPDATE ToDo SET title = ?, desc = ?, isComplete = ?, completedDate = ? WHERE id = ?"

        self.__cursor.execute(sql, (task.title, task.desc, task.isComplete, str(task.completeDate), task.id))
        self.__conn.commit()


    def get_task(self, id):
        sql = "SELECT * FROM ToDo WHERE id = ?"

        result = self.__cursor.execute(sql, id)

        self.__conn.commit()
        return result
    
    def remove_task(self, id):
        sql = "DELETE FROM ToDo WHERE id = ?"

        self.__cursor.execute(sql, (id,))
        self.__conn.commit()


    def get_all_tasks(self):
        sql = "SELECT * FROM ToDo"

        result = self.__conn.execute(sql)
        self.__conn.commit()
        return result
    
