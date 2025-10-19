from flask import Flask, render_template, request
import math
from stack import Stack 



app = Flask(__name__)

stack = Stack()


#index
@app.route('/')
def index():
    return render_template('index.html')

#profile
@app.route('/profile')
def profile():
    return render_template('profile.html')

#works-STRING
@app.route('/works', methods=['GET', 'POST'])
def works():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

#works-CIRCLE area
@app.route('/areaOfcircle', methods=['GET', 'POST'])
def circle():
    if request.method == 'POST':
        try:
            radius = float(request.form['radius'])
            area = math.pi * radius**2
            formatted_area = round(area, 2)
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
            formatted_area = round(area, 2)
            return render_template('TRIANGLE.html', area=area, height=height, base=base)
        except ValueError:
            return render_template('TRIANGLE.html', error="hehe, please enter a valid number. >.<")
    return render_template('TRIANGLE.html')

#works-STACK
@app.route('/Stacks', methods=['GET', 'POST'])
def stacks():
    message = None

    if request.method == 'POST':
        action = request.form.get('action')
        # Always read the value and strip whitespace
        value = request.form.get('value', '').strip()

        if action == 'push':
            if not value:
                message = "Please enter a value to push."
            else:
                stack.push(value)
                message = f"Pushed '{value}'."

        elif action == 'pop':
            removed = stack.pop()
            message = f"Popped '{removed}'." if removed is not None else "Stack is empty."

        elif action == 'remove_beginning':
            removed = stack.remove_beginning()
            message = f"Removed from beginning: '{removed}'." if removed is not None else "Stack is empty."

        elif action == 'remove_end':
            removed = stack.remove_at_end()
            message = f"Removed from end: '{removed}'." if removed is not None else "Stack is empty."

        elif action == 'remove_at':
            if not value:
                message = "Please enter a value to remove."
            else:
                removed = stack.remove_at(value)
                message = f"Removed '{removed}'." if removed is not None else f"No node with value '{value}' found."

        else:
            message = f"Unknown action: {action}"

    current_stack = stack.display()
    return render_template('stacks.html', message=message, stack=current_stack)


#Contact
@app.route('/contact')
def contact():
    return render_template('contact.html')
if __name__ == "__main__":
    app.run(debug=True)