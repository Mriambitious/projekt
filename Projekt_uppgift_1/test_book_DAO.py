import pytest
import sqlite3
from book import Book
from book_dao import BookDAO
 
 
@pytest.fixture
def book_dao():
    #Förbereder testdatabas
    book_dao = BookDAO(":memory:")  # Använder en temporär minnesdatabas i RAM minnes ist för som en fil ville ej funka med 'file.db'
    book_dao.create_table()  # Skapar tabell
   
    book1= Book('The Shining', 'Horror', 'Stephen King') #Måste skriva Book framför för att lägga in den i Book
    book2= Book('Harry Potter', 'Fantasy', 'JK Rowling')
    book3= Book('Game Of Thrones', 'Action', 'George RR Martin')
   
    book_dao.insert_book(book1) #Behöver ingen 'Self' här för att den bara ska anropa
    book_dao.insert_book(book2)
    book_dao.insert_book(book3)
   
    yield book_dao #yield gör att vi retunerar objektet för användning i testerna
 
    #rensar efter testet
    book_dao.clear_table() #rensar efter varje test
    book_dao.close()
 
 
class TestBookDao:
 
#TEST 1: Hämta alla böcker och verifiera att databasen innehåller 3 böcker
 
    def test_get_all_books(self, book_dao):
        books = book_dao.get_all_books() #Hämtar alla böcker
        assert len(books) == 3 #Testar så att de tre böckerna finns i databasen
 
#TEST 2: Lägg till en ny bok och se till att databasen innehåller 4 böcker
 
    def test_insert_book(self, book_dao):
        new_book=Book('Python från början', 'Kurslitteratur', 'Jan Skansholm') #Skapar en ny book
        book_dao.insert_book(new_book) #Lägger till den nya boken
        books = book_dao.get_all_books() #Hämtar böckerna inklusive nya boken
        assert len(books)==4 #Testar så att databasen nu innehåller 4 böcker
 
#TEST 3: Hämta en bok via titel och verifiera att beskrivningen (description) stämmer med förväntat värde
 
    def test_find_by_title(self, book_dao):
        books = book_dao.get_all_books() #Hämtar alla böcker
        book_title = book_dao.find_by_title("Game Of Thrones")  #Hämtar boken via titel
        assert book_title.description == "Action" #Testar att bookens titel stämmer överens med bokens
 
#TEST 4: Hämta en bok via titel och uppdatera bokens beskrivning, hämta den igen via titel och verifiera att ändringen har slagit igenom
 
    def test_update_book(self, book_dao):
        books = book_dao.get_all_books() #Hämtar alla böcker
        book = book_dao.find_by_title("Harry Potter")  #Hämtar boken via titel
        description= 'Thriller' #Sätter in descriptionen i variabel så att man slipper upprepa 'Thriller'
        book.description= description
        book_dao.update_book(book) #Uppdaterar databasen med ny description
        book = book_dao.find_by_title("Harry Potter") #Hämtar boken igen via titel
        assert book.description == description # Verifierar att ändringarna har slagit igenom
 
#Test 5: Hämta en bok via titel och radera boken, försök sedan hämta den och verifiera att den är == None
 
    def test_delete_book(self, book_dao):
        book= book_dao.find_by_title('The Shining') #Hittar bok via titel
        book_dao.delete_book(book) #Raderar boken
        book= book_dao.find_by_title('The Shining') #Hämtar boken igen
        assert book == None #checkar att boken är borta