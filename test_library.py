import unittest
import os
from library import Library


class TestLibrary(unittest.TestCase):
    def setUp(self):
        """ Создаем временный файл для тестов. """
        self.test_file = 'test_library_data.json'
        self.library = Library(self.test_file)
        self.library.books = []  # Очищаем библиотеку для тестов

    def tearDown(self):
        """ Удаляем временный файл после тестов. """
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_book(self):
        """ Тестируем добаление книги в библиотеку. """
        self.library.add_book("Test Book", "Test Author", 2021)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "Test Book")
        self.assertEqual(self.library.books[0].author, "Test Author")
        self.assertEqual(self.library.books[0].year, 2021)

    def test_remove_book(self):
        """ Тестируем удаление книги из библиотеки. """
        self.library.add_book("Test Book", "Test Author", 2021)
        self.library.remove_book(1)
        self.assertEqual(len(self.library.books), 0)

    def test_search_books_by_title(self):
        """ Тестируем поиск книги в библиотеке по названию. """
        self.library.add_book("Test Book", "Test Author", 2021)
        self.library.add_book("Another Book", "Another Author", 2020)
        results = self.library.search_books("Test Book")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Test Book")

    def test_search_books_by_author(self):
        """ Тестируем поиск книги в библиотеке по автору. """
        self.library.add_book("Test Book", "Test Author", 2021)
        results = self.library.search_books("Test Author")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].author, "Test Author")

    def test_display_books(self):
        """ Тестируем отображение книг в библиотеке. """
        self.library.add_book("Test Book", "Test Author", 2021)
        self.library.add_book("Another Book", "Another Author", 2020)
        self.library.display_books()  # Просто проверяем, что не возникает исключений

    def test_change_status(self):
        """ Тестируем смену статуса книги в библиотеке. """
        self.library.add_book("Test Book", "Test Author", 2021)
        self.library.change_status(1, "выдана")
        self.assertEqual(self.library.books[0].status, "выдана")

    def test_change_status_invalid(self):
        """ Тестируем смену статуса книги в библиотеке на недопустимый. """
        self.library.add_book("Test Book", "Test Author", 2021)
        self.library.change_status(1, "недоступный статус")  # Проверка на некорректный статус
        self.assertEqual(self.library.books[0].status, "в наличии")  # Статус не должен измениться


if __name__ == '__main__':
    unittest.main()
