import os
from flask import Flask, jsonify, request , session
from src.process.atm import Atm_State
from src.db.database import DBManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

@app.route('/', methods=['POST'])
def health_check():
    return jsonify({'message': 'ATM is running'}), 200

# withddrawal operations
@app.route('/atm/withdrawal', methods=['POST'])
def atm_withdrawal():
    data = request.get_json()
    result = ATM.witdraw(data)

    if result.get('result') is None:
        return jsonify({'message': result['validation_message'] }), result['validation_status']
    else:
        return jsonify(result), 200

# refill operations
@app.route('/atm/refill', methods=['POST'])
def atm_refill():
    data = request.get_json()
    result = ATM.refill(data)
    return jsonify({'message': result['validation_message'] }), result['validation_status']

# done to reset database for initial state
@app.route('/atm/reset', methods=['POST'])
def atm_reset():
    result = ATM.reset_atm()
    return jsonify({'message': 'ATM Reset is done'}), 200

#main flask 
if __name__ == '__main__':

    app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'ATM.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
            
    with app.app_context():
        DbManager = DBManager(db=db)
        ATM = Atm_State(dbmanager=DbManager)
     
    app.run(host="0.0.0.0", port=3000,debug=True)
            