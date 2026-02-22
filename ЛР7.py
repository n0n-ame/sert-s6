import datetime

class RareBook:
    def __init__(self, title, author, year, pub_place, storage_place):
        # Проверка строковых полей на пустоту (У1, У2, У5, У6)
        if not str(title).strip():
            raise ValueError("Ошибка: Название не может быть пустым.")
        if not str(author).strip():
            raise ValueError("Ошибка: Автор не может быть пустым.")
        if not str(pub_place).strip():
            raise ValueError("Ошибка: Место издания не может быть пустым.")
        if not str(storage_place).strip():
            raise ValueError("Ошибка: Место хранения не может быть пустым.")
        
        # Проверка года на тип данных (У3)
        try:
            self.year = int(year)
        except ValueError:
            raise ValueError("Ошибка: Год издания должен быть целым числом.")
            
        # Проверка года на диапазон (У4)
        current_year = datetime.datetime.now().year
        if self.year < 1000 or self.year > current_year:
            raise ValueError(f"Ошибка: Год издания вне допустимого диапазона (1000-{current_year}).")
            
        self.title = title.strip()
        self.author = author.strip()
        self.pub_place = pub_place.strip()
        self.storage_place = storage_place.strip()

    def __str__(self):
        return (f"«{self.title}» — {self.author} ({self.year} г.), "
                f"г. {self.pub_place}, хранение: {self.storage_place}")

def find_earliest_and_latest_books(books):
    """Функция для поиска самой ранней и самой поздней книги."""
    # Проверка на пустой список (У7)
    if not books:
        return "Ошибка: Список книг пуст. Невозможно выполнить поиск."
    
    earliest_book = min(books, key=lambda b: b.year)
    latest_book = max(books, key=lambda b: b.year)
    
    result = "РЕЗУЛЬТАТЫ ПОИСКА:\n"
    result += f"Самая ранняя книга:\n  {earliest_book}\n"
    result += f"Самая поздняя книга:\n  {latest_book}"
    return result


if __name__ == "__main__":
    print("--- ТЕСТ: ПРАВИЛЬНЫЕ ДАННЫЕ ---")
    try:
        books_list = [
            RareBook("Апостол", "Федоров И.", 1564, "Москва", "РГБ"),
            RareBook("Псалтырь", "Мстиславец П.", 1568, "Заблудов", "ГИМ"),
            RareBook("Грамматика", "Смотрицкий М.", 1619, "Евье", "РНБ")
        ]
        print(find_earliest_and_latest_books(books_list))
    except ValueError as e:
        print(e)

    print("\n--- ТЕСТ: НЕПРАВИЛЬНЫЕ ДАННЫЕ ---")
    
    invalid_data_tests = [
        {"title": "", "author": "Пушкин А.С.", "year": 1833, "pub": "СПб", "store": "Эрмитаж"}, # Н1.1
        {"title": "Слово...", "author": "Неизвестен", "year": "древность", "pub": "Киев", "store": "РНБ"}, # Н3.1
        {"title": "Евангелие", "author": "Неизвестен", "year": 900, "pub": "Новгород", "store": "РНБ"}, # Н4.1
        {"title": "Мертвые души", "author": "Гоголь Н.В.", "year": 1842, "pub": "Москва", "store": "  "}, # Н6.1
    ]
    
    for i, data in enumerate(invalid_data_tests, 1):
        print(f"Тест неверных данных {i}: ", end="")
        try:
            book = RareBook(data["title"], data["author"], data["year"], data["pub"], data["store"])
            print("Создано успешно (ОШИБКА, должно было выбросить исключение)")
        except ValueError as e:
            print(e)
            
    print("\nТест пустого списка (Н7.1): ", end="")
    print(find_earliest_and_latest_books([]))