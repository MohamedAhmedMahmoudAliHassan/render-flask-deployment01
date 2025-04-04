from flask import Flask, redirect, url_for, render_template
from InsertEmp import insert_to_table

app = Flask(__name__)

@app.route('/run_script')
def run_script():
    insert_to_table()
    return render_template('base.html')

@app.route("/", methods=['Get'])
def home():
    #return '<a href="/run_script">Add new employee</a>'
    return render_template('index.html') 

if __name__ == "__main__":
    app.run()