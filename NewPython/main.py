from flask import Flask, jsonify, abort, make_response
from Calendar import getCalendar
from Temperature import getTemperature
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/IOT/api/v1.0/Calendar', methods=['GET'])
def get_Calendar():
    return jsonify({'events': getCalendar()})
@app.route('/IOT/api/v1.0/status', methods=['GET'])
def get_status():
    return jsonify({'status':'connected'})
@app.route('/IOT/api/v1.0/Temperature', methods=['GET'])
def get_Temperature():
    return jsonify({'temperature': getTemperature()})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not found'}),404)
if __name__ == '__main__':
    app.run(debug=True)
