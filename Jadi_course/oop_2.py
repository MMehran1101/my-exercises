class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.title}, {self.author}, {self.isbn}"

    def __repr__(self):
        return self.__str__()

class Member:
    def __init__(self, name, member_id, borrowed_book=None):
        self.name = name
        self.id = member_id
        self.borrowed = borrowed_book if borrowed_book is not None else []

    def __str__(self):
        return f"{self.name},{self.id}"

    def borrow_book(self, book):
        self.borrowed.append(book)

    def return_book(self, book):
        self.borrowed.remove(book)


class Library:
    def __init__(self, books: list[Book], members: list[Member]):
        self.books = books
        self.members = members

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def show_books(self):
        for i in self.books:
            print(i)

    def lend_book(self, book, member):
        member.borrow_book(book)

    def receive_book(self, book, member):
        member.return_book(book)


rh_b = Book('Remind of Her', 'Cillian', 64891)
blind_b = Book("Blindness", 'Alas', 44444)

mehran_m = Member("Mehran Fallah", 25616961)

library = Library([rh_b, blind_b], [mehran_m])

library.lend_book(rh_b, mehran_m)


print(mehran_m.borrowed)
