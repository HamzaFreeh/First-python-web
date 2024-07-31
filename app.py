from flask import Flask, render_template, jsonify
from flask.typing import TemplateFilterCallable

JOBS = [
    {
         'id':1,
         'title': 'Data Analyst',
         'location': 'Bengaluru, India',
         'salary': 'Rs. 10,00,000'
    },
    {
         'id':2,
         'title': 'Data Scientist',
         'location': 'Delhi, India',
         'salary': 'Rs. 15,00,000'
    },
    {
         'id':3,
         'title': 'Front-end Engineer',
         'location': 'Remote',
         'salary': 'Rs. 12,00,000'
    },
    {
         'id':1,
         'title': 'Back-end Engineer',
         'location': 'San Francisco, USA',
         'salary': '$120,000'
    },
]

app = Flask(__name__)
@app.route("/")
def hello():
    return render_template("home.html",jobs=JOBS,company_name="Hamza")

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__" :
  app.run(host='0.0.0.0', debug=True)
