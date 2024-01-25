from flask import Flask, request, flash, jsonify
# from flask_cors import CORS
from werkzeug.utils import secure_filename

import os, sys
import time
import datetime
from pathlib import Path
import logging
from worker import predictWaste

logger = logging.getLogger(__name__)

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = 'static'

# remove files older than 1 minute (60s)
def removeTempFiles():
   for file in [
      obj for obj in Path(app.config['UPLOAD_FOLDER']).iterdir() 
      if obj.is_file() and not obj.name.startswith('.')
   ]:
      creation_date = datetime.datetime.fromtimestamp(os.path.getmtime(file))
      now = datetime.datetime.now()
      diff = now - creation_date
      if diff.seconds > 60:
         logging.debug('%s', f'Removing file {file.name}')
         os.remove(file)

def saveFile(f):
   filename = secure_filename(f.filename) 
   if filename=='':
      return (False, 'Empty filename')
   removeTempFiles()
   timestamp = time.time()
   name = ".".join(filename.split('.')[:-1]) + f'_{timestamp}' + '.' + filename.split('.')[-1]
   print(name)
   fullname = os.path.join(app.config['UPLOAD_FOLDER'], name)
   f.save(fullname)
   return (True, fullname)


@app.route('/check')
def check():
   return "69"


@app.route('/classify', methods = ['POST'])
def classifier():
   if 'file' not in request.files:
      flash('No file part!')
      return jsonify({"error": "No file parttype found in the request"}), 400
   
   file = request.files['file']
   # If the user does not select a file, the browser submits an empty file without a filename.
   if file.filename == '':
      flash('No selected file')
      return jsonify({"error": "No file parttype found in the request"}), 400
   
   if file:
      (result, filename) = saveFile(file)
      if result:
         result = predictWaste(filename)
         os.remove(filename)
      else:
         return filename
   return jsonify(result)


if __name__ == '__main__':
   logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
   app.run(debug=True, host='0.0.0.0', port=5000)

