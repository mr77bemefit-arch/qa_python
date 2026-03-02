import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test

class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # проверка добавления книги которой еще нет в словаре, позитивный сценарий
    def test_add_new_book_add_book_not_in_list_positive_result(self):
        collector2 = BooksCollector()
        collector2.add_new_book('Терминатор')
        assert collector2.books_genre['Терминатор'] == ''
    
    # проверка добавления книги с негативным сценарием
    @pytest.mark.parametrize('book_name',['', 'Война мир Война мир Война мир Война мир В'])
    def test_add_new_book_add_empty_book_name_and_41symbols_book_name(self, book_name):
        collector1 = BooksCollector()
        collector1.add_new_book(book_name)
        assert len(collector1.books_genre()) == 0

    #проверка добавления жанра книги
    def test_set_book_genre_add_book_genre_positive_result(self):
        collector3 = BooksCollector()
        collector3.add_new_book('Терминатор')
        collector3.set_book_genre('Терминатор', 'Фантастика')
        assert collector3.books_genre['Терминатор'] == 'Фантастика'

    #проверка получения жанра книги по её имени
    def test_get_book_genre_by_name_book_positive_result(self):
        collector4 = BooksCollector()
        collector4.add_new_book('Терминатор')
        collector4.set_book_genre('Терминатор', 'Фантастика')
        assert collector4.get_book_genre('Терминатор') == 'Фантастика'

    #проверка отображения списка книг с определённым жанром
    def test_get_books_with_specific_genre_fantastic_positive_result(self):
        collector5 = BooksCollector()
        collector5.add_new_book('Терминатор')
        collector5.set_book_genre('Терминатор', 'Фантастика')
        collector5.add_new_book('Чужой')
        collector5.set_book_genre('Чужой', 'Ужасы')
        collector5.add_new_book('Маска')
        collector5.set_book_genre('Маска', 'Комедии')
        assert collector5.get_books_with_specific_genre('Фантастика') == ['Терминатор']

    #проверка получения словаря books_genre
    def test_get_books_genre_positive_result(self):
        collector6 = BooksCollector()
        collector6.add_new_book('Терминатор')
        collector6.set_book_genre('Терминатор', 'Фантастика')
        assert collector6.get_book_genre('Терминатор') == 'Фантастика'

    # проверка возвращения книги, подходящей детям
    def test_get_books_for_children_positive_result(self):
        collector7 = BooksCollector()
        collector7.add_new_book('Терминатор')
        collector7.set_book_genre('Терминатор', 'Фантастика')
        collector7.add_new_book('Чужой')
        collector7.set_book_genre('Чужой', 'Ужасы')
        collector7.add_new_book('Маска')
        collector7.set_book_genre('Маска', 'Комедии')
        assert collector7.get_books_for_children() == ['Терминатор', 'Маска']

    # проверка добавления книги в Избранное
    def test_add_book_in_favorites_add_correct_genre_positive_result(self):
        collector8 = BooksCollector()
        collector8.add_new_book('Терминатор')
        collector8.add_book_in_favorites('Терминатор')
        assert collector8.favorites == ['Терминатор']

    #проверка удаления книги из Избранного
    def test_delete_book_from_favorites_del_exist_book_positive_result(self):
        collector9 = BooksCollector()
        collector9.add_new_book('Терминатор')
        collector9.add_book_in_favorites('Терминатор')
        collector9.delete_book_from_favorites('Терминатор')
        assert len(collector9.favorites) == 0

    # проверка получения списка Избранных книг
    def test_get_list_of_favorites_books_positive_result(self):
        collector10 = BooksCollector()
        collector10.add_new_book('Терминатор')
        collector10.add_book_in_favorites('Терминатор')
        assert collector10.get_list_of_favorites_books() == ['Терминатор']




    
