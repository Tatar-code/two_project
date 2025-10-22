from database import SessionLocal,Task
import datetime
from tkinter import messagebox

def add_task(name,text):
    try:
        with SessionLocal() as session:
            new_task = Task(name=name, text=text, time=datetime.datetime.now(),is_actual=True)
            session.add(new_task)
            session.commit()
    except Exception as e:
        session.rollback()
    finally:
        session.close()
    
def del_task(id):
    try:
        with SessionLocal() as session:
            del_task = session.query(Task).filter(Task.id == id).first()
            if del_task is not None:
                session.delete(del_task)
                session.commit()
    except Exception:
        session.rollback()
    finally:
        session.close()

            
def all_active_tasks():
    with SessionLocal() as session:
        all_true = session.query(Task).filter(Task.is_actual == True).all()
        return all_true

def all_not_active_tasks():
    with SessionLocal() as session:
        all_not = session.query(Task).filter(Task.is_actual == False).all()
        return all_not
    
def find_text(id):
    with SessionLocal() as session:
        text = session.query(Task).filter(Task.id == id).first()
        messagebox.showinfo(title=f'Заметка №{id}',message=text.text)