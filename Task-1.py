from tkinter import *

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_tasks()

def delete_task():
    selected = tasks_listbox.curselection()
    if selected:
        tasks.pop(selected[0])
        update_tasks()

def edit_task():
    selected = tasks_listbox.curselection()
    if selected:
        current_task = tasks_listbox.get(selected)
        entry.delete(0, END)
        entry.insert(END, current_task)
        delete_task()

def update_tasks():
    tasks_listbox.delete(0, END)
    for task in tasks:
        tasks_listbox.insert(END, task)

tasks = []

root = Tk()
root.title("To-Do List")

label = Label(root, text="To-Do-List",background="Blue",font=("Times New Roman",60))
label.pack(fill= BOTH)

label = Label(root, text="Add Item ",background="white",font=("Times New Roman",30))
label.place(x=600,y=100)

label = Label(root, text="Enter a task:",font=("Times New Roman",20))
label.place(x=600,y=150)

entry = Entry(root, width=30,font=(7))
entry.place(x=750,y=160)

add_button = Button(root, text="Add Task", command=add_task,activebackground="red",height=2,width=10)
add_button.place(x=770,y=190)


label = Label(root, text="List of Items :",font=("Times New Roman",20))
label.place(x=600,y=270)


edit_button = Button(root, text="Edit Task", command=edit_task,activebackground="lightblue",height=2,width=10)
edit_button.place(x=1000,y=350)

delete_button = Button(root, text="Delete Task", command=delete_task,activebackground="lightgreen",height=2,width=10)
delete_button.place(x=1100,y=350)

tasks_listbox = Listbox(root,width=30,font=(7))
tasks_listbox.place(x=650,y=320)

update_tasks()

root.mainloop()
