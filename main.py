# Import stack
import mysql.connector
from datetime import date
import requests

"""
#TODO
    Connect http methonds
    create git ignore
    FIX VALIDATOR for email and positions
    ADD Functionalty to edit and delete button on Employee table.
    Remove Array from html
    Fix valid date on Hire page
    Add CSS TO Employee table
"""

# Initialize SQL Database
database = mysql.connector.connect(
    host = "localhost",
    user = "branden",
    password = "T3chn0l0gy",
    database = "Employee"
)


curser = database.cursor()


# Gets and views data from Employees table
curser.execute("SELECT * FROM Employee")
results = curser.fetchall()

# array to store data
data = []

#loop through results and makes data nice.
for row in results:
    data.append("<tr>")
    for values in row:
        data.append(f"<td>{values}</td>")
        
    data.append('<td><p data-placement="top" data-toggle="tooltip" title="Edit"><button class="btn btn-primary btn-xs" data-title="Edit" data-toggle="modal" data-target="#edit" ><span class="glyphicon glyphicon-pencil"></span></button></p></td>')
    data.append('<td><p data-placement="top" data-toggle="tooltip" title="Delete"><button class="btn btn-danger btn-xs" data-title="Delete" data-toggle="modal" data-target="#delete" ><span class="glyphicon glyphicon-trash"></span></button></p></td></tr>')
    
    
# builds html page to store table. 
contents = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
    <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/js/bootstrap.min.js"></script>
    <script src="//code.jquery.com/jquery-1.11.1.min.js"></script>
    <title>Document</title>
</head>
<body>

<div class="container">
	<div class="row">
		        
        <div class="col-md-12">
        <h4>Employee Table</h4>
        <a href="index.html"class="btn btn-primary float-right" role="button">New Employee</a>
        <div class="table-responsive">
                
              <table id="mytable" class="table table-bordred table-striped">

                <tr>
                <th>ID</th> 
                <th>First Name</th> 
                <th>Last Name</th> 
                <th>Email</th> 
                <th>Hire Date</th> 
                <th>Job Title</th> 
                <th>Agency Number</th> 
                <th>Regrisdtation Date</th> 
                <th>Edit</th>
                <th>Delete</th>
                </tr>

 <tbody>
    
{data}    

    </tbody>
        
                </table>            
        </div>
	</div>
</div>
</body>
</html>
'''

# set file name to table.html
filename = 'table.html'


# deletes employee by id number
def delete(person_id):
    curser.execute(f"DELETE FROM Employee WHERE person_id = '{person_id}'; ")
 

# updates employee by id 
def update(person_id, set_by):
    
    # loop through dictinary to get column, value
    for key, val in set_by.items():
        curser.execute(f"UPDATE Employee SET '{key}' = '{val}' WHERE person_id = '{person_id}';")


# insert data to sql
def insert(person_id, first_name, last_name, email_address, hire_date, job_title, agency_num):
    curser.execute("INSERT INTO Employee"
               "(person_id, first_name, last_name, email_address, hire_date, job_title, agency_num, registration_date)"
               f"VALUES ('{person_id}', '{first_name}','{last_name}','{email_address}','{hire_date}','{job_title}','{agency_num}','{date.today()}')")



payload = {"person_id": "", "first_name":"", "last_name":"", "email_address":"", "hire_date":"", "job_title":"", "agency_num":""}
# response = requests.get("https://bherna33.github.io/RCG/get")
response = requests.post("http://127.0.0.1:5500/index.html/post", data=payload)
print(response)


def main(contents, filename):
    
    # write to file 
    output = open(filename,"w")
    output.write(contents)
    output.close()
    
    # closes data base
    database.commit()
    database.close()

main(contents, filename)