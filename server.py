from flask import Flask, render_template, request
from os import path
import shelve
app = Flask(__name__)
db = shelve.open(path.join(app.root_path, 'shelve.db'), writeback=True)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def submit():
    message = request.form['message']
    print(message)
    db.setdefault('messages', [])
    db['messages'].append(message)
    print(db['messages'])
    return render_template('index.html', submitted=True)

@app.route("/view")
def view():
    messages = db['messages']
    return render_template('view.html', messages=messages)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
