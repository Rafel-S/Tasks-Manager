import tkinter
import os


def main():
    file_exists = os.path.isfile('tasks.txt')
    if not file_exists:
        file = open('tasks.txt', 'w+')
    file = open('tasks.txt', 'r')
    file_string = file.read()
    tasks_list = file_string.splitlines()
    tasks_manager = tkinter.Tk(className='Task List')
    tasks_manager.title('To-do List Manager')
    tasks_manager.geometry('800x600')
    scroll_tasks = tkinter.Scrollbar()
    scroll_tasks.pack(side='right', fill='y')
    title_1 = tkinter.Label(tasks_manager, text="Your List of Tasks:")
    title_1.pack(anchor='n')
    tasks = tkinter.Listbox(tasks_manager, yscrollcommand=scroll_tasks.set, height='25', width='130', selectmode='single')
    tasks.pack(anchor='nw', padx='10', pady='10')
    for i in tasks_list:
        tasks.insert('end', i)
    label_2 = tkinter.Label(tasks_manager, text="Type your task below:")
    label_2.pack(anchor='s')
    text_box = tkinter.Entry(tasks_manager, width='110')
    text_box.pack(anchor='sw', padx='50', pady='15')
    add_task = tkinter.Button(tasks_manager, text='Add Task', command=lambda: add_task_method(tasks_list, text_box, tasks), height='3', width='15', background='green')
    add_task.pack(side='left', padx='180')
    remove_task = tkinter.Button(tasks_manager, text='Remove Task', command=lambda: remove_task_method(tasks_list, tasks), height='3', width='15', background='red')
    remove_task.pack(side='left')
    tasks_manager.mainloop()
    file = open('tasks.txt', 'w+')
    for i in tasks_list:
        file.write(i + '\n')
    file.close()


def add_task_method(tasks_list, text_box, tasks):
    task = text_box.get()
    tasks_list.append(task)
    tasks.insert('end', task)


def remove_task_method(tasks_list, tasks):
    if tasks.curselection():
        selected_task = tasks.get(tasks.curselection())
        task_index = tasks.curselection()
        tasks_list.remove(selected_task)
        tasks.delete(task_index)


if __name__ == '__main__':
    main()
