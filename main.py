from flask import Flask, render_template,request,session,redirect
from flask_sqlalchemy import SQLAlchemy

#my database connection
local_server = True
app = Flask(__name__)
app.secret_key='princysingh'

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/hms'
db=SQLAlchemy(app)


# here we will be creating db models i.e tables
class Test(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    email=db.Column(db.String(100))

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

@app.route('/signup',methods=['POST','GET'])
def signup():
        if request.method=="POST":
               username=request.form.get(username)
               email=request.form.get(email)
               password=request.form.get(password)
        return render_template('signup.html')

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