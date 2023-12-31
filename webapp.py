from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}!"

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello, {name}!"
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
