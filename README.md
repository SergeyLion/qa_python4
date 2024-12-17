# qa_python
Были созданы следующие тесты: 

* test_add_new_book_add_two_books - проверяет метод add_new_book, добавляя две книги. 
* test_add_new_book_add_valid_length_name_add_book - проверяет валидацию метода add_new_book, добавляя книги с именем от 1 до 40
* test_set_book_genre_from_genre_list - проверяет метод set_book_genre, на установку допустимых жанров
* test_set_book_genre_no_genre_list - проверяет метод set_book_genre, и валидацию метода на допустимые жанры 
* test_get_book_genre_from_books_genre - проверяет метод get_book_genre, на возврат жанра по имени книги 
* test_get_books_with_specific_genre_return_one_book - проверяет метод get_books_with_specific_genre, на возврат списка сформированного по задаваемому жанру 
* test_get_books_genre - проверяет метод get_books_genre, на возврат справочника книга: жанр 
* test_get_books_for_children - проверяем метод get_books_for_children, на возврат списка книг допустимых жанров для детей
* test_add_book_in_favorites_add_one_book - проверяем метод add_book_in_favorites на добавление книги в избранное
* test_delete_book_from_favorites_del_one_book - проверяем метод delete_book_from_favorites на удаление книги из избранного