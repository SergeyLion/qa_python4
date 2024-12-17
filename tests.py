import pytest


from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        # создаем экземпляр (объект) класса BooksCollector
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize('name_book',['я', 'Lorem ipsum dolor si', 'Lorem ipsum dolor sit amet, consectetuer'])
    def test_add_new_book_add_valid_length_name_add_book(self, name_book, collector):
        collector.add_new_book(name_book)
        assert collector.books_genre[name_book] == ''

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_from_genre_list(self, genre, collector, add_one_book):
        collector.set_book_genre('Скорбь сатаны', genre)
        assert collector.books_genre['Скорбь сатаны'] == genre

    def test_set_book_genre_no_genre_list(self, collector, add_one_book):
        collector.set_book_genre('Скорбь сатаны', 'Классика')
        assert collector.books_genre['Скорбь сатаны'] == ''

    def test_get_book_genre_from_books_genre(self, collector, add_one_book):
        collector.set_book_genre('Скорбь сатаны', 'Фантастика')
        assert collector.get_book_genre('Скорбь сатаны') == 'Фантастика'

    def test_get_books_with_specific_genre_return_one_book(self, collector, word_three_books):
        assert collector.get_books_with_specific_genre('Ужасы') == ['Оно']

    def test_get_books_genre(self, collector, word_three_books):
        assert collector.get_books_genre() == {'Скорбь сатаны': 'Фантастика', 'Шерлок Холмс': 'Детективы', 'Оно': 'Ужасы'}

    def test_get_books_for_children(self, collector, word_three_books):
        assert collector.get_books_for_children() == ['Скорбь сатаны']

    def test_add_book_in_favorites_add_one_book(self,collector, word_three_books):
        collector.add_book_in_favorites('Оно')
        assert collector.favorites == ['Оно']

    def test_delete_book_from_favorites_del_one_book(self,collector, favorites_list):
        collector.delete_book_from_favorites('Шерлок Холмс')
        assert collector.favorites == ['Скорбь сатаны']

    def test_get_list_of_favorites_books(self, collector, favorites_list):
        assert collector.get_list_of_favorites_books() == ['Скорбь сатаны', 'Шерлок Холмс']

