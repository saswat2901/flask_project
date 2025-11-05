from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask Project</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                text-align: center;
            }
            h1 {
                color: #333;
            }
            p {
                color: #666;
                line-height: 1.6;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to Flask Project</h1>
        <p>This is a basic Flask application running on Replit.</p>
        <p>You can start building your web application here!</p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
