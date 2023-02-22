from datetime import date
from flask import Flask, request ,render_template, Flask, redirect
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
@app.route("/", methods=['POST'])
def verify_post(): 
    if request.method == "POST":
        insert(request.form['person_id'], request.form['first_name'], request.form['last_name'], request.form['email_address'], request.form['hire_date'], request.form['job_title'], "")
        return hello_world()

# gets post using id
# def get_post(post_id):
#     conn = get_db_connection()
#     post = conn.execute('SELECT * FROM Employee WHERE person_id = ?', (post_id)).fetchone()
#     conn.close()
#     if post is  None:
#         abort(404)
#     return post


@app.route('/<person_id>', methods=['POST'])
def delete(person_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM Employee WHERE person_id = ?', (person_id,))
    conn.commit()
    conn.close()
    # flash('"{}" was snapped away!'.format(post['first_name']))
    return redirect("/")
    


# deletes employee by id number
# @app.route('/<person_id>', methods=['GET'])
# def delete(person_id):
#     # return person_id
#     # post = get_post(person_id)
#     conn = get_db_connection()
#     conn.execute('DELETE FROM Employee WHERE person_id = ?', (person_id,))
#     conn.commit()
#     conn.close()
#     # flash('"{}" was snapped away!'.format(post['first_name']))
#     return render_template("index.html")
 

saved_id= None

@app.route('/<person_id>', methods=['POST'])
def save_id(person_id):
    saved_id =person_id

# updates employee by id 
@app.route('/', methods=['POST'])
def edit():
    return render_template("index.html")
    # stored_values= {
    #     "first_name":request.form['first_name'], 
    #     "last_name":request.form['last_name'], 
    #     "email_address":request.form['email_address'], 
    #     "hire_date":request.form['hire_date'], 
    #     "job_title":request.form['job_title'], 
    #     "agency_num":request.form['agency_num'], 
    #     "registration_date":request.form['registration_date']
    # }
    # database = sqlite3.connect('test.db')
    # curser = database.cursor()
        
    # for key, val in stored_values.items():
    #     if not val:
    #         curser.execute(f"UPDATE Employee SET {key} = {val} WHERE person_id = {saved_id};" ) 
            
    # database.commit()
    # database.close()
    # return redirect("/")
          
            

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
