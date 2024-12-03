from typing import List

from models.db import JsonDatabase
from models.task_model import Task


class TaskManager(JsonDatabase):
    def add_task(self, task: Task):
        """Добавление новой задачи в базу данных."""
        data = self.read_data()
        data.append(task.to_dict())
        self.write_data(data)

    def change_status(self, title: str):
        tasks = self.get_all_tasks()
        for task in tasks:
            if task.title == title:
                task.status = True if not task.status else False
                self.write_data([task.to_dict() for task in tasks])
                return True
        return False

    def get_all_tasks(self) -> List[Task]:
        """Получение всех задач из базы данных."""
        data = self.read_data()
        return [Task.from_dict(task) for task in data]

    def find_task_by_category(self, category: str) -> List[Task]:
        """Поиск задач по категории."""
        tasks = self.get_all_tasks()
        find_tasks = []
        for task in tasks:
            if task.category == category:
                find_tasks.append(task)
        return find_tasks if find_tasks else []

    def delete_task_by_title(self, title: str) -> True | False:
        """Удаление задачи по названию."""
        tasks = self.get_all_tasks()
        tasks_new = [task for task in tasks if task.title != title]
        if len(tasks) == len(tasks_new):
            return False
        else:
            self.write_data([task.to_dict() for task in tasks_new])
            return True

    def edit_task(self, task_id: str, **kwargs):
        """Редактирование существующей задачи по её идентификатору."""
        tasks = self.get_all_tasks()
        task_found = False

        for task in tasks:
            print(task.id)
            if task.id == task_id:
                for key, value in kwargs.items():
                    if hasattr(task, key) and value != "":
                        setattr(task, key, value)  # Обновляем только существующие атрибуты
                task_found = True
                break  # Прерываем цикл после нахождения и обновления задачи

        if task_found:
            self.write_data([task.to_dict() for task in tasks])  # Сохраняем обновленные задачи
            return True  # Успешное обновление
        return False
