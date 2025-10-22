import tkinter as tk
from tkinter import simpledialog
import request as rq


class ToDoApp:
    def __init__(self):
        self.screen = tk.Tk()
        self.edit_screen()
        self.front_screen()
        self.create_green_button()
        self.create_red_button()
        self.create_add_task_button()
        self.tasks = []
        self.x = 350
        self.y = 150
    
    def edit_screen(self):
        self.screen.title('ToDoApp')
        self.screen.geometry('1000x800')
    

    def front_screen(self):
        green_widget = tk.Label(self.screen,
                              text='In processing',
                              anchor='w',
                              fg='green',
                              padx=100,
                              pady=75,
                              font=('Arial',20)
                              )
        red_widget = tk.Label(self.screen,
                              text='Over',
                              anchor='w',
                              fg='red',
                              padx=400,
                              pady=75,
                              font=('Arial',20)
                              )
        green_widget.grid(row=0,column=0,sticky='w')
        red_widget.grid(row=0,column=1,sticky='e')


    def create_green_button(self):
        row = 8
        for task in rq.all_active_tasks():
            button = tk.Button(self.screen,
                            text=task.name,
                            anchor='w',
                            fg='green',
                            font=('Arial',20),
                            width=10,
                            command=lambda t=task: rq.find_text(t.id)
                            )
            button.grid(row=row,column=0,sticky='w',padx=100)
            if row > 0:
                row -=1

    def create_red_button(self):
        row = 1
        for task in rq.all_not_active_tasks():
            button = tk.Button(self.screen,
                               text=task.name,
                               anchor='e',
                               fg='red',
                               font=('Arial',20),
                               width=10,
                               command=lambda t=task: rq.find_text(t.id)
                               )
            button.grid(row=row,column=1,sticky='e',padx=350)
            row += 1

    def create_add_task_button(self):
            button = tk.Button(self.screen,
                           text='+',
                           fg='green',
                           font=('Arial',20),
                           width=10,
                           command=self.enter_data
                           )
            button.grid(sticky='n')

    
    def enter_data(self):
        name = simpledialog.askstring('NAME','Enter name for the task...')
        text = simpledialog.askstring('VALUE','Enter value for the task...')
        if name and text is not None:
            rq.add_task(name=name,text=text)
            self.create_green_button()



if __name__ == '__main__':
    app = ToDoApp()
    app.screen.mainloop()




