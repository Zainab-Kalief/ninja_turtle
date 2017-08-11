from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def helloNinja():
    return render_template('noNinja.html')

@app.route('/ninja')
def ninja():
    return render_template('ninja.html')

@app.route('/ninja/<color>')
def allNinjas(color):
    print color
    return render_template('ninjas.html', color = color)

app.run(debug=True)
