from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/start', methods = ['POST'])
def start():
    print request.form
    return 'start'

@app.route('/end', methods = ['POST'])
def end():
    print request.form
    return 'end'


@app.route('/change', methods = ['POST'])
def change():
    print request.form
    return 'change'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')