from src.models.book import Book

def test_book_borrow_true():
    '''Позитивный тест бронирования книги'''
    book = Book ("Алиса в Стране Чудес", "Льюис Кэрролл", 1865 , "1234-12-34")
    assert book.borrow() == "Книга'Алиса в Стране Чудес' выдана"

def test_book_borrow_false():

    book = Book("Алиса в стране чудес", "Льюис Кэрролл", 1865, "1234-12-34")
    book.borrow() 
    assert book.borrow() == "Выдача книги Алиса в стране чудес невозможна!"