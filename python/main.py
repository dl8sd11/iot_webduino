from flask import Flask, jsonify, abort, make_response,request, send_from_directory
from Calendar import getCalendar
from Traffic import updateTraffic
from Kitchen import getRecipe
from Temperature import getTemperature
from Outdoor import getOutdoorInfo
from flask_cors import CORS
app = Flask(__name__ , static_url_path='/src')
CORS(app)

clotheshorse = 2;

@app.route('/IOT/api/v1.0/Calendar', methods=['GET'])
def get_Calendar():
    return jsonify({'events': getCalendar()})
@app.route('/IOT/api/v1.0/status', methods=['GET'])
def get_status():
    return jsonify({'status':'connected'})
@app.route('/IOT/api/v1.0/Temperature', methods=['GET'])
def get_Temperature():
    return jsonify({'temperature': getTemperature()})
@app.route('/IOT/api/v1.0/Outdoor', methods=['GET'])
def get_Outdoor():
    return jsonify(getOutdoorInfo())
@app.route('/IOT/api/v1.0/Traffic',methods=['GET'])
def update_traffix():
    updateTraffic()
    return "Yes Sir"
@app.route('/IOT/api/v1.0/getCollectClothes',methods=['GET'])
def get_Collect_Clothes():
    return jsonify(clotheshorse);
@app.route('/IOT/api/v1.0/Recipe')
def get_Recipe():
    return jsonify({'recipe':getRecipe()});
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not found'}),404)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
    #DIdkiZS7
