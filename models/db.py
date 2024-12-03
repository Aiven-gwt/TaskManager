from typing import Dict, List
import json


class JsonDatabase:
    def __init__(self, filename):
        self.filename = filename

    def read_data(self) -> List[Dict]:
        """Чтение всех данных из JSON-файла."""
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def write_data(self, data: List[Dict]):
        """Запись данных в JSON-файл."""
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
