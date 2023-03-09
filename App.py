from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

#create the object of Flask
app = Flask(__name__)
app.secret_key = "yvesnoel"

#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://yvesnoel:Nkeng2001@localhost/flaskcrud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create the SQLAlchemy object
db = SQLAlchemy()





# Creating model tables for our CRUD database
class StudentsData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    credits = db.Column(db.String(100))

    def __init__(self, name, credits):
        self.name = name
        self.credits = credits


class InstructorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    department = db.Column(db.String(100))

    def __init__(self, name, department):
        self.name = name
        self.department = department


class CourseData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(100))
    instructor = db.Column(db.String(100))

    def __init__(self, course, instructor):
        self.course = course
        self.instructor = instructor





#creating our routes
@app.route('/')
def Index():
    all_data = StudentsData.query.all()
    all_data1 = InstructorData.query.all()
    all_data2 = CourseData.query.all()
    return render_template("index.html", students = all_data, instructors = all_data1, courses = all_data2)




#this route is for inserting data to mysql database via html forms
@app.route('/insert', methods = ['POST'])
def insert():
 
    if request.method == 'POST':
 
        name = request.form['name']
        credits = request.form['credits']
 
 
        my_data = StudentsData(name, credits)
        db.session.add(my_data)
        db.session.commit()
 
        flash("Student Inserted Successfully")
 
        return redirect(url_for('Index'))
    

@app.route('/insert1', methods = ['POST'])
def insert1():
 
    if request.method == 'POST':
 
        name = request.form['name']
        department = request.form['department']
 
 
        my_data = InstructorData(name, department)
        db.session.add(my_data)
        db.session.commit()
 
        flash("Instructor Inserted Successfully")
 
        return redirect(url_for('Index'))


@app.route('/insert2', methods = ['POST'])
def insert2():
 
    if request.method == 'POST':
 
        course = request.form['course']
        instructor = request.form['instructor']
 
 
        my_data = CourseData(course, instructor)
        db.session.add(my_data)
        db.session.commit()
 
        flash("Course Inserted Successfully")
 
        return redirect(url_for('Index'))
    




#this is our update route where we are going to update our data
@app.route('/update', methods = ['GET', 'POST'])
def update():
 
    if request.method == 'POST':
        my_data = StudentsData.query.get(request.form.get('id'))
 
        my_data.name = request.form['name']
        my_data.credits = request.form['credits']
 
        db.session.commit()
        flash("Student Info Updated Successfully")
 
        return redirect(url_for('Index'))
    

@app.route('/update1', methods = ['GET', 'POST'])
def update1():
 
    if request.method == 'POST':
        my_data = InstructorData.query.get(request.form.get('id'))
 
        my_data.name = request.form['name']
        my_data.department = request.form['department']
 
        db.session.commit()
        flash("Instructor Info Updated Successfully")
 
        return redirect(url_for('Index'))
    

@app.route('/update2', methods = ['GET', 'POST'])
def update2():
 
    if request.method == 'POST':
        my_data = CourseData.query.get(request.form.get('id'))
 
        my_data.course = request.form['course']
        my_data.instructor = request.form['instructor']
 
        db.session.commit()
        flash("Course Info Updated Successfully")
 
        return redirect(url_for('Index'))
    




#this route is for deleting our data
@app.route('/delete/<id>/', methods=['GET', 'POST'])
def delete(id):
    my_data = StudentsData.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Student Info Deleted Successfully")

    return redirect(url_for('Index'))


@app.route('/delete1/<id>/', methods=['GET', 'POST'])
def delete1(id):
    my_data = InstructorData.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Instructor Info Deleted Successfully")

    return redirect(url_for('Index'))


@app.route('/delete2/<id>/', methods=['GET', 'POST'])
def delete2(id):
    my_data = CourseData.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Course Info Deleted Successfully")

    return redirect(url_for('Index'))



    

# set up the application context
with app.app_context():
    # initialize the SQLAlchemy object with the app
    db.init_app(app)
    # create all tables
    db.create_all()

# run flask app
if __name__ == "__main__":
    app.run(debug=True)