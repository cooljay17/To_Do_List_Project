import ConnectDB as db

# This module provides functions to manage tasks in a to-do list application.
# It includes functions to add, view, update, and delete tasks in a PostgreSQL database.
# Ensure the database connection is established before performing any operations.
   
#To add a task
def add_task(task_desc, is_completed):
    conn = db.connect_to_db()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute('''INSERT INTO "SCH_TASKS"."T_TDO_TASKS"("TASK_DESC","IS_COMPLETED") 
                           VALUES (%s, %s)''', 
                           (task_desc, is_completed))
            conn.commit()
            print("Task added successfully.")
        except Exception as e:
            print(f"Error adding task: {e}")
        finally:
            cursor.close()
            conn.close()

# To view all tasks
def view_tasks():   
    conn = db.connect_to_db()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute('''select "TASK_DESC", (CASE WHEN "IS_COMPLETED"=TRUE THEN 'YES' ELSE 'NO' END) AS "IS_COMPLETED" 
                                from "SCH_TASKS"."T_TDO_TASKS" ''')
            tasks = list(cursor.fetchall())
            for task in tasks:
                print( f"Name: {task[0]}, IsCompleted: {task[1]}")
            return tasks        
        except Exception as e:
            print(f"Error retrieving tasks: {e}")
        finally:
            cursor.close()
            conn.close() 


# To view tasks names for updation
def view_tasks_names():   
    conn = db.connect_to_db()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute('''SELECT "ID","TASK_DESC","IS_COMPLETED" FROM  "SCH_TASKS"."T_TDO_TASKS" ''')
            tasks = list(cursor.fetchall())
            for task in tasks:
                print( f"ID: {task[0]}, Task: {task[1]}, IsCompleted: {task[2]}")
            return tasks        
        except Exception as e:
            print(f"Error retrieving tasks: {e}")
        finally:
            cursor.close()
            conn.close() 
               

#To update a task
def update_task(task_id, task_desc):
    conn = db.connect_to_db()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute('''UPDATE "SCH_TASKS"."T_TDO_TASKS"  \
                            SET "TASK_DESC" = %s WHERE "ID" = %s''', 
                           (task_desc, task_id))
            conn.commit()
            print("Task updated successfully.")
        except Exception as e:
            print(f"Error updating task: {e}")
        finally:
            cursor.close()
            conn.close()

# To update the status of a task
def update_task_status(task_id, is_completed):
    conn = db.connect_to_db()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute('''UPDATE "SCH_TASKS"."T_TDO_TASKS"  
                           SET  "IS_COMPLETED" = %s WHERE "ID" = %s ''', 
                           (is_completed, task_id))
            conn.commit()
            print("Task status updated successfully.")
        except Exception as e:
            print(f"Error updating task: {e}")
        finally:
            cursor.close()
            conn.close()  

# To delete a task
def delete_task(task_id):
    conn = db.connect_to_db()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute('''DELETE FROM "SCH_TASKS"."T_TDO_TASKS" WHERE "ID" = %s''', (task_id,))
            conn.commit()
            print("Task deleted successfully.")
        except Exception as e:
            print(f"Error deleting task: {e}")
        finally:
            cursor.close()
            conn.close()                      