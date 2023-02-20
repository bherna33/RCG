import mysql.connector
import datetime
import requests
import webbrowser

"""
#TODO
    Connect http methonds
    create git ignore
    FIX VALIDATOR
"""


mydb = mysql.connector.connect(
    host = "localhost",
    user = "branden",
    password = "T3chn0l0gy",
    database = "Employee"
)

if mydb:
    print("sucessfull")
else:
    print("oh no, I'm not conntected")

curser = mydb.cursor()

# curser.execute("INSERT INTO Employee"
#                "(person_id, first_name, last_name, email_address, hire_date, job_title, agency_num, registration_date)"
#                "VALUES ('7', 'branden','hernandez','b@t.com','2023-02-19','aa','2','2023-02-18')")

curser.execute("SELECT * FROM Employee")

resuts = curser.fetchall()

p = []

tbl ="<tr><th>ID</th> <th>First Name</th> <th>Last Name</th> <th>Email</th> <th>Hire Date</th> <th>Job Title</th> <th>Agency Number</th> <th>Regrisdtation Date</th> <th>Edit</th><th>Delete</th></tr>"

    

for row in resuts:
    a = "<tr><td>%s</td>"%row[0]
    p.append(a)
    b = "<td>%s</td>"%row[1]
    p.append(b)
    c = "<td>%s</td>"%row[2]
    p.append(c)
    d = "<td>%s</td>"%row[3]
    p.append(d)
    e = "<td>%s</td>"%row[4]
    p.append(e)
    f = "<td>%s</td>"%row[5]
    p.append(f)
    j = "<td>%s</td>"%row[6]
    p.append(j)
    k = "<td>%s</td>"%row[7]
    p.append(k)
    l = '<td><p data-placement="top" data-toggle="tooltip" title="Edit"><button class="btn btn-primary btn-xs" data-title="Edit" data-toggle="modal" data-target="#edit" ><span class="glyphicon glyphicon-pencil"></span></button></p></td>'
    p.append(l)
    q = '<td><p data-placement="top" data-toggle="tooltip" title="Delete"><button class="btn btn-danger btn-xs" data-title="Delete" data-toggle="modal" data-target="#delete" ><span class="glyphicon glyphicon-trash"></span></button></p></td></tr>'
    p.append(q)
    
contents = '''<!DOCTYPE html>
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
        <a href="/index.html"class="btn btn-primary float-right" role="button">New Employee</a>
        <div class="table-responsive">
                
              <table id="mytable" class="table table-bordred table-striped">

%s
 <tbody>
    
%s    
    </tbody>
        
                </table>            
        </div>
	</div>
</div>
</body>
</html>
'''%(tbl, p)

filename = 'table.html'

# curser.execute("INSERT INTO Employee"
#                "(person_id, first_name, last_name, email_address, hire_date, job_title, agency_num, registration_date)"
#                "VALUES ('2', 'branden','hernandez','b@t.com','2023-02-19','aa','2','2023-02-18')")


# curser.execute("DELETE FROM Employee WHERE person_id = '2'; ")

# curser.execute("UPDATE Employee SET first_name = 'justyn' WHERE person_id = '1';")



mydb.commit()


def main(contents, filename):
    output = open(filename,"w")
    output.write(contents)
    output.close()

main(contents, filename)    
webbrowser.open(filename)

if(mydb.is_connected()):
    curser.close()
    mydb.close()
    print("MySQL connection is closed.") 


# api = "https://www.geeksforgeeks.org/get-post-requests-using-python/"
# responce = requests.get(api)
# print(responce.json())
