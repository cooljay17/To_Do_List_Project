#create a streamlit web app for to do list  to add, view,delete, and update tasks
import streamlit as st
import ManageTasks as mt
import pandas as pd


# Set the title of the app
st.title("To-Do List Application")      
# Create a sidebar for navigation
st.sidebar.title("Menu")  
# Add options to the sidebar
option = st.sidebar.selectbox("Select an option", ["Add Task", "View Tasks", "Update Task", "Update Task Status","Delete Task"])

# Add a section for adding tasks
if option == "Add Task":
    st.header("Add Task")
    task_name = st.text_input("Task Name")
    task_completed = st.checkbox("Is Completed", value=False)
    if st.button("Add Task"):
        if task_name:
            mt.add_task(task_name, task_completed)
            st.success("Task added successfully!")
        else:
            st.error("Please fill in all fields.")

# Add a section for viewing tasks
elif option == "View Tasks":
    st.header("View Tasks")
    print("Fetching tasks from the database...")  
    tasks = mt.view_tasks() # Fetch tasks from the database   
    if tasks:
        # Create a DataFrame to display tasks in a table format
        df = pd.DataFrame(tasks, columns=["Task Name", "Completion Status"])
        st.table(df.set_index(df.columns[0])) 
    else:
        st.write("No tasks found.")
        


# Add a section for updating task status
elif option == "Update Task Status":                                            
    st.header("Update Task Status")
    print("Fetching tasks from the database...")  
    tasks = mt.view_tasks_names()
    if tasks:
        task_names = st.selectbox("Select a task to update", tasks, format_func=lambda x: f"{x[0]} - {x[1]}")
        task = task_names                      
        st.write(f"Selected Task ID: {task[0]}, Task Name: {task[1]}")
    else:
        st.write("No tasks found.")  
     
    print("Task Id to be updated:", tuple({task[0]}))
    print ("Is Completed Status:", task[2])
    # Create a checkbox for task completion status based on the task's current status
    task_completed= st.checkbox("Is Completed", value=task[2])
    print("Task Completed Status:", task_completed)
    if st.button("Update Status"):  
        if tuple({task[0]}) and task_completed:          
            mt.update_task_status(tuple({task[0]}), task_completed)
            st.success("Task status updated successfully!")       
        else:
            st.write("Error: Please select a task to update status.")
    
   

# Add a section for updating tasks
elif option == "Update Task":   
    st.header("Update Task")
    print("Fetching tasks from the database...")  
    tasks = mt.view_tasks_names()
    if tasks:
        task_names = st.selectbox("Select a task to update", tasks, format_func=lambda x: f"{x[0]} - {x[1]}")
        task = task_names                      
        st.write(f"Selected Task ID: {task[0]}, Task Name: {task[1]}")
    else:
        st.write("No tasks found.") 
    task_name = st.text_input("New Task Name")
    
    if st.button("Update Task"):
        if tuple({task[0]}) and task_name:
            mt.update_task(tuple({task[0]}), task_name)
            st.success("Task updated successfully!")
        else:
            st.error("Please fill in all fields.")


# Add a section for deleting tasks
elif option == "Delete Task":
    st.header("Delete Task")
    st.header("Update Task")
    print("Fetching tasks from the database...")  
    tasks = mt.view_tasks_names()
    if tasks:
        task_names = st.selectbox("Select a task to update", tasks, format_func=lambda x: f"{x[0]} - {x[1]}")
        task = task_names                      
        st.write(f"Selected Task ID: {task[0]}, Task Name: {task[1]}")
    else:
        st.write("No tasks found.")
    task_id = tuple({task[0]})
    if st.button("Delete Task"):
        if task_id:
            mt.delete_task(task_id)
            st.success("Task deleted successfully!")
        else:
            st.error("Please enter a valid Task ID.")

# Add a footer
st.sidebar.markdown("---")  
st.sidebar.markdown("Made with ❤️ by Jayanthi")





