from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Full Stack Dev',
    'location': 'London',
    'salary': '£95,000',
    
  },

  {
    'id': 2,
    'title': 'Backend Dev',
    'location': 'London',
    'salary': '£75,000',
    
  },

  {
    'id': 3,
    'title': 'Frontend Dev',
    'location': 'London',
    
    
  },
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name='DevOps')
  
@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)