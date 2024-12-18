import pytest


from main import BooksCollector


@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture
def add_one_book(collector):
    collector.books_genre = {'Скорбь сатаны': ''}

@pytest.fixture
def word_three_books(collector):
    collector.books_genre = {'Скорбь сатаны': 'Фантастика', 'Шерлок Холмс': 'Детективы', 'Оно': 'Ужасы'}

@pytest.fixture
def favorites_list(collector):
    collector.favorites = ['Скорбь сатаны', 'Шерлок Холмс']
