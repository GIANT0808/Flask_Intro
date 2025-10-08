from flask import Flask, render_template, request
<<<<<<< HEAD
import math


app = Flask(__name__)


#index
=======

app = Flask(__name__)

>>>>>>> 04210ba4083968f729d6821c95d2794bd9bbb7a1
@app.route('/')
def index():
    return render_template('index.html')

<<<<<<< HEAD
#profile
=======
>>>>>>> 04210ba4083968f729d6821c95d2794bd9bbb7a1
@app.route('/profile')
def profile():
    return render_template('profile.html')

<<<<<<< HEAD
#works-STRING
=======
>>>>>>> 04210ba4083968f729d6821c95d2794bd9bbb7a1
@app.route('/works', methods=['GET', 'POST'])
def works():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

<<<<<<< HEAD
#works-CIRCLE area
@app.route('/areaOfcircle', methods=['GET', 'POST'])
def circle():
    if request.method == 'POST':
        try:
            radius = float(request.form['radius'])
            area = math.pi * radius**2
            return render_template('CIRCLE.html', area=area, radius=radius)
        except ValueError:
            return render_template('CIRCLE.html', error="hehe, please enter a valid number. >.<")
    return render_template('CIRCLE.html')

#works-TRIANGLE
@app.route('/areaOftriangle', methods = ['GET', 'POST'])
def triangle():
    if request.method == 'POST':
        try:
            base = float(request.form['base'])
            height = float(request.form['height'])
            area = 0.5 * base * height
            return render_template('TRIANGLE.html', area=area, height=height, base=base)
        except ValueError:
            return render_template('TRIANGLE.html', error="hehe, please enter a valid number. >.<")
    return render_template('TRIANGLE.html')
    
#Contact
@app.route('/contact')
def contact():
    return render_template('contact.html')
=======
@app.route('/contact')
def contact():
    return "Contact Page. please create me an html page with dummy contact info"

>>>>>>> 04210ba4083968f729d6821c95d2794bd9bbb7a1
if __name__ == "__main__":
    app.run(debug=True)
