# TODO Найдите количество книг, которое можно разместить на дискете
Volume_in_mbytes = 1.44
Pages = 100
lines = 50
words = 25
safe = 4
Volume_in_bytes = Volume_in_mbytes * 1024 ** 2

count_of_words = Pages * lines * words

safe_book = count_of_words * safe

count_of_book = Volume_in_bytes / safe_book
count_of_book_ = round(count_of_book)

print("Количество книг, помещающихся на дискету:", count_of_book_)
