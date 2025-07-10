from datetime import datetime

class Task:
    def __init__(self, task_id, description):
        self.id = task_id
        self.description = description
        self.status = "Pendiente"
        self.creation_date = datetime.now()

class TodoList:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, description):
        task = Task(self.next_id, description)
        self.tasks.append(task)
        self.next_id += 1

    def list_tasks(self):
        for task in self.tasks:
            print(f"ID: {task.id}, Descripción: {task.description}, Estado: {task.status}, Fecha de creación: {task.creation_date}")

    def mark_task_complete(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.status = "Completada"
                break

    def clear_all_tasks(self):
        self.tasks.clear()
        self.next_id = 1

    def edit_task(self, task_id, new_description):
        for task in self.tasks:
            if task.id == task_id:
                task.description = new_description
                break

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.id != task_id]