# To run the program enter the command: python app.py or python3 app.py in the terminal
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import gdown
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Importing and processing dataset
file_id = "1YZpUyMz7ZWKx3tPS-j2kLijCuVPDsjl0"
gdown.download(f"https://drive.google.com/uc?export=download&id={file_id}", 'books_with_genre.xlsx', quiet=False)
books_xlsx_path = "books_with_genre.xlsx"
books_df = pd.read_excel(books_xlsx_path)
books_df.columns = books_df.columns.str.strip()

# Encode categorical variables
label_encoder = LabelEncoder()  # Initialize label encoder
books_df["category"] = label_encoder.fit_transform(books_df["category"]) # Encode genre categories

students = {}   # Dictionary to store student data
MAX_BORROW_LIMIT = 3    # Maximum number of books a student can borrow

# Function to recommend books based on student preferences with a more even split across genres
def recommend_books(student_id):
    preferred_genres = students[student_id]["preferred_genres"] # Access the student's preferred genres
    category_labels = label_encoder.transform(preferred_genres) # Encode the preferred genres
    recommendations = []    # List to store recommended books
    num_books_per_category = max(6 // len(category_labels), 1)  # Distribute books evenly according to the number of preferred genres
    
    for category in category_labels:
        category_books = books_df[books_df["category"] == category] # Filter books by category
        sampled_books = category_books.sample(min(num_books_per_category, len(category_books))) # Sample books from the category
        recommendations.append(sampled_books)   # Create recommended list from sampled books
    
    recommended_books = pd.concat(recommendations)  # Concatenate the recommended books and return
    return recommended_books[["title", "authors", "category", "average_rating", "publication_date", "publisher"]]

# Function for borrowing a book
def borrow_book(student_id, book_title):
    if student_id in students:  # Check if student exists
        if book_title in books_df["title"].values:  # Check if the book exists in the dataset
            if len(students[student_id]["borrowed_books"]) < MAX_BORROW_LIMIT:  # Check borrowing limit
                students[student_id]["borrowed_books"].append(book_title)   # Add the book to the student's borrowed list
                return f'"{book_title}" borrowed successfully.'
            else:
                return "Borrowing limit reached! Return a book before borrowing a new one."
        else:
            return "Book not found in the system!"
    else:
        return "Student not found!"

# Function for returning a book
def return_book(student_id, book_title):
    if student_id in students:  # Check if student exists
        if book_title in students[student_id]["borrowed_books"]:    # Check if the book is in the borrowed list
            students[student_id]["borrowed_books"].remove(book_title)   # Remove the book from the borrowed list
            return f"{book_title} returned successfully."
        else:
            return "This book is not in the borrowed books list!"
    else:
        return "Student not found!"

# ROUTING SECTION
# Route for home page
@app.route('/')
def home():
    return render_template('index.html')    # Render the home page

# Define allowed genres based on your dataset
ALLOWED_GENRES = {
    "Biography", "Business", "Fantasy", "General Fiction", "History", "Horror",
    "Mystery", "Philosophy", "Psychology", "Romance", "Self-Help", "Science Fiction", "Thriller"
}

@app.route('/add_student', methods=['GET', 'POST'])
def add_student_route():
    if request.method == 'POST':
        student_id = request.form['student_id']
        raw_genres = request.form['preferred_genres'].split(',')
        preferred_genres = [genre.strip() for genre in raw_genres]

        # Validate genres
        invalid_genres = [genre for genre in preferred_genres if genre not in ALLOWED_GENRES]
        
        if invalid_genres:
            message = f"The following genres are invalid: {', '.join(invalid_genres)}"
            return render_template('add_student.html', recommendations=pd.DataFrame(), message=message)

        # Save valid data
        students[student_id] = {"preferred_genres": preferred_genres, "borrowed_books": []}
        recommendations = recommend_books(student_id)
        return render_template('add_student.html', recommendations=recommendations)

    return render_template('add_student.html', recommendations=pd.DataFrame())


# # Route for adding a student
# @app.route('/add_student', methods = ['GET', 'POST'])
# def add_student_route():
#     if request.method == 'POST':    # Check if the form is submitted
#         student_id = request.form['student_id'] # Get the student ID from the form
#         preferred_genres = request.form['preferred_genres'].split(',')  # Split the preferred genres by comma
#         students[student_id] = {"preferred_genres": preferred_genres, "borrowed_books": []} # Store student data in the dictionary
#         recommendations = recommend_books(student_id)  # Get initial recommendations
#         return render_template('add_student.html', recommendations = recommendations)  # Pass recommendations to template
#     return render_template('add_student.html', recommendations = pd.DataFrame())    # Render the add student page with an empty recommendations DataFrame
    
# Route for viewing a student account
@app.route('/view_student', methods = ['GET', 'POST'])
def view_student_route():
    message = None
    if request.method == 'POST':
        student_id = request.form['student_id']
        if student_id in students:
            student = students[student_id]
            return render_template('view_student.html', student = student, student_id = student_id) # Render the view student page with student data
        else:
            message = "Student not found!"
    return render_template('view_student_form.html', message = message)  # Render the view student form page with an optional message

# Route for deleting a student account
@app.route('/delete_student', methods = ['POST'])
def delete_student_route():
    student_id = str(request.form.get('student_id'))  # Get the student ID from the form
    if student_id in students:
        borrowed_books = students[student_id]["borrowed_books"]
        if borrowed_books:
            # Block deletion if there are borrowed books
            message = "You must return all borrowed books before deleting your account."
            return render_template('view_student.html', student_id = student_id, student = students[student_id], message = message)
        else:
            # Allow deletion if no borrowed books
            del students[student_id]
            print(f"Student {student_id} deleted.")
            return render_template('confirm_delete.html')  # Show confirmation message
    else:
        print("Student not found!")
        return redirect(url_for('view_student_form'))

# Route for updating a student account
@app.route('/update_student/<student_id>', methods = ['GET', 'POST'])
def update_student_form(student_id):
    if student_id not in students:
        return "Student not found!"
    if request.method == 'POST':
        new_genres = request.form['preferred_genres']
        genre_list = [genre.strip() for genre in new_genres.split(',')]
        students[student_id]['preferred_genres'] = genre_list
        message = "Student information updated successfully!"
        return render_template('update_student_form.html', student = students[student_id], student_id = student_id, message = message)
    return render_template('update_student_form.html', student = students[student_id], student_id = student_id)

# Route for borrowing a book
@app.route('/borrow_book', methods = ['GET', 'POST'])
def borrow_book_route():
    message = None
    if request.method == 'POST':
        student_id = request.form['student_id']
        book_title = request.form['book_title']
        message = borrow_book(student_id, book_title)   # Call the borrow_book function to borrow a book
    return render_template('borrow_book_form.html', message = message)

# Route for returning a book
@app.route('/return_book', methods = ['GET', 'POST'])
def return_book_route():
    if request.method == 'POST':
        student_id = request.form['student_id']
        book_title = request.form.get('book_title')
        if student_id in students:
            borrowed_books = students[student_id]["borrowed_books"]
            if book_title:  # Only try to return a book if one is submitted
                message = return_book(student_id, book_title)
                return render_template('return_book.html', student_id = student_id, borrowed_books = borrowed_books, message = message)
            else:
                # No book submitted yet — just show the form without a message
                return render_template('return_book.html', student_id = student_id, borrowed_books = borrowed_books)
        else:
            return "Student not found!"
    return render_template('return_book_form.html')  # Show form to enter student ID on GET

# Route for book recommendations
@app.route('/recommend_books', methods = ['GET', 'POST'])
def recommend_books_route():
    message = None
    if request.method == 'POST':
        student_id = request.form['student_id']
        if student_id in students:
            recommendations = recommend_books(student_id)  # Call the recommend_books function
            print(f"Recommendations for {student_id}: {recommendations}")  # Log the recommendations
            return render_template('recommend_books.html', recommendations = recommendations)
        else:
            message = "Student not found!"
    return render_template('recommend_books_form.html', message = message)

# Run the app
if __name__ == "__main__":
    app.run()
