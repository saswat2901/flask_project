from flask import Flask, render_template

app = Flask(__name__)

jobs = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Full Stack Developer',
        'location': 'NOIDA, India',
        'salary': 'Rs. 30,00,000'
    },
    {
        'id': 3,
        'title': 'Quality & Assurance',
        'location': 'DELHI, India',
        'salary': 'Rs. 12,00,000'
    },
]


@app.route('/')
def home():
    """Render the homepage with the list of jobs."""
    return render_template('home.html', jobs=jobs, companyname="SAFASWFATFA")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
