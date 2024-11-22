from library import Library


def main():
    library = Library('library_data.json')

    while True:
        print("\nДобро пожаловать в нашу библиотеку! Выберите что бы вы хотели сделать:")
        print("1. Добавить книгу в библиотеку")
        print("2. Удалить книгу из библиотеки")
        print("3. Найти книгу в библиотеке")
        print("4. Отобразить все книги, которые есть в библиотеке")
        print("5. Изменить статус книги")
        print("6. Выйти")

        choice = input("Введите номер необходимого действия: ")

        if choice == '1':
            title = input("Введите название книги для добавления: ")
            author = input("Введите автора книги для добавления: ")
            year = int(input("Введите год издания для добавления: "))
            library.add_book(title, author, year)
        elif choice == '2':
            book_id = int(input("Введите ID книги для ее удаления из библиотеки: "))
            library.remove_book(book_id)
        elif choice == '3':
            query = input("Введите название, автора или год для поиска книги в библиотеке: ")
            library.search_books(query)
        elif choice == '4':
            print('В нашей библиотеке на данный момент есть следующие книги:')
            library.display_books()
        elif choice == '5':
            book_id = int(input("Введите ID книги для изменения ее статуса: "))
            new_status = input("Введите новый статус (в наличии/выдана): ")
            library.change_status(book_id, new_status)
        elif choice == '6':
            print("До новых встреч.")
            break
        else:
            print("Некорректный ввод, попробуйте снова.")


if __name__ == "__main__":
    main()
