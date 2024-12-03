from models.task_manager_model import TaskManager
from models.task_model import Task
from datetime import datetime


def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def display_menu():
    print("\nКонсоль управления задачами")
    print("--------------------------")
    print("1. Добавить новую задачу")
    print("2. Показать все задачи")
    print("3. Задачи по категории")
    print("4. Удалить задачу по названию")
    print("5. Изменить статус задачи")
    print("6. Редактировать задачу")
    print("7. Выйти")


def get_task_details():
    title = input("Введите название задачи: ")
    description = input("Введите описание задачи: ")
    category = input("Введите категорию задачи: ")

    while True:
        due_date = input("Введите дату выполнения задачи (ГГГГ-ММ-ДД): ")
        if is_valid_date(due_date):
            break
        else:
            print(f"Дата {due_date} введена неправильно. Попробуйте ещё раз.")

    priority = input("Введите приоритет задачи (Низкий/Средний/Высокий): ")
    return Task(title, description, category, due_date, priority)


def main():
    db = TaskManager("tasks2.json")

    while True:
        display_menu()
        choice = input("Выберите опцию (1-5)>> ")

        if choice == "1":
            task = get_task_details()
            db.add_task(task)
            print("\nЗадача успешно добавлена!")

        elif choice == "2":
            tasks = db.get_all_tasks()
            if not tasks:
                print("\nЗадачи не найдены.")
            else:
                print("\nСписок всех задач:")
                for task in tasks:
                    print(task)

        elif choice == "3":
            category = input("Введите категорию: ")
            task = db.find_task_by_category(category)
            if task:
                for task_ in task:
                    print(task_)
            else:
                print("\nЗадач в данной категории не найдено.")

        elif choice == "4":
            title_to_delete = input("Введите название задачи для удаления: ")
            if db.delete_task_by_title(title_to_delete):
                print("\nЗадача успешно удалена.")
            else:
                print("\nЗадача с таким названием не найдена.")

        elif choice == "5":
            title_to_update_status = input("Введите название задачи для удаления: ")
            if db.change_status(title_to_update_status):
                print("\nСтатус обновлён")
            else:
                print("\nЗадача с таким названием не найдена.")

        elif choice == "6":
            id_to_update = input("Введите id задачи для редактирования: ")
            print("\t Вводите параметры которые нужно обновить, или оставляйте поле пустым")
            task_details = get_task_details().to_dict()
            if db.edit_task(id_to_update, **task_details):
                print("\nЗадача обновлён")
            else:
                print("\nЗадача с таким id не найдена.")

        elif choice == "7":
            print("Выход из программы.")
            break

        else:
            print("\nНекорректный ввод. Пожалуйста, выберите опцию от 1 до 5.")


if __name__ == "__main__":
    main()
