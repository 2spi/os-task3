from flask import Flask
app = Flask(__name__)

stack = [7, 6, 2]

@app.route('/')
def home():
    return 'api'

@app.route('/api/<val>', methods = ["PUSH"])
def push(val):
    if isinstance(val, int) and val > 0:
        stack.append(val)
        return f"{val} inserted."
    
    return "Value should be a positive integer."


@app.route('/api/<val>', methods = ["DELETE"])
def pop(val):
    if stack.isEmpty():
        return "Stack Empty."
    return stack.pop()

@app.route('/api/', methods = ["GET"])
def view():
    return stack