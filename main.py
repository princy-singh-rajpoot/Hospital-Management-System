from flask import Flask, render_template,request,session,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin,login_user,logout_user
from werkzeug.security import generate_password_hash,check_password_hash

#my database connection
local_server = True
app = Flask(__name__)
app.secret_key='princysingh'

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/hms'
db=SQLAlchemy(app)

# here we will be creating db models i.e tables --------------->>>>
class Test(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    email=db.Column(db.String(100))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)  # Set unique=True
    password = db.Column(db.String(4))

# here we will be creating endpoints and run the funtion ---------->>>
@app.route('/')
def index():
        return render_template('index.html')

@app.route('/doctors')
def doctors():
        return render_template('doctors.html')

@app.route('/patients')
def patients():
        return render_template('patients.html')

@app.route('/bookings')
def bookings():
        return render_template('bookings.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == "POST":
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        
        if user:
            print("Email already exists")
            return render_template("signup.html", error="Email already exists")

        encpassword = generate_password_hash(password)
        new_user = User(username=username, email=email, password=encpassword)

        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect('/login')  # Redirect to login page after successful signup
        except Exception as e:
            print(f"Error occurred: {e}")
            db.session.rollback()
            return render_template("signup.html", error="An error occurred during signup")

    return render_template("signup.html")  # For GET requests, just render the signup page

@app.route('/login')
def login():
        return render_template('login.html')

@app.route('/logout')
def logout():
        return render_template('logout.html')

@app.route('/test')
def test():
    try:
        Test.query.all( )
        return 'my db is conn'
    except:
        return 'my db is not conn'


app.run(debug=True)