class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def get_name(self):
        return self.name

    def change_email(self, address):
        self.email = address
        print("User's email has been updated.")

    def __repr__(self):
        return "User {name}, email: {email}, books read: {number}".format(name=self.name, email=self.email, number=len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        rating_sum = 0
        for i in self.books.keys():
            if self.books[i] is not None:
                rating_sum += self.books[i]
            else:
                continue
        average_rating = rating_sum / len(self.books)
        return average_rating

class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("Book's ISBN has been updated.")

    def add_rating(self, rating):
        if rating is not None and rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating.")

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False

    def get_average_rating(self):
        rating_sum = 0
        for i in self.ratings:
            if i is not None:
                rating_sum += i
            else:
                continue
        average_rating = rating_sum / len(self.ratings)
        return average_rating

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return "{title}".format(title=self.title)

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)

class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        new_book = Book(title, isbn)
        return new_book

    def create_novel(self, title, author, isbn):
        new_fiction = Fiction(title, author, isbn)
        return new_fiction

    def create_non_fiction(self, title, subject, level, isbn):
        new_none_fiction = Non_Fiction(title, subject, level, isbn)
        return new_none_fiction

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users:
            user = self.users.get(email)
            user.read_book(book, rating)
            book.add_rating(rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user with email {email}!".format(email=email))

    def add_user(self, name, email, user_books=None):
        new_user = User(name, email)
        self.users[email] = new_user
        if user_books is not None:
            for i in user_books:
                self.add_book_to_user(i, email)

    def print_catalog(self):
        for i in self.books:
            print(i)

    def print_users(self):
        for i in self.users:
            print(self.users[i])

    def most_read_book(self):
        most_read_value = 0
        most_read_book = None
        for i in self.books:
            if self.books[i] > most_read_value:
                most_read_value = self.books[i]
                most_read_book = i
            else:
                continue
        return most_read_book

    def highest_rated_book(self):
        highest_rating = 0
        highest_rated_book = None
        for i in self.books:
            rating = i.get_average_rating()
            if rating > highest_rating:
                highest_rating = rating
                highest_rated_book = i
            else:
                continue
        return highest_rated_book

    def most_positive_user(self):
        highest_average_rating = 0
        most_positive_user = None
        for i in self.users:
            rating = self.users[i].get_average_rating()
            if rating > highest_average_rating:
                highest_average_rating = rating
                most_positive_user = self.users[i]
        return most_positive_user

    def __repr__(self):
        booklist = []
        userlist = []
        for i in self.books:
            booklist = booklist + [i.get_title()]
        for i in self.users:
            userlist = userlist + [self.users[i].get_name()]
        return "List of books: {booklist}, List of users: {userlist}".format(booklist=booklist, userlist=userlist)

    def __eq__(self, other_TomeRater):
        #step 1: create lists of books and users for object in 1st argument, sort them and create a string for each witch each element
        #create lists
        booklist = []
        userlist = []
        for i in self.books:
            booklist = booklist + [i.get_title()]
        for i in self.users:
            userlist = userlist + [self.users[i].get_name()]
        #sort lists and create strings
        sorted_booklist_str = sorted(' '.join(booklist))
        sorted_userlist_str = sorted(' '.join(userlist))

        #step 2: create lists of books and users for object in 2nd argument, sort them and create a string for each witch each element
        #create lists
        other_booklist = []
        other_userlist = []
        for i in other_TomeRater.books:
            other_booklist = other_booklist + [i.get_title()]
        for i in other_TomeRater.users:
            other_userlist = other_userlist + [other_TomeRater.users[i].get_name()]
        #sort lists and create strings
        sorted_other_booklist_str = sorted(' '.join(other_booklist))
        sorted_other_userlist_str = sorted(' '.join(other_userlist))

        #Step 3: string comparison
        if sorted_booklist_str == sorted_other_booklist_str and sorted_userlist_str == sorted_other_userlist_str:
            return True
        else:
            return False
