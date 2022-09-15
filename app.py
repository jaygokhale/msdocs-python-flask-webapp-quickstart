from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import requests
import os
app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)

       response = requests.get('https://adventureapim.azure-api.net/AdventureFunctionApp/GradingTriggerv3?name=1854'), 
       headers={
            "Ocp-Apim-Subscription-Key": "ec610f8bddfe41ba80bcdca6ac051ef0"
         }
       print(response)
       #instead of rendering hello.html I need to call and API 

    #  return render_template('hello.html', name = name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()