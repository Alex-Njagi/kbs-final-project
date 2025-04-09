# LIBRARY BOOK RECOMMENDATION SYSTEM

## A. Project Overview
This project is a library management knowledge based system that recommends books to students based on their preferences. In addition to providing personalised book recommendations, it allows students to create and manage their accounts as well as borrow and return books. As a knowledge based system, it incorporates machine learning techniques for book recommendation based on past reading preferences and current interests. The system also features a comprehensive and intuitive web user interface made using Flask that allows users to carry out said tasks.

## B. Technologies Used
The following technologies were used to develop and test the system over a development period of 4 weeks:
- **Python**: The primary programming language.
- **Pandas**: For handling and analysing the book dataset.
- **scikit-learn**: For encoding categorical data.
- **gdown**: To download the dataset from Google Drive.
- **Excel**: For dataset storage.
- **Flask**: For the web interface.

## C. System Features
The system boasts the following features in an effort to effectively meet its intended objectives:
- **Add Student Profiles**: Create student profiles with preferred genres.
- **Account Management**: Students can view and update their respective accounts to maintain their collections.
- **Book Recommendations**: Suggest books based on preferred genres the latter of which can be updated.
- **Borrowing Books**: Students are allowed to borrow up to 3 books at a time.
- **Returning Books**: Students are able to return any books they have borrowed.
- **Dynamic Recommendations**: Books are recommended evenly across genres and grouped by category.

## D. How It Works
1. **Student Preferences**: Students input their student ID as well as their preferred genres.
2. **Book Recommendation**: Upon enrollment, the system makes some initial suggestions. Students can continue to request new recommendations after the fact as well.
3. **Borrowing Books**: Students can borrow books and have a limit of 3 active borrowed books before being blocked. They are allowed to view their accounts so they can stay on top of their deadlines.
4. **Updating Preferences**: Students can update their preferred genres for new book recommendations.
5. **Returning Books**: Books can be returned and made available for other students.

## E. System Components
### 1️. Data Loading and Preprocessing
The dataset is loaded from a Google Drive link and contains details about books including title, authors, category, and average ratings. The categories are encoded using `LabelEncoder` from scikit-learn to standardise genre categories.

### 2️. Book Recommendation System
- Books are sampled based on the student's preferred genres, and the recommendations are evenly distributed across genres.
- The recommendations are grouped by category and returned in a numbered list.

### 3️. Student Account Management
- Add, update, and delete student profiles.
- View and manage borrowed books.
- Track and recommend books based on updated preferences.

### 4️. User Interface
A simple Flask based web interface allows users to:
- Add students.
- View and update student profiles.
- Borrow and return books.
- View book recommendations.

## F. Setup Instructions
1. Clone or download this repository.
2. Ensure you have the required libraries installed:
<code>pip install pandas scikit-learn gdown</code>
<code>python your_script_name.py</code>

Once you the program is launched, you’ll be presented with a simple menu which the user can interact with the system with:
###    Library System Menu:
    1. Add Student
    2. View Student Account
    3. Update Student Preferences
    4. Borrow Book
    5. Get Book Recommendations
    6. Return Book
    7. Delete Student Account
    8. Exit

## G. Future Enhancements
- **GUI**: Develop a graphical user interface for easier student interaction.
- **Advanced Book Recommendations**: Incorporate more complex recommendation algorithms (e.g., collaborative filtering).
- **Real-time Integration**: Integrate the system with an actual library database.



## H. Authors' Credit
This system was developed by Alex Njagi, Dorcas Mwihaki, Cynthia Yator and Caroline Oriama.
