from flask import Flask, render_template,flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask_ngrok import run_with_ngrok
UPLOAD_FOLDER = '/uploads'
app = Flask(__name__, )
run_with_ngrok(app)
@app.route("/")
def project(name=None):
    return render_template('project.html',name=name)

@app.route('/uploader', methods = ['GET', 'POST'])
def upload():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
		

app.run()
