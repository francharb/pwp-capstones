from TomeRater import *

Tome_Rater = TomeRater()
Tome_Rater2 = TomeRater()
#Create some books:
print("book1")
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
print("novel1")
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
print("novel1-nlisbn")
novel1.set_isbn(9781536831139)
print("nonfiction1")
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
print("nonfiction2")
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
print("novel2")
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
print("novel3")
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

#Create users:
print("alan")
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
print("david")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
print("marvin et ses 3 livres")
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:

print("book1, alan, 1")
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
print("novel1, alan, 3")
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
print("nonfiction1, alan, 3")
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
print("nonfiction2, alan, 4")
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
print("novel3, alan, 1")
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)
print("novel2, marvin, 2")
Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
print("novel3, marvin, 2")
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
print("novel3, david, 4")
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)


#Uncomment these to test your functions:
print("catalogue")
Tome_Rater.print_catalog()
print("utilisateurs")
Tome_Rater.print_users()

print("Most positive user:")
print(Tome_Rater.most_positive_user())
print("Highest rated book:")
print(Tome_Rater.highest_rated_book())
print("Most read book:")
print(Tome_Rater.most_read_book())

# Print True
if Tome_Rater == Tome_Rater:
    print('True')
else:
    print('False')

# Print False
if Tome_Rater == Tome_Rater2:
    print('True')
else:
    print('False')
