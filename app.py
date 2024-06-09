from flask import Flask, jsonify, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 10,00,000'
    },
    
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Delhi, India',
        'salary': 'Rs. 15,00,000'
    },
    
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Remote',
        'salary': 'Rs. 12,00,000'
    },

    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'San Francisco, USA',
    }

]

@app.route("/")
def home():
    return render_template('home.html', style='CSS/style.css', jobs=JOBS)


@app.route("/about")
def about():
    return render_template('about.html', style='CSS/style.css')

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
