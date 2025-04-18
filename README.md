# LIBRARY BOOK RECOMMENDATION SYSTEM

## A. Project Overview
This project is a library management knowledge based system that recommends books to students based on their preferences. In addition to providing personalised book recommendations, it allows students to create and manage their accounts as well as borrow and return books. As a knowledge based system, it incorporates machine learning techniques for book recommendation based on past reading preferences and current interests. The system also features a comprehensive and intuitive web user interface made using Flask that allows users to carry out said tasks.

## B. Technologies Used
The following technologies were used to develop and test the system over a development period of 4 weeks:
•⁠  ⁠*Pandas*: For handling and analysing the book dataset.
•⁠  ⁠*Python*: The primary programming language.
•⁠  ⁠*Excel*: For dataset storage.
•⁠  ⁠*gdown*: To download the dataset from Google Drive.
•⁠  ⁠*Flask*: For the web interface.
•⁠  ⁠*scikit-learn*: For encoding categorical data.
•⁠  ⁠*VS Code*: For the prototype command line interface.

## C. System Features
The system boasts the following features in an effort to effectively meet its intended objectives:
•⁠  ⁠*Add Student Profiles*: Create student profiles with preferred genres and receive suggestions books based on preferred genres the latter of which can be updated.
•⁠  ⁠*Account Management*: Students can view and update their respective accounts to maintain their collections.
•⁠  ⁠*Dynamic Recommendations*: Books are recommended evenly across genres and grouped by category.
•⁠  ⁠*Borrowing Books*: Students are allowed to borrow up to 3 books at a time.
•⁠  ⁠*Returning Books*: Students are able to return any books they have borrowed.
•⁠  ⁠*Comprehensive Interface*: Students are able to freely browse and access the system's pool of features.

## D. How It Works
1.⁠ ⁠*Student Preferences*: Students input their student ID as well as their preferred genres.
2.⁠ ⁠*Book Recommendation*: Upon enrollment, the system makes some initial suggestions. Students can continue to request new recommendations after the fact as well.
3.⁠ ⁠*Updating Preferences*: Students can update their preferred genres for new book recommendations.
4.⁠ ⁠*Borrowing Books*: Students can borrow books and have a limit of 3 active borrowed books before being blocked. They are allowed to view their accounts so they can stay on top of their deadlines.
5.⁠ ⁠*Returning Books*: Books can be returned and made available for other students.

## E. System Components
### 1️. Data Loading and Preprocessing
The dataset is loaded from a Google Drive link and contains details about books including title, authors, category, and average ratings. The categories are encoded using ⁠ LabelEncoder ⁠ from scikit-learn to standardise genre categories and later decoded to present them in text form in the user interface.

### 2️. Book Recommendation System
•⁠  ⁠Books are sampled based on the student's preferred genres, and the recommendations are evenly distributed across genres. Recommendations are then grouped by category and presented in a numbered list.

### 3️. Student Account Management
•⁠  ⁠Add, update, and delete student profiles.
•⁠  ⁠View and manage borrowed books.
•⁠  ⁠Track and recommend books based on updated preferences.

### 4️. User Interface
A simple Flask based web interface allows users to:
•⁠  ⁠Add students.
•⁠  ⁠View and update student profiles.
•⁠  ⁠Borrow and return books.
•⁠  ⁠View book recommendations.

## F. Setup Instructions
To access the system, simply enter the following url in your browser:
<code>https://kbs-project-app.onrender.com</code>

## G. Future Enhancements
•⁠  ⁠*Advanced Book Recommendations*: Incorporate more complex recommendation algorithms (e.g., collaborative filtering).
•⁠  ⁠*Real-time Integration*: Integrate the system with an actual library database.

## H. Authors' Credit
This system was developed by Alex Njagi, Dorcas Mwihaki, Cynthia Yator and Caroline Oriama.
