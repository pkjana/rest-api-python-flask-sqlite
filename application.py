from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app: Flask = Flask(__name__)


# connect database sqlalchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.db'
db = SQLAlchemy(app)


# Create a database model

class Employee(db.Model):
    id = db.column(db.Integer, primary_key=True)
    name = db.column(db.String(120), unique=True, nulable=False)
    department = db.column(db.String(80))

    def __repr__(self):
        return f"{self.name} - {self.department}"


@app.route('/')
def index():
    return "Welcome to empolyee management system"


@app.route('/employee')
def get_employee():
    return {"employee": "employee data"}


@app.route('/employees')
def get_employees():
    employees = Employee.query.all()

    output = []
    for employee in employees:
        employee_data = {'Name': employee.name, 'Department': employee.department}
        output.append(employee_data)

    return {"employee": output}


@app.route('/employees/<id>')
def get_employee(id):
    employee = Employee.query.get_or_404(id)

    return {'Name': employee.name, 'Department': employee.department}
    # return jsonify({'Name': employee.name, 'Department': employee.department})


@app.route('/employees', methods=['POST'])
def add_employee():
    employee = Employee(name=request.json['name'], department=request.json['department'])
    db.session.add(employee)
    db.session.commit()

    return {'id': employee.id}


@app.route('/employees/<id>')
def delete_employee(id):
    employee = Employee.query.get(id)
    if employee is None:
        return {'error': 'not found'}
    db.session.delete(employee)
    db.session.commit()
    return {"message": "delete successfully"}

