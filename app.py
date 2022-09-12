from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id':1,
        'title':'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 100,1000'
    },
    {
        'id':2,
        'title':'Data Scientist',
        'location': 'Delhi, India',
        'salary': 'Rs. 150,1000'
    },
    {
        'id':3,
        'title':'Frontend Enigineer',
        'location': 'Bengaluru, India',
        
    },
    {
        'id':4,
        'title':'Backend Engineer',
        'location': 'San=fansisco',
        'salary': '$ 100,1000'
    },
]
@app.route("/")
def index():
    return render_template('home.html', jobs=JOBS, company_name='Jovian')

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(debug=True)