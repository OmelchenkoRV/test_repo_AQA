import requests

book_template = {'title': 'Great expectation', 'author': 'Charles Dickens'}
book_change = {'title': 'The Old Curiosity Shop', 'author': 'Charles Dickens'}
URL = 'http://pulse-rest-testing.herokuapp.com/books'

post_book_response = requests.post(URL, data=book_template)
book_id = post_book_response.json()
_id = book_id.get('id')
print(_id)

URL_id = URL + '/' + str(_id)
get_book_by_id = requests.get(URL_id)
if get_book_by_id.status_code == 200:
    print('Book has been successfully added')
else:
    raise Warning('Something went wrong')

get_all_books_response = requests.get(URL)
books_list = get_all_books_response.json()
for item in books_list:

    if _id not in item.values():
        pass
else:
    print('Book is in the list')
put_book = requests.put(URL_id, data=book_change)
print(put_book)
get_book_by_id = requests.get(URL_id)
if get_book_by_id.status_code == 200:
    print('Book has been successfully changed')
else:
    raise Warning('Something went wrong')

get_all_books_response = requests.get(URL)
books_list = get_all_books_response.json()
for item in books_list:

    if item['title'] == book_change['title'] and item['author'] == book_change['author']:
        print('Book is in the list after change')
delete_book = requests.delete(URL + '/' + str(_id))
print(delete_book, 'Book has been successfully deleted')
