from flask import Flask, redirect, url_for, render_template
#from InsertEmp import insert_to_table
from SelectEmp import select_emp

app = Flask(__name__)

'''
@app.route('/run_script')
def run_script():
    insert_to_table()
    return render_template('base.html')
'''


@app.route("/", methods=['Get'])
def home():
    #return '<a href="/run_script">Add new employee</a>'
    return render_template('index.html') 

@app.route('/select_emp')
def select_emp1():
       data, column_names = select_emp()
       return render_template('employee.html', data=data, column_names=column_names)
   
@app.route('/new_emp')
def add_new_emp():
       return render_template('new_employee.html')

if __name__ == "__main__":
    app.run()