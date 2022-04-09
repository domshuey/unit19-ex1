from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_nums():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    res = add(a,b)
    return str(res)

@app.route('/sub')
def sub_nums():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    res = sub(a,b)
    return str(res)

@app.route('/mult')
def mult_nums():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    res = mult(a,b)
    return str(res)

@app.route('/div')
def div_nums():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    res = div(a,b)
    return str(res) 

operation = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

@app.route('/math/<operations>')
def operation_on_nums(operations):
    op = operation[operations]
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    res = op(a,b)
    return str(res)
