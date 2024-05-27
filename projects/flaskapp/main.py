from flask import Flask
from random import randint
from projects.pythonpro.calc import Calculate

app = Flask(__name__)
my_calculator = Calculate()

@app.route('/')
def hello():
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    message = "{} + {} = {}".format(num1, num2, my_calculator.add(num1, num2))

if __name__ == 'main':
    app.run()  
