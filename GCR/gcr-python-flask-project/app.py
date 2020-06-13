import os
import logging

from flask import Flask

# Change the format of messages logged to Stackdriver
logging.basicConfig(format='%(message)s', level=logging.INFO)

app = Flask(__name__)

@app.route('/')
def home():
	html = """
<html>
 <head>
  <title>
   Google Cloud Run - Hello World with my course
  </title>
 </head>
 <body>
  <p>Hello World! I am running on Cloud Run </p>
  <a href="https://www.udemy.com/course/devsecops" target="_blank">DevSecOps : DevOps + Security course</a>
  <a href="https://www.udemy.com/course/sonarqube-master-sonarqube-within-a-few-hours-2020" target="_blank">SonarQube : SAST + Code Quality course</a>
 </body>
</html>
"""
	return html

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
