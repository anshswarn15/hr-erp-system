from email import message
from flask import Flask, render_template, request, session
import pymysql

app = Flask(__name__)
app.secret_key = "my_super_secret_key_123"

# MySQL connection
con = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="hr_erp_db"
)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/adminlogin")
def adminlogin():
    return render_template("adminLogin.html")

@app.route("/contactus")
def contactus():
    return render_template("contactus.html")

@app.route("/admindashboard",methods = ['post'])
def admindashboard():
    u = request.form['usernametxt']
    p = request.form['passwordtxt']

    if u == 'admin' and p == 'super' :
        session["name"] = "Anshuk"
        return render_template("admin_dashboard.html")
    else:
        message = 'Invalid Username and Password!'

        return render_template('adminLogin.html',status = message)

@app.route("/adminaddemp")
def adminaddemp():
    return render_template("admin_addemp.html")

@app.route("/adminsearchemp")
def adminsearchemp():
    return render_template("admin_searchemp.html")

@app.route("/adminshowemp")
def adminshowemp():

    cur = con.cursor()

    cur.execute("select empid,empname,designation from registration")

    emplist = cur.fetchall()

    return render_template("admin_showemp.html",recordlist = emplist)

@app.route("/save", methods=["POST"])
def save():
    i = request.form['txtEmpID']
    n = request.form['txtName']
    e = request.form['txtEmailID']
    m = request.form['txtMobile']
    d = request.form['txtDes']
    s = request.form['txtSalary']

    cur = con.cursor()

    cur.execute(
        "INSERT INTO registration(empid,empname,emailid,mobile,designation,salary) VALUES (%s,%s,%s,%s,%s,%s)",
        (i, n, e, m, d, s)
    )

    con.commit()
    cur.close()

    return render_template("admin_reg_success.html")


@app.route("/admin_emp_profile")
def adminempprofile():
    id = request.args.get('eid')
    cur = con.cursor()

    cur.execute(f'select * from registration where empid = {id}')
    recordlist = cur.fetchall()
    print(recordlist)
    
    return render_template("admin_emp_profile.html",emplist = recordlist)

@app.route("/admin_emp_update",methods = ['post'])
def adminempupdate():

    i = request.form['txtEmpID']
    n = request.form['txtName']
    e = request.form['txtEmailID']
    m = request.form['txtMobile']
    d = request.form['txtDes']
    s = request.form['txtSalary']

    cur = con.cursor()

    cur.execute(
        "update registration set empid = %s, empname = %s, emailid = %s, mobile = %s, designation = %s, salary = %s where empid = %s",(i, n, e,m, d,s,i,)
    )

    con.commit()
    cur.close()

    return render_template("admin_emp_update_success.html")

@app.route("/admin_emp_delete")
def adminempdelete():

    id = request.args.get('id')

    
    print(id)
    cur = con.cursor()

    cur.execute(
        'delete from registration where empid = %s', (id,)
    )

    con.commit()
    cur.close()

    return render_template("admin_emp_delete_success.html")

@app.route("/admin_emp_searchprocess",methods = ['post'])
def adminempsearchresult():

    n = request.form['txtName']
    print(n)

    # id = request.args.get('id')

    
    # print(id)
    cur = con.cursor()

    q = f"select * from registration where empname like '{n}%'"
    print(q)

    cur.execute(
        q
    )

    emplist = cur.fetchall()
    print(emplist)

    # con.commit()
    cur.close()

    return render_template("admin_emp_searchresult.html",recordlist = emplist)

@app.route('/logout')
def logout():
    session["name"] = None
    return render_template('adminLogin.html')

app.run(debug=True)

