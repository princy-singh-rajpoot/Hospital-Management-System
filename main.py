from flask import Flask, render_template,url_for,request,session,redirect,flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin,login_user,logout_user,login_manager,LoginManager,login_required,current_user
from werkzeug.security import generate_password_hash,check_password_hash

#my database connection
local_server = True
app = Flask(__name__)
app.secret_key='princysingh'

# this is for getting unique user access
login_manager=LoginManager(app)
login_manager.login_view='login'

@login_manager.user_loader
def load_user(user_id):
      return User.query.get(int(user_id))





app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/hms'
db=SQLAlchemy(app)

# here we will be creating db models i.e tables --------------->>>>
class Test(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    email=db.Column(db.String(100))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50),unique=True)
    password = db.Column(db.String(1000))













# here we will be creating endpoints and run the funtion ---------->>>
@app.route('/')
def index():
        return render_template('index.html')

@app.route('/doctors')
def doctors():
        return render_template('doctors.html')

@app.route('/patients')  
@login_required
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
            flash("Email already exists", "warning")
            return render_template("signup.html", error="Email already exists")

        encpassword = generate_password_hash(password)
        new_user = User(username=username, email=email, password=encpassword)
        try:
            db.session.add(new_user)
            db.session.commit()
            flash("Signup successful, please log in", "success")
            return redirect(url_for('login'))  # Redirect to login page after successful signup
        except Exception as e:
            print(f"Error occurred: {e}")
            db.session.rollback()
            flash("An error occurred during signup", "danger")
            return render_template("signup.html", error="An error occurred during signup")

    # GET request handling
    return render_template("signup.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)  # This should log in the user
            flash("login done","primary") 
            return redirect(url_for('index'))  # Redirects to index page after login
        else:
            flash("Invalid information","danger")
            return render_template('login.html')

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
        logout_user()
        flash("logout done","primary")
        return redirect(url_for('login'))

@app.route('/test')
def test():
    try:
        Test.query.all( )
        return 'my db is conn'
    except:
        return 'my db is not conn'


app.run(debug=True)