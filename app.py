from flask import Flask, render_template
from flask_ngrok import run_with_ngrok
app = Flask(__name__, )
run_with_ngrok(app)
@app.route("/")
def project(name=None):
    return render_template('project.html',name=name)
app.run()
