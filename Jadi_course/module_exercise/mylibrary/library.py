class Library:
    books_data = []

    def add_book(self, title, author):
        new_book = {'title': title, 'author': author}
        self.books_data.append(new_book)

    def remove_book(self, title):
        pass

    def search_book(self, title):
        pass

    def show_book(self):
        print("\nBook of your library : ")
        for idx, book in enumerate(self.books_data, start=1):
            print(f"\n{idx}. Title: {book['title']}\nAuthor: {book['author']}")
