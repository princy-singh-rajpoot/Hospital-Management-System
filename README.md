## Project Title
Hospital Management System

## Description - 
This is a Flask-based web application for managing hospital operations, including managing patients, doctors, and appointments. The application provides functionalities for user authentication, patient registration, and searching for doctors and departments.

### Prerequisites

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-Mail
- MySQL (for the database)

### Installation Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```

2. Configure the database:

   - Set up your MySQL database and update the database URI in the `main.py` file:

     ```python
     app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/dbname'
     <!-- app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/hms' (hms is my db name)-->
     In, PhpMyAdmin, import the hms.sql file.
     ```

5. Run the application:

   ```
   python main.py
   ```

## Usage

- Navigate to `http://localhost:5000` in your browser to access the application.
- Use the available routes to register patients, manage doctor details, and more.

## Database Models

- **User**: Handles user authentication.
- **Patients**: Stores information about patients.
- **Doctors**: Stores information about doctors, including their department.
- **Test**: A sample model for demonstration.
- **Trigr**: Stores data related to a specific trigger (not fully detailed). It stores information related to patients whether they are added,updated or deleted.

## Routes

- `/login`: User login page.
- `/register`: User registration page.
- `/search`: Search functionality for doctors and departments.
- `/doctors`: dDoctor registration page.
- `/patients`: Patients Registration Page
- `/booking`: Patient Booking page.

## Contributing

Contributions are welcome! Please create a pull request or submit an issue if you find any bugs.

## Contact

For any queries, please contact [princyvandanasingh@gmail.com].