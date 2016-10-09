from flask import Flask

app = Flask(__name__)

@app.route('/start', methods = ['POST'])
def start():
    return 'start'

@app.route('/end', methods = ['POST'])
def end():
    return 'end'


@app.route('/change', methods = ['POST'])
def change():
    return 'change'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')