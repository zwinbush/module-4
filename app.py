from flask import Flask, request, jsonify

app = Flask(__name__)

books = [
    {
        "id": 1,
        "book_name": "Harry Potter",
        "author": "J.K. Rowling",
        "publisher": "Bloomsbury"
    }
]

# GET - Retrieve all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)


# GET - Retrieve a specific book
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    for book in books:
        if book["id"] == id:
            return jsonify(book)

    return jsonify({"message": "Book not found"}), 404


# POST - Add a new book
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()

    new_book["id"] = len(books) + 1

    books.append(new_book)

    return jsonify(new_book), 201


# PUT - Update an existing book
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    for book in books:
        if book["id"] == id:
            updated_book = request.get_json()

            book["book_name"] = updated_book["book_name"]
            book["author"] = updated_book["author"]
            book["publisher"] = updated_book["publisher"]

            return jsonify(book)

    return jsonify({"message": "Book not found"}), 404


# DELETE - Remove a book
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    for book in books:
        if book["id"] == id:
            books.remove(book)

            return jsonify({"message": "Book deleted successfully"})

    return jsonify({"message": "Book not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)