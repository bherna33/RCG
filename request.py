from datetime import date
from flask import Flask, request ,render_template, Flask, abort, flash
import sqlite3

# creates flask APP
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///test.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATION'] = True

# get database connection
def get_db_connection():
    conn = sqlite3.connect('test.db')
    conn.row_factory = sqlite3.Row
    return conn

# updates homepage
@app.route("/")
def hello_world():
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM Employee').fetchall()
    conn.close()
    return render_template("index.html", posts=post)

# gets POST or GET responts 
@app.route("/", methods=['GET','POST'])
def verify_post(): 
    if request.method == "POST":
        insert(request.form['person_id'], request.form['first_name'], request.form['last_name'], request.form['email_address'], request.form['hire_date'], request.form['job_title'], "")
        return hello_world()

# gets post using id
def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM Employee WHERE person_id = ?', (post_id)).fetchone()
    conn.close()
    if post is  None:
        abort(404)
    return post


# deletes employee by id number
@app.route('/', methods=['POST'])
def delete(person_id):
    post = get_post(person_id)
    conn = get_db_connection()
    conn.execute('DELETE FROM Employee WHERE person_id = ?', (person_id))
    conn.commit()
    conn.close()
    flash('"{}" was snapped away!'.format(post['first_name']))
    # curser.execute(f"DELETE FROM Employee WHERE person_id = '{person_id}'; ")
    return render_template("index.html")
 

# updates employee by id 
@app.route('/<int:id>/edit/', methods=['POST'])
def edit(person_id, set_by):
    post = get_post(person_id)
    
    # loop through dictinary to get column, value
    for key, val in set_by.items():
        # curser.execute(f"UPDATE Employee SET '{key}' = '{val}' WHERE person_id = '{person_id}';")
        pass


# insert data to sql
def insert(person_id, first_name, last_name, email_address, hire_date, job_title, agency_num):
    database = sqlite3.connect('test.db')
    curser = database.cursor()
    curser.execute("INSERT INTO Employee (person_id, first_name, last_name, email_address, hire_date, job_title, agency_num, registration_date) VALUES(?,?,?,?,?,?,?,?)", (person_id, first_name, last_name, email_address, hire_date, job_title, agency_num, date.today() ) )
    database.commit()
    database.close()

# main function.
if __name__ == '__main__':
    app.run(debug=True)
