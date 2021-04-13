
from flask import Flask, render_template
from flask_ngrok import run_with_ngrok
app = Flask(__name__, )
run_with_ngrok(app)
@app.route("/")
def project():
    return render_template('project.html')
app.run()
