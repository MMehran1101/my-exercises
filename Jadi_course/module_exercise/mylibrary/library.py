class Library:
    books_data = []

    def add_book(self, title, author):
        new_book = {'title': title, 'author': author}
        self.books_data.append(new_book)

    def remove_book(self, title):
        for book in self.books_data:
            if book['title'] == title:
                self.books_data.remove(book)
                print(f"'{title}' removed from your library")
            else:
                print(f"'{title}' book is not find.")

    def search_book(self, title):
        pass

    def show_book(self):
        if self.books_data != []:
            print("\nBook of your library : ")
            for idx, book in enumerate(self.books_data, start=1):
                print(f"\n{idx}. Title: {book['title']}\nAuthor: {book['author']}")
        else:
            print("\nYou don't have any book.")
