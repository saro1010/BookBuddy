

## BookBuddy – Python CLI Application
<br>

#### BookBuddy is a command-line Python application designed to help readers manage their personal library and track their reading habits.
<br>
The program allows users to add books, record reading sessions, and monitor their overall progress.
This version includes the core required features from the assignment without any optional additions.

___

---

***


### 📌 Overview
> #### simple reading-management tool where users can:

+ Build and maintain their personal library

+ Track pages they read over time

+ Review reading statistics and progress

+ Store and retrieve data using basic file handling
___

---

***

## 📚 Main Features
<br>

>#### ✔️ Add New Books
>> #### Users can register books with the following details
+ Title

+ Author

+ Genre

+ Total pages

+ Date added

<br> 

> #### ✔️ Log Reading Sessions
>>Each reading session includes:
+ Reading date
+ Pages reads

+ Optional notes

<br>

>#### ✔️ View Library

+ Display a list of all registered books
+ Show authors, genres, and total pages

<br>

> #### ✔️ View Reading Progress

+ Track how many pages have been read

+ Calculate and display completion percentage

<br>

> #### ✔️ Basic Data Storage

+ Data is saved and loaded using simple file handling (e.g., JSON)

<br>

### 📂  Project Structure :
```
BookBuddy/
├── models/
│   ├── book.py
│   ├── ebook.py
│   ├── audiobook.py
│   └── reading_log.py
│
├── services/
│   ├── reading_tracker.py
│   └── progress_manager.py
│
├── storage/
│   └── json_handler.py
│
├── main.py
└── README.md
```
<br>

### ▶️ How to Run

```
python main.py
```
