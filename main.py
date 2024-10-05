from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        feet = float(request.form['feet'])
        inches = feet * 12
        yards = feet * 0.333333333
        miles = feet * 0.000189393939
        return render_template('menu.html', feet=feet, inches=inches, yards=yards, miles=miles)
    return render_template('menu.html')

if __name__ == '__main__':
    app.run(debug=True)