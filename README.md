# Project Name: rest-api-python-flask-sqlite
REST API using python flask sqlite

Create a project using PyCharm IDE it will add virtual environmrnt(.venv) through a some steps

OR

## Create a project manually as per above project name.

### create virtual environment (.venv)

$ python3 -m venv .venv

activate the environment

$ source .venv/bin/activate

install dependency

$ pip3 install flask

$ pip3 install flask_sqlalchemy 

$ pip3 freeze > requirement.txt

$ touch application.py  or ni application.py


To run Flask app we need to export some variable fi you restart the editor need to rerun the following commands 
       
$ export FLASK_APP = application.py

For pycharm windows run lines below on the terminal (powersell):
set FLASK_APP=application.py
$env:FLASK_APP = "application.py" 

#Since version 2.3.0, Flask has replaced FLASK_ENV=development with FLASK_DEBUG=1
$Env:FLASK_DEBUG=1


$ export FLASK_ENV = development
$Env:FLASK_ENV = development  //for powersell

#Since version 2.3.0, Flask has replaced FLASK_ENV=development with FLASK_DEBUG=1
$ export FLASK_DEBUG=1 
$Env:FLASK_DEBUG=1


$ flask run


First add db model class to application 
db creation  
ctrl+c to exit from devlopment server console
$ python3
>>> from application import db
To create a table 
>>> db.create_all()
>>> from application import Employee
>>> employee = Employee(name="Rama", department="Sales")
>>> employee  # display the employee data
>>> db.session.add(employee)
>>> db.session.commit()
>>> Employee.query.all()  # display data from Employee db
to add another record to Employee db
>>> db.session.add(Employee(name="Cherry", department="HR"))
>>> db.session.commit()
>>> Employee.query.all()
exit and go back to flask
>>> exit()

$ flask run

## use postman to test rest api





