from flask import Flask, render_template,url_for,request,session,redirect,flash,get_flashed_messages
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin,login_user,logout_user,login_manager,LoginManager,login_required,current_user
from werkzeug.security import generate_password_hash,check_password_hash
from sqlalchemy import text
from flask_mail import Mail
import json

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

class Patients(db.Model):
     pid=db.Column(db.Integer,primary_key=True)
     email=db.Column(db.String(50))
     name=db.Column(db.String(50))
     gender=db.Column(db.String(50))
     slot=db.Column(db.String(50))
     disease=db.Column(db.String(50))
     time = db.Column(db.String(50), nullable=False)
     date = db.Column(db.String(50), nullable=False)
     dept=db.Column(db.String(50))
     number=db.Column(db.String(50))

class Doctors(db.Model):
    did = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(50),unique=True)
    doctorname = db.Column(db.String(50))
    dept = db.Column(db.String(50))

class Trigr(db.Model):
    tid = db.Column(db.Integer,primary_key=True)
    pid = db.Column(db.Integer)
    email = db.Column(db.String(50))
    name = db.Column(db.String(50))
    action = db.Column(db.String(50))
    timestamp = db.Column(db.String(50))









# here we will be creating endpoints and run the funtion ---------->>>
@app.route('/')
def index():
        return render_template('index.html')

@app.route('/doctors', methods=['POST', 'GET'])
@login_required
def doctors():
    if request.method == "POST":
        email = request.form.get('email')
        doctorname = request.form.get('doctorname')
        dept = request.form.get('dept')
        new_doctor = Doctors(
            email=email,
            doctorname=doctorname,
            dept=dept,
        )
        db.session.add(new_doctor)
        db.session.commit()
        flash("Registration confirmed", "info")
    return render_template('doctors.html')

@app.route('/patients', methods=['POST', 'GET'])
@login_required
def patients():
    doct = Doctors.query.all()  # ORM way to retrieve all doctors
    if request.method == "POST":
        email = request.form.get('email')
        name = request.form.get('name')
        gender = request.form.get('gender')
        slot = request.form.get('slot')
        disease = request.form.get('disease')
        time = request.form.get('time')
        date = request.form.get('date')
        dept = request.form.get('dept')
        number = request.form.get('number')

        new_patient = Patients(
            email=email,
            name=name,
            gender=gender,
            slot=slot,
            disease=disease,
            time=time,
            date=date,
            dept=dept,
            number=number
        )
        db.session.add(new_patient)
        db.session.commit()

        flash("Booking confirmed", "info")
    return render_template('patients.html',doct=doct)

@app.route('/bookings')
@login_required
def bookings():
    em = current_user.email
    query = text("SELECT * FROM patients WHERE email = :em")
    with db.engine.connect() as conn:
        result = conn.execute(query, {'em': em}).fetchall()
    return render_template('bookings.html', query=result)

@app.route("/update/<string:pid>", methods=['POST', 'GET'])
@login_required
def update(pid):
    if request.method == "POST":
        email = request.form.get('email')
        name = request.form.get('name')
        gender = request.form.get('gender')
        slot = request.form.get('slot')
        disease = request.form.get('disease')
        time = request.form.get('time')
        date = request.form.get('date')
        dept = request.form.get('dept')
        number = request.form.get('number')
        sql = text("""
            UPDATE patients
            SET email = :email, name = :name, gender = :gender, slot = :slot, disease = :disease, time = :time, date = :date, dept = :dept, number = :number
            WHERE pid = :pid
        """)
        db.session.execute(sql, {
            'email': email,
            'name': name,
            'gender': gender,
            'slot': slot,
            'disease': disease,
            'time': time,
            'date': date,
            'dept': dept,
            'number': number,
            'pid': pid
        })
        db.session.commit()
        flash("Slot updated")
        return redirect('/bookings')
    patient = Patients.query.filter_by(pid=pid).first()
    return render_template("update.html", posts=patient)

@app.route("/delete/<string:pid>", methods=['POST', 'GET'])
@login_required
def delete(pid):
    patient = Patients.query.filter_by(pid=pid).first()
    if patient:
        db.session.delete(patient)
        db.session.commit()
        flash("Deletion done", "danger")
    else:
        flash("Patient not found", "warning")
    return redirect('/bookings')

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

@app.route('/search', methods=['POST', 'GET'])
@login_required
def search():
    if request.method == 'POST':
        query = request.form.get('search')
        
        # Search by department
        dept = Doctors.query.filter_by(dept=query).first()
        
        # Search by doctor name
        name = Doctors.query.filter_by(doctorname=query).first()
        
        if dept:
            flash("Department is Available", "info")
        elif name:
            flash("Doctor is Available", "info")
        else:
            flash("No matching department or doctor found", "danger")

    return render_template('index.html')

@app.route('/details')
@login_required
def details():
    posts = Trigr.query.all()
    return render_template('trigers.html',posts=posts)

app.run(debug=True)