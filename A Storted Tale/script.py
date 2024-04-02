import utils
import sorts

bookshelf = utils.load_books('books_small.csv')
long_bookshelf = utils.load_books('books_large.csv')
bookshelf_v1 = bookshelf[:]
bookshelf_v2 = bookshelf[:]

for book in bookshelf:
  print(book)

print(ord("a"))
print(ord(" "))
print(ord("A"))

def by_title_ascending(book_a, book_b):
  return book_a['title_lower'] > book_b['title_lower']
def by_author_ascending(book_a, book_b):
  return book_a["author_lower"] > book_b["author_lower"]
def by_total_length(book_a, book_b):
  return len(book_a['title_lower']) + len(book_a['author_lower']) > len(book_b['title_lower']) + len(book_b['author_lower'])
  
sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)
sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)
#sorts.bubble_sort(long_bookshelf, by_total_length)
sorts.quicksort(long_bookshelf, 0, len(long_bookshelf) -1, by_total_length)

for book in sort_1:
  print(book['title'])
print()
for book in sort_2:
  print(book['author'])
print()
for book in bookshelf_v2:
  print(book['author'])
print()