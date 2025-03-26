class Book:
    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        if not Book.check_year(year):
            raise ValueError("Год издания должен быть целым числом и не в будущем")
        self.__year = year

    @staticmethod
    def check_year(year):
        current_year = 2024
        return isinstance(year, int) and year <= current_year

    @classmethod
    def create_default_year(cls, title, author):
        default_year = 2024
        return cls(title, author, default_year)

    def get_info(self):
        return f"{self.__title}, автор: {self.__author}, год: {self.__year}"
    
book1 = Book("1984", "George Orwell", 1949)
print(book1.get_info())  # Вывод: "1984, автор: George Orwell, год: 1949"

book2 = Book.create_default_year("Brave New World", "Aldous Huxley")
print(book2.get_info())  # Вывод: "Brave New World, автор: Aldous Huxley, год: 2024"