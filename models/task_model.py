from typing import Dict
import uuid


class Task:
    def __init__(
            self,
            title: str,
            description: str,
            category: str,
            due_date: str,
            priority: str,
            # status: str,
    ):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.category = category
        self.due_date = due_date
        self.priority = priority
        self.status = False

    def __str__(self):
        stat = "\033[32mВыполнено\033[0m" if self.status else "\033[31mОжидает\033[0m"
        return (
            f"ID: \033[33m{self.id}\033[0m "
            f"Название: {self.title}, Категория: {self.category}, "
            f"\nОписание: \033[34m{self.description}\033[0m, Дата выполнения: {self.due_date} "
            f"Приоритет: {self.priority}," f"Статус: \033[31m{stat}\033[0m"
            "\n-----------------------------------------------------------------------"
        )

    def to_dict(self) -> Dict:
        """Преобразование объекта задачи в словарь."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "due_date": self.due_date,
            "priority": self.priority,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data: Dict):
        """Создание объекта Task из словаря."""
        task = Task(
            data["title"],
            data["description"],
            data["category"],
            data["due_date"],
            data["priority"],
        )
        task.id = data.get("id")
        task.status = data.get("status", False)
        return task
