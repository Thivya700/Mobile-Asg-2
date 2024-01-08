
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def landing_page():
    return render_template('landing.html')

# Define other routes for main, hobby, portfolio, help/contact pages

if __name__ == '__main__':
    from flask_ngrok import run_with_ngrok
    run_with_ngrok(app)
    app.run()
