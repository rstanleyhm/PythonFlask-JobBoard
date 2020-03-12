from flask import Flask, app
from flask import render_template
app = Flask(__name__)


# The jobs function can be reached at / and /jobs
# by using these decorators
@app.route("/")
@app.route("/jobs")
def jobs():
    return render_template('index.html')
