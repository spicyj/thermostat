from flask import Flask, render_template, jsonify
app = Flask(__name__)

import gpio
import monitor


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/api/heater_on')
def heater_on():
    return jsonify(heat=monitor.heat_on())


@app.route('/api/current_temp')
def current_temp():
    return jsonify(temp=gpio.get_temp())


if __name__ == "__main__":
    app.run(debug=True, port=18260)
