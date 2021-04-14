from flask import Flask, render_template,flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask_ngrok import run_with_ngrok
app = Flask(__name__, )
app.config['UPLOAD_PATH'] = '/uploads'
run_with_ngrok(app)

@app.route("/")
def project(name=None):
    return render_template('project.html',name=name)

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
      return 'file uploaded successfully'
		
app.run()
