import json
import os

from book import Book


class Library:
    """ Класс библиотеки. Управляет коллекцией книг и предоставляет методы для выполнения различных операций с ними"""
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.books = []
        self.load_books()

    def load_books(self):
        """ Загружает книги из файла JSON. """
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for book in data:
                    self.books.append(Book(**book))

    def save_books(self):
        """ Сохраняет текущий список книг в файл JSON . """
        with open(self.file_name, 'w', encoding='utf-8') as file:
            for book in self.books:
                json.dump(book.to_dict(), file, ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: int):
        """ Добавляет новую книгу в библиотеку. """
        book_id = len(self.books) + 1
        new_book = Book(book_id, title, author, year)
        self.books.append(new_book)
        self.save_books()
        print(f'Книга "{title}" добавлена в библиотеку.')

    def remove_book(self, book_id: int):
        """ Удаляет книгу из библиотеки по ее ID. """
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                self.save_books()
                print(f'Книга с ID {book_id} удалена из библиотеки.')
                return
        print(f'Книга с ID {book_id} не найдена.')

    def search_books(self, query: str):
        """ Ищет книги по названию, автору или году. """
        results = []
        for book in self.books:
            if query.lower() in book.title.lower() or query.lower() in book.author.lower() or query == str(book.year):
                results.append(book)
            for res in results:
                print(f'ID: {res.id}, Название: {res.title}, Автор: {res.author}, '
                      f'Год: {res.year}, Статус: {res.status}')
                return results
        else:
            print('Книги не найдены.')

    def display_books(self):
        """ Отображает все книги в библиотеке. """
        if not self.books:
            print('Библиотека пуста.')
            return
        for book in self.books:
            print(f'ID: {book.id}, Название: {book.title}, '
                  f'Автор: {book.author}, Год: {book.year}, Статус: {book.status}')

    def change_status(self, book_id: int, new_status: str):
        """ Меняет статус книги по ее ID. """
        for book in self.books:
            if book.id == book_id:
                if new_status in ["в наличии", "выдана"]:
                    book.status = new_status
                    self.save_books()
                    print(f'Статус книги с ID {book_id} изменен на "{new_status}".')
                else:
                    print('Некорректный статус. Доступные статусы: "в наличии", "выдана".')
                return
        print(f'Книга с ID {book_id} не найдена.')
